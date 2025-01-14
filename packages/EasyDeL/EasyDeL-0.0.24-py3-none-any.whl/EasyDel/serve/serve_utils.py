import copy
import functools
import os
import typing

import flax.core
import gradio as gr
import jax
import tqdm
import transformers
import uvicorn
from fastapi import FastAPI
from fjutils import make_shard_and_gather_fns, match_partition_rules, with_sharding_constraint
from fjutils.utils import read_ckpt
from typing import Optional, List, Union
from EasyDel.smi import get_mem, initialise_tracking
from flax.core import freeze
from flax.traverse_util import unflatten_dict
from jax import numpy as jnp
from jax.experimental import mesh_utils, pjit

from ml_collections import ConfigDict
from pydantic import BaseModel
from fjutils import get_float_dtype_by_name
from jax.sharding import Mesh, PartitionSpec as Ps
from transformers import GenerationConfig, TextIteratorStreamer
from EasyDel.serve.theme import seafoam
import logging
from EasyDel.utils.utils import RNG
import multiprocessing as mp
import torch
from EasyDel.utils.utils import prefix_str

pjit = pjit.pjit


def get_dtype(dtype):
    if isinstance(dtype, str):
        dtype = get_float_dtype_by_name(dtype)
    return dtype


def shard_params(params, partition_rules,
                 shard_mesh_shape=(1, -1, 1),
                 backend='gpu',
                 shard_mesh=('dp', 'fsdp', 'mp'), do_unf=True,
                 dtype='fp16'):
    dtype = get_dtype(dtype)
    params = unflatten_dict(params) if do_unf else params
    params = freeze(params)
    mxd = jax.device_count(backend)
    rsp = jnp.asarray([1, mxd, 1]).reshape(shard_mesh_shape)
    phs_mesh = mesh_utils.create_device_mesh(rsp.tolist(), )
    mesh = jax.sharding.Mesh(phs_mesh, shard_mesh)
    ps = match_partition_rules(
        partition_rules,
        params
    )
    with mesh:
        shard_fns, _ = make_shard_and_gather_fns(
            ps, dtype
        )
        params = jax.tree_util.tree_map(lambda fn, x: fn(x), shard_fns, params)
    return params, mesh


class InstructRequest(BaseModel):
    prompt: str
    system: Optional[str] = None
    temperature: Optional[float] = None
    greedy: Optional[bool] = False


class ChatRequest(BaseModel):
    prompt: str
    history: Union[List[List], None] = None
    temperature: Optional[float] = None
    greedy: Optional[bool] = False


class JAXServer(object):

    def __init__(self, config=None):

        self.process_uvicorn, self.prefix_tokenizer, self.params, self.tokenizer, self.model, \
            self.rules, self._generate, self._greedy_generate = [None] * 8

        self.config = self.get_default_config(config)
        self._funcs_generated = False
        self.number_of_served_request_until_last_up_time = 0

        self.rng_generator = RNG(42)
        initialise_tracking(0.5)
        array = jnp.ones((len(jax.devices()), 1)).reshape(self.config.mesh_axes_shape)
        self.mesh = Mesh(mesh_utils.create_device_mesh(array.shape), self.config.mesh_axes_names)

        self.app = FastAPI()
        self.app.post('/chat')(self.forward_chat)
        self.app.post('/instruct')(self.forward_instruct)
        self.app.get('/status')(self.status)
        self.gradio_app_chat = self.create_gradio_ui_chat()
        self.gradio_app_instruct = self.create_gradio_ui_instruct()
        self.app = gr.mount_gradio_app(self.app, self.gradio_app_chat, '/gradio_chat')
        self.app = gr.mount_gradio_app(self.app, self.gradio_app_instruct, '/gradio_instruct')

    @staticmethod
    def get_default_config(updates=None):
        config = ConfigDict()
        config.host = '0.0.0.0'
        config.port = 2059

        config.instruct_format = '### SYSTEM:\n{system}\n### INSTRUCT:\n{instruct}\n### ASSISTANT:\n'
        config.chat_format = '<|prompter|>{prompt}</s><|assistant|>{assistant}</s>'

        config.batch_size = 1

        config.system_prefix = ''
        config.system = ''

        config.prompt_prefix_instruct = ''
        config.prompt_postfix_instruct = ''

        config.prompt_prefix_chat = '<|prompter|>'
        config.prompt_postfix_chat = '</s><|assistant|>'

        config.chat_prefix = ''
        config.contains_auto_format = True

        config.max_length = 2048
        config.max_new_tokens = 2048

        config.max_stream_tokens = 32

        assert config.max_new_tokens % config.max_stream_tokens == 0, \
            'max_new_tokens should be divisible by  max_new_tokens' \
            f'{config.max_new_tokens % config.max_stream_tokens}'

        config.temperature = 0.1
        config.top_p = 0.95
        config.top_k = 50

        config.logging = True

        config.mesh_axes_names = ('dp', 'fsdp', 'mp')
        config.mesh_axes_shape = (1, -1, 1)

        config.dtype = 'fp16'

        config.use_prefix_tokenizer = True

        if updates is not None:
            config.update(ConfigDict(updates).copy_and_resolve_references())
        return config

    def status(self):
        return {
            'config': {k: v for k, v in self.config.__dict__.items()},
            'devices': f"{jax.devices()}",
            'number_of_backends': len(jax.devices()),
            'status': 'Ready',
            'number_of_served_request_until_last_up_time': f"{self.number_of_served_request_until_last_up_time}",
            'memory': f"{get_mem()}"
        }

    @staticmethod
    def get_memory():
        return get_mem()

    def configure_generate_functions(self, model, tokenizer):

        assert self.rules is not None, 'you should first shard params with using ``shard_params`` method'

        if tokenizer.pad_token is None:
            logging.info(
                'Tokenizer does not contain padding token setting padding token to eos token for open end generation')
            tokenizer.pad_token = tokenizer.eos_token

        try:
            tokenizer.padding_side = 'left'
            tokenizer.truncation_side = 'left'
            self.prefix_tokenizer = copy.deepcopy(tokenizer)
            tokenizer.padding_side = 'right'
            tokenizer.truncation_side = 'right'
            self.tokenizer = copy.deepcopy(tokenizer)
        except:
            prefix_str(
                'Warning', f'The class Model of Tokenizer {type(tokenizer)} do not support deepcopy option '
            )
            if self.config.use_prefix_tokenizer:
                tokenizer.padding_side = 'left'
                tokenizer.truncation_side = 'left'
            else:
                tokenizer.padding_side = 'right'
                tokenizer.truncation_side = 'right'
            self.prefix_tokenizer = tokenizer

        @functools.partial(
            pjit,
            in_shardings=(self.rules, Ps(), Ps()),
            out_shardings=(Ps())
        )
        def greedy_generate(parameters, input_ids, attention_mask):
            input_ids = with_sharding_constraint(input_ids, Ps(('dp', 'fsdp')))
            attention_mask = with_sharding_constraint(attention_mask, Ps(('dp', 'fsdp')))
            predict = model.generate(
                input_ids,
                attention_mask=attention_mask,
                params=parameters,
                generation_config=GenerationConfig(
                    max_new_tokens=self.config.max_stream_tokens,
                    eos_token_id=tokenizer.eos_token_id,
                    pad_token_id=tokenizer.pad_token_id,
                    bos_token_id=tokenizer.bos_token_id,

                    temperature=self.config.temperature,
                    do_sample=False,
                    num_beams=1,
                )
            ).sequences[:, input_ids.shape[1]:]
            return predict

        @functools.partial(
            pjit,
            in_shardings=(self.rules, Ps(), Ps()),
            out_shardings=(Ps())
        )
        def generate(parameters, input_ids, attention_mask):
            input_ids = with_sharding_constraint(input_ids, Ps(('dp', 'fsdp')))
            attention_mask = with_sharding_constraint(attention_mask, Ps(('dp', 'fsdp')))
            predict = model.generate(
                input_ids,
                attention_mask=attention_mask,
                params=parameters,
                generation_config=GenerationConfig(
                    max_new_tokens=self.config.max_stream_tokens,

                    eos_token_id=tokenizer.eos_token_id,
                    pad_token_id=tokenizer.pad_token_id,
                    bos_token_id=tokenizer.bos_token_id,

                    temperature=self.config.temperature,
                    do_sample=True,
                    num_beams=1,
                    top_p=self.config.top_p,
                    top_k=self.config.top_k,
                )
            ).sequences[:, input_ids.shape[1]:]
            return predict

        self._generate = generate
        self._greedy_generate = greedy_generate
        self._funcs_generated = True

    def auto_configure(self, model, params, tokenizer, partition_rules):
        self.shard_params(params=params, partition_rules=partition_rules)
        self.configure_generate_functions(model, tokenizer)

    def generate(self,
                 params: Union[flax.core.FrozenDict, dict],
                 input_ids: jax.Array,
                 attention_mask: jax.Array,
                 ):
        if not self._funcs_generated:
            raise NotImplementedError(
                'this method will be implemented automatically after using ``configure_generate_functions`` function'
            )
        else:
            with self.mesh:
                return self._generate(
                    params, input_ids, attention_mask
                )

    @classmethod
    def load(
            cls,
            model: transformers.FlaxPreTrainedModel,
            config_model: transformers.PretrainedConfig,
            tokenizer: transformers.PreTrainedTokenizer,
            path: typing.Union[str, os.PathLike],
            config=None,
            add_param_field: bool = True,
            init_shape: tuple = (1, 1)
    ):
        assert hasattr(model,
                       'init_weights'), 'model must contain init_weights func in order to init params for shard_fns'
        assert hasattr(config_model, 'get_partition_rules'), 'config_model must contain get_partition_rules functions'
        server = cls(config=config)

        def _init():
            return model.init_weights(jax.random.PRNGKey(0), init_shape)

        shape = jax.eval_shape(_init)
        rules = match_partition_rules(params=shape, rules=config_model.get_partition_rules(True))
        with server.mesh:
            shard_fns, _ = make_shard_and_gather_fns(rules, get_float_dtype_by_name(server.config.dtype))

            params = read_ckpt(
                path=path, shard_fns=flax.traverse_util.flatten_dict(shard_fns)
            )
        params = flax.traverse_util.unflatten_dict(params)
        params = {'params': params} if add_param_field else params

        server.rules = {'params': rules} if add_param_field else rules
        server.params = params
        server.configure_generate_functions(model, tokenizer)
        return server

    @classmethod
    def load_from_params(
            cls,
            model: transformers.FlaxPreTrainedModel,
            config_model: transformers.PretrainedConfig,
            tokenizer: transformers.PreTrainedTokenizer,
            params: typing.Dict,
            config=None,
            add_param_field: bool = True,
    ):
        assert hasattr(model,
                       'init_weights'), 'model must contain init_weights func in order to init params for shard_fns'
        assert hasattr(config_model, 'get_partition_rules'), 'config_model must contain get_partition_rules functions'
        server = cls(config=config)

        with server.mesh:
            rules = match_partition_rules(params=params, rules=config_model.get_partition_rules(True))
            shard_fns, _ = make_shard_and_gather_fns(rules, get_float_dtype_by_name(server.config.dtype))

            params = jax.tree_util.tree_map(
                lambda f, p: f(p), shard_fns, params
            )

        params = {'params': params} if add_param_field else params

        server.rules = {'params': rules} if add_param_field else rules
        server.params = params
        server.configure_generate_functions(model, tokenizer)
        return server

    def greedy_generate(self,
                        params: Union[flax.core.FrozenDict, dict],
                        input_ids: jax.Array,
                        attention_mask: jax.Array,
                        ):
        if not self._funcs_generated:
            raise NotImplementedError(
                'this method will be implemented automatically after using ``configure_generate_functions`` function'
            )
        else:
            with self.mesh:
                return self._greedy_generate(
                    params, input_ids, attention_mask
                )

    def save_params(self, params):

        assert self.rules is not None, 'you first must shard params using ``shard_params`` method'
        self.params = params

    def shard_params(self, params, partition_rules):

        logging.log(
            logging.INFO,
            'the parameters will be sharded and ba saved inside server you can access them by ``JAXServer.params``')
        rules = match_partition_rules(params=params, rules=partition_rules)
        self.rules = rules
        shard_fns, _ = make_shard_and_gather_fns(rules, get_float_dtype_by_name(self.config.dtype))

        with self.mesh:
            new_parameters = jax.tree_map(
                lambda f, p: f(p), shard_fns, params
            )
        self.save_params(new_parameters)

        return new_parameters

    def forward_chat(self, data: ChatRequest):

        if not self._funcs_generated:
            return {
                'status': "down"
            }

        history = self.process_chat_history(data.history or [])
        history += self.config.prompt_prefix_chat + data.prompt + self.config.prompt_postfix_chat

        response, used_tokens = self.process(
            string=history,
            greedy=data.greedy,
            max_new_tokens=None
        )
        self.number_of_served_request_until_last_up_time += 1
        return {
            'input': f'{history}',
            'response': response,
            'tokens_used': used_tokens,
        }

    def forward_instruct(self, data: InstructRequest):
        if not self._funcs_generated:
            return {
                'status': "down"
            }

        string = self.config.instruct_format.format(instruct=data.prompt, system=data.system)

        response, used_tokens = self.process(
            string=string,
            greedy=data.greedy,
            max_new_tokens=None
        )
        self.number_of_served_request_until_last_up_time += 1
        return {
            'input': f'{string}',
            'response': response,
            'tokens_used': used_tokens,
        }

    def forward_instruct_non_api(self, prompt, system, greedy):
        data = InstructRequest(
            prompt=prompt,
            system=system,
            greedy=greedy
        )
        return self.forward_instruct(data)

    def forward_chat_non_api(self, prompt, history, greedy):
        data = ChatRequest(
            prompt=prompt,
            history=history,
            greedy=greedy
        )
        return self.forward_chat(data)

    def process(self,
                string,
                greedy: bool = False,
                max_new_tokens: int = None,
                pbar=tqdm
                ):
        tokens = self.prefix_tokenizer(
            string,
            max_length=self.config.max_length - self.config.max_stream_tokens,
            padding='max_length',
            return_tensors='jax'
        ) \
            if self.config.use_prefix_tokenizer else \
            self.tokenizer(
                string,
                return_tensors='jax'
            )

        input_ids = tokens.input_ids
        attention_mask = tokens.attention_mask
        num_generated_tokens = 0
        pad = self.config.max_length - self.config.max_stream_tokens

        for _ in pbar.tqdm(range((max_new_tokens or self.config.max_new_tokens) // self.config.max_stream_tokens),
                           ):
            predicted_token = self.greedy_generate(
                params=self.params,
                input_ids=input_ids,
                attention_mask=attention_mask
            ) if greedy else self.generate(
                params=self.params,
                input_ids=input_ids,
                attention_mask=attention_mask
            )

            num_generated_tokens += predicted_token.shape[-1]

            input_ids = jnp.concatenate(
                (input_ids, predicted_token), axis=-1
            )[:, -pad:]
            attention_mask = jnp.concatenate(
                (attention_mask, jnp.ones((len(attention_mask), self.config.max_stream_tokens), dtype=jnp.int32)),
                axis=-1
            )[:, -pad:]
            if predicted_token[0][-1] == self.tokenizer.eos_token_id or predicted_token[0][
                -1] == self.prefix_tokenizer.eos_token_id:
                break

        return self.tokenizer.decode(input_ids[0][-num_generated_tokens:],
                                     skip_special_tokens=True), num_generated_tokens

    def process_chat_history(self, history: List):
        if len(history) == 0:
            return ''
        else:
            message_history = ''
            for message in history:
                message_history += self.config.chat_format.format(prompt=message[0], assistant=message[1])

        return message_history

    def process_gradio_chat(self, prompt, history, max_new_tokens, greedy, pbar=gr.Progress()):
        string = self.process_chat_history(history)
        string += self.config.prompt_prefix_chat + prompt + self.config.prompt_postfix_chat
        response, _ = self.process(
            string=string,
            greedy=greedy,
            max_new_tokens=max_new_tokens,
            pbar=pbar
        )
        history.append([prompt, response])
        return '', history

    def process_gradio_instruct(self, prompt, system, max_new_tokens, greedy, pbar=gr.Progress()):
        string = self.config.instruct_format.format(system=system, instruct=prompt)
        response, _ = self.process(
            string=string,
            greedy=greedy,
            max_new_tokens=max_new_tokens,
            pbar=pbar
        )
        return '', response

    def create_gradio_ui_chat(self):
        with gr.Blocks(
                theme=seafoam) as block:
            gr.Markdown("# <h1> <center>Powered by [EasyDeL](https://github.com/erfanzar/EasyDel) </center> </h1>")
            with gr.Row():
                history = gr.Chatbot(elem_id="EasyDel", label="EasyDel", container=True, height=600)

            with gr.Row():
                with gr.Column():
                    prompt = gr.Textbox(show_label=False, placeholder='Message Box', container=False)
                with gr.Column():
                    with gr.Row():
                        submit = gr.Button(variant="primary")
                        stop = gr.Button(value='Stop ')
                        clear = gr.Button(value='Clear Conversation')

            with gr.Row():
                with gr.Accordion('Advanced Options', open=False):
                    max_new_tokens = gr.Slider(value=self.config.max_new_tokens, maximum=10000,
                                               minimum=self.config.max_stream_tokens,
                                               label='Max New Tokens', step=self.config.max_stream_tokens, )
                    max_length = gr.Slider(value=self.config.max_length, maximum=self.config.max_length, minimum=1,
                                           label='Max Length', step=1)
                    temperature = gr.Slider(value=0.2, maximum=1, minimum=0.1, label='Temperature', step=0.01)

                    greedy = gr.Checkbox(value=True, label='Greedy Search')

            inputs = [prompt, history, max_new_tokens, greedy]
            sub_event = submit.click(fn=self.process_gradio_chat, inputs=inputs, outputs=[prompt, history])

            def clear_():
                return []

            clear.click(fn=clear_, outputs=[history])
            txt_event = prompt.submit(fn=self.process_gradio_chat, inputs=inputs, outputs=[prompt, history])

            stop.click(fn=None, inputs=None, outputs=None, cancels=[txt_event, sub_event])

        block.queue()
        return block

    def create_gradio_ui_instruct(self):
        with gr.Blocks(
                theme=seafoam) as block:
            gr.Markdown("# <h1> <center>Powered by [EasyDeL](https://github.com/erfanzar/EasyDel) </center> </h1>")
            with gr.Row():
                pred = gr.TextArea(elem_id="EasyDel", label="EasyDel", container=True, height=600)

            with gr.Row():
                submit = gr.Button(variant="primary")
                stop = gr.Button(value='Stop ')
                clear = gr.Button(value='Clear Conversation')
            with gr.Column():
                prompt = gr.Textbox(show_label=False, placeholder='Instruct Message', container=False)
                system = gr.Textbox(value='You Are an helpful AI Assistant, generate good and helpful answers',
                                    show_label=False, placeholder='System Message', container=False)

            with gr.Row():
                with gr.Accordion('Advanced Options', open=False):
                    max_new_tokens = gr.Slider(value=self.config.max_new_tokens, maximum=10000,
                                               minimum=self.config.max_stream_tokens,
                                               label='Max New Tokens', step=self.config.max_stream_tokens, )
                    max_length = gr.Slider(value=self.config.max_length, maximum=self.config.max_length, minimum=1,
                                           label='Max Length', step=1)
                    temperature = gr.Slider(value=0.2, maximum=1, minimum=0.1, label='Temperature', step=0.01)
                    greedy = gr.Checkbox(value=True, label='Greedy Search')

            inputs = [prompt, system, max_new_tokens, greedy]
            sub_event = submit.click(fn=self.process_gradio_instruct, inputs=inputs, outputs=[prompt, pred])

            def clear_():
                return ''

            clear.click(fn=clear_, outputs=[pred])
            txt_event = prompt.submit(fn=self.process_gradio_instruct, inputs=inputs, outputs=[prompt, pred])

            stop.click(fn=None, inputs=None, outputs=None, cancels=[txt_event, sub_event])

        block.queue()
        return block

    def fire(self):
        assert self._funcs_generated, 'you have to first add your model and parameters into server before using fire ' \
                                      'with using ``configure_generate_functions``'

        def run():
            uvicorn.run(self.app, host=self.config.host, port=self.config.port)

        self.process_uvicorn = mp.Process(target=run)
        self.process_uvicorn.start()

    def end(self):
        if self.process_uvicorn is not None:
            self.process_uvicorn.join()
        else:
            logging.warning('you have to fire server before ending that this command will be ignored')


class PyTorchServer(object):

    def __init__(self, config=None):
        logging.warning('PytorchServer is not built fully yet at this version')

        self.config = self.get_default_config(config)
        self.app = FastAPI()
        self.number_of_served_request_until_last_up_time = 0
        self.device_rolling = self.get_gpu_memory(self.config.max_number_of_gpus)
        self.dict_max_memory_sharding = {i: str(int(mem * self.config.max_gpu_perc_to_use)) + 'GiB' for i, mem in
                                         enumerate(self.device_rolling)}
        self.app.post('/chat')(self.forward_chat)
        self.app.post('/instruct')(self.forward_instruct)
        self.app.get('/status')(self.status)
        self.app = gr.mount_gradio_app(self.app, self.create_gradio_ui(), '/gradio_app')

    @staticmethod
    def get_default_config(updates=None):
        config = ConfigDict()
        config.host = '0.0.0.0'
        config.port = 2059

        config.instruct_format = '### SYSTEM:\n{system}\n### INSTRUCT:\n{instruct}\n### ASSISTANT:\n'
        config.chat_format = '<|prompter|>{prompt}</s><|assistant|>{assistant}</s>'

        config.batch_size = 1

        config.system_prefix = ''
        config.system = ''

        config.prompt_prefix_instruct = ''
        config.prompt_postfix_instruct = ''

        config.prompt_prefix_chat = '<|prompter|>'
        config.prompt_postfix_chat = '</s><|assistant|>'

        config.chat_prefix = ''
        config.contains_auto_format = True

        config.max_length = 2048
        config.max_new_tokens = 2048

        config.temperature = 0.8
        config.top_p = 0.95
        config.top_k = 50

        config.logging = True

        config.dtype = 'fp16'

        if updates is not None:
            config.update(ConfigDict(updates).copy_and_resolve_references())
        return config

    @staticmethod
    def get_gpu_memory(num_gpus_req=None):

        gpu_m = []
        dc = torch.cuda.device_count()
        num_gpus = torch.cuda.device_count() if num_gpus_req is None else min(num_gpus_req, dc)

        for gpu_id in range(num_gpus):
            with torch.cuda.device(gpu_id):
                gpu_properties = torch.cuda.get_device_properties(torch.cuda.current_device())
                gpu_m.append(
                    (gpu_properties.total_memory / (1024 ** 3)) - (torch.cuda.memory_allocated() / (1024 ** 3)))
        return gpu_m

    def get_model_load_kwargs(self):
        if self.config.dtype == 'fp16':
            dtype = torch.float16
        elif self.config.dtype == 'fp32':
            dtype = torch.float32
        elif self.config.dtype == 'bf16':
            dtype = torch.bfloat16
        else:
            raise ValueError('unknown type available types are [fp32 fp16 bf16]')
        load_kwargs = {
            'torch_dtype': dtype,
            'device_map': 'auto',
            'max_memory': self.dict_max_memory_sharding
        }
        return load_kwargs

    def status(self):

        return {
            'config': {k: v for k, v in self.config.__dict__.items()},
            'devices': f"{torch.cuda.device_count()}",
            'device_sharding': self.device_rolling,
            'max_memory': self.dict_max_memory_sharding,
            'status': 'Ready',
            'number_of_served_request_until_last_up_time': f"{self.number_of_served_request_until_last_up_time}"
        }

    def forward_instruct_non_api(self, prompt, system, greedy):
        data = InstructRequest(
            prompt=prompt,
            system=system,
            greedy=greedy
        )
        return self.forward_instruct(data)

    def forward_chat_non_api(self, prompt, history, greedy):
        data = ChatRequest(
            prompt=prompt,
            history=history,
            greedy=greedy
        )
        return self.forward_chat(data)

    def process(self,
                string,
                greedy: bool = False,
                max_new_tokens: int = None,
                pbar=tqdm
                ):
        tokens = self.tokenizer(

        )
        input_ids = tokens.input_ids
        attention_mask = tokens.attention_mask
        num_generated_tokens = 0
        pad = self.config.max_length - self.config.max_stream_tokens

        stream = TextIteratorStreamer(
            tokenizer=self.tokenizer,
            skip_prompt=True,
            skip_special_tokens=True
        )

        return 1, 1

    def process_chat_history(self, history: List):
        if len(history) == 0:
            return ''
        else:
            message_history = ''
            for message in history:
                message_history += self.config.chat_format.format(prompt=message[0], assistant=message[1])

        return message_history

    def process_gradio_chat(self, prompt, history, max_new_tokens, greedy, pbar=gr.Progress()):
        string = self.process_chat_history(history)
        string += self.config.prompt_prefix_chat + prompt + self.config.prompt_postfix_chat
        response, _ = self.process(
            string=string,
            greedy=greedy,
            max_new_tokens=max_new_tokens,
            pbar=pbar
        )
        history.append([prompt, response])
        return '', history

    def process_gradio_instruct(self, prompt, system, max_new_tokens, greedy, pbar=gr.Progress()):
        string = self.config.instruct_format.format(system=system, instruct=prompt)
        response, _ = self.process(
            string=string,
            greedy=greedy,
            max_new_tokens=max_new_tokens,
            pbar=pbar
        )
        return '', response

    def create_gradio_ui_chat(self):
        with gr.Blocks(
                theme=seafoam) as block:
            gr.Markdown("# <h1> <center>Powered by [EasyDeL](https://github.com/erfanzar/EasyDel) </center> </h1>")
            with gr.Row():
                history = gr.Chatbot(elem_id="EasyDel", label="EasyDel", container=True, height=600)

            with gr.Row():
                with gr.Column():
                    prompt = gr.Textbox(show_label=False, placeholder='Message Box', container=False)
                with gr.Column():
                    with gr.Row():
                        submit = gr.Button(variant="primary")
                        stop = gr.Button(value='Stop ')
                        clear = gr.Button(value='Clear Conversation')

            with gr.Row():
                with gr.Accordion('Advanced Options', open=False):
                    max_new_tokens = gr.Slider(value=self.config.max_new_tokens, maximum=10000,
                                               minimum=self.config.max_stream_tokens,
                                               label='Max New Tokens', step=self.config.max_stream_tokens, )
                    max_length = gr.Slider(value=self.config.max_length, maximum=self.config.max_length, minimum=1,
                                           label='Max Length', step=1)
                    temperature = gr.Slider(value=0.2, maximum=1, minimum=0.1, label='Temperature', step=0.01)

                    greedy = gr.Checkbox(value=True, label='Greedy Search')

            inputs = [prompt, history, max_new_tokens, greedy]
            sub_event = submit.click(fn=self.process_gradio_chat, inputs=inputs, outputs=[prompt, history])

            def clear_():
                return []

            clear.click(fn=clear_, outputs=[history])
            txt_event = prompt.submit(fn=self.process_gradio_chat, inputs=inputs, outputs=[prompt, history])

            stop.click(fn=None, inputs=None, outputs=None, cancels=[txt_event, sub_event])

        block.queue()
        return block

    def create_gradio_ui_instruct(self):
        with gr.Blocks(
                theme=seafoam) as block:
            gr.Markdown("# <h1> <center>Powered by [EasyDeL](https://github.com/erfanzar/EasyDel) </center> </h1>")
            with gr.Row():
                pred = gr.TextArea(elem_id="EasyDel", label="EasyDel", container=True, height=600)

            with gr.Row():
                submit = gr.Button(variant="primary")
                stop = gr.Button(value='Stop ')
                clear = gr.Button(value='Clear Conversation')
            with gr.Column():
                prompt = gr.Textbox(show_label=False, placeholder='Instruct Message', container=False)
                system = gr.Textbox(value='You Are an helpful AI Assistant, generate good and helpful answers',
                                    show_label=False, placeholder='System Message', container=False)

            with gr.Row():
                with gr.Accordion('Advanced Options', open=False):
                    max_new_tokens = gr.Slider(value=self.config.max_new_tokens, maximum=10000,
                                               minimum=self.config.max_stream_tokens,
                                               label='Max New Tokens', step=self.config.max_stream_tokens, )
                    max_length = gr.Slider(value=self.config.max_length, maximum=self.config.max_length, minimum=1,
                                           label='Max Length', step=1)
                    temperature = gr.Slider(value=0.2, maximum=1, minimum=0.1, label='Temperature', step=0.01)
                    greedy = gr.Checkbox(value=True, label='Greedy Search')

            inputs = [prompt, system, max_new_tokens, greedy]
            sub_event = submit.click(fn=self.process_gradio_instruct, inputs=inputs, outputs=[prompt, pred])

            def clear_():
                return ''

            clear.click(fn=clear_, outputs=[pred])
            txt_event = prompt.submit(fn=self.process_gradio_instruct, inputs=inputs, outputs=[prompt, pred])

            stop.click(fn=None, inputs=None, outputs=None, cancels=[txt_event, sub_event])

        block.queue()
        return block

    def fire(self):
        def run():
            uvicorn.run(self.app, host=self.config.host, port=self.config.port)

        self.process_uvicorn = mp.Process(target=run)
        self.process_uvicorn.start()

    def end(self):
        if self.process_uvicorn is not None:
            self.process_uvicorn.join()
        else:
            logging.warning('you have to fire server before ending that this command will be ignored')
