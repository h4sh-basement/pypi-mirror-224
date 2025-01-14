# -*- coding: utf-8 -*-
# @Author  : ssbuild
# @Time    : 2023/5/29 9:49
import os
import re
from collections import OrderedDict
import torch
from torch import nn
from torch.nn.modules.module import _IncompatibleKeys
from transformers import PreTrainedModel, HfArgumentParser, AutoConfig
from ...data_helper import ModelArguments, TrainingArguments, DataArguments
from ...nlp.models.prompt import PromptLearningConfig, PromptModel,PromptArguments,get_prompt_model
from ...nlp.models.lora.v2 import LoraModel, LoraArguments,LoraConfig
from ...utils.save_checkpoint import save_checkpoint_to_hf_format

__all__ = [
    'ModelWeightMinMax',
    'ModelWeightMixin',
    'LoraModel',
    'LoraArguments',
    'LoraConfig',
    'AutoConfig',
    'PromptLearningConfig',
    'PromptModel',
    'PromptArguments',
    'get_prompt_model',
    'ModelArguments',
    'TrainingArguments',
    'DataArguments',
    'PreTrainedModel',
    'HfArgumentParser'
]


class ModelWeightMixin:
    lora_args = None
    prompt_args = None
    def save_pretrained_merge_lora(self,sft_weight_path: str,llm_weight_only = True,max_shard_size="10GB"):
        assert os.path.exists(os.path.dirname(sft_weight_path))
        assert self.lora_args is not None and self.lora_args.with_lora
        lora_model : LoraModel = self.backbone
        model: nn.Module = lora_model.merge_and_unload()

        if llm_weight_only:
            model.model.save_pretrained(sft_weight_path,max_shard_size=max_shard_size)
        else:
            #torch.save(model.model.state_dict(), sft_weight_path)
            save_checkpoint_to_hf_format(self,sft_weight_path,max_shard_size=max_shard_size)
        return model

    # def save_pretrained_merge_lora_and_restore(self, sft_weight_path: str):
    #     assert os.path.exists(os.path.dirname(sft_weight_path))
    #     assert self.lora_args is not None and self.lora_args.with_lora
    #     lora_model: LoraModel = self.backbone
    #     lora_model.merge_adapter()
    #     # 保存hf权重，可用infer.py推理
    #     #torch.save(lora_model.model.model.state_dict(), weight_path_file)
    #     lora_model.model.model.save_pretrained(sft_weight_path)
    #     lora_model.unmerge_adapter()

    def load_sft_weight(self, sft_weight_path: str, is_trainable=False, strict=False,adapter_name="default"):
        assert os.path.exists(sft_weight_path)
        if self.lora_args is not None and self.lora_args.with_lora:
            # 恢复权重
            self.backbone: LoraModel
            self.backbone.load_adapter(sft_weight_path, adapter_name=adapter_name, is_trainable=is_trainable, strict=strict)

        elif self.prompt_args is not None and self.prompt_args.with_prompt:
            # 恢复权重
            self.backbone: PromptModel
            self.backbone.load_adapter(sft_weight_path, adapter_name=adapter_name, is_trainable=is_trainable, strict=strict)
        else:
            weight_dict = torch.load(sft_weight_path)
            weights_dict_new = OrderedDict()
            valid_keys = ['module', 'state_dict']
            for k in valid_keys:
                if k in weight_dict:
                    weight_dict = weight_dict[k]
                    break
            pl_model_prefix = '_TransformerLightningModule__backbone'
            is_pl_weight = pl_model_prefix in ','.join(list(weight_dict.keys()))
            base_model_prefix = self.backbone.base_model_prefix
            model_prefix = r'{}\.{}'.format(pl_model_prefix, base_model_prefix)
            for k, v in weight_dict.items():
                if is_pl_weight:
                    k = re.sub(r'_forward_module\.', '', k)
                    #llm module
                    if k.startswith(model_prefix):
                        k = re.sub(r'{}\.'.format(model_prefix), '', k)
                        k = model_prefix + '.' + k
                    #TransformerBase module
                    if not k.startswith(pl_model_prefix):
                        k = pl_model_prefix + '.' + k
                else:
                    # hf module weight
                    k = model_prefix + '.' + k
                weights_dict_new[k] = v
            # 加载sft 或者 p-tuning-v2权重
            def assert_state_dict_fn(model,incompatible_keys: _IncompatibleKeys):
                if not incompatible_keys.missing_keys and not incompatible_keys.unexpected_keys:
                    return None
                _keys_to_ignore_on_load_missing = getattr(model.backbone.model,"_keys_to_ignore_on_load_missing",[])
                missing_keys = [_ for _ in incompatible_keys.missing_keys]
                model_prefix = r'{}\.{}\.'.format(pl_model_prefix, base_model_prefix)
                missing_keys = [re.sub(r'{}'.format(model_prefix), '', _) for _ in missing_keys]
                missing_keys = [re.sub(r'{}'.format(pl_model_prefix), '', _) for _ in missing_keys]
                if missing_keys and _keys_to_ignore_on_load_missing:
                    __ = []
                    for _ in _keys_to_ignore_on_load_missing:
                        for missing_key in missing_keys:
                            if re.match(re.compile(_),missing_key):
                                __.append(missing_key)
                    for _ in __:
                        missing_keys.remove(_)

                if missing_keys:
                    if strict:
                        raise ValueError('Error in load_sft_weight missing_keys',missing_keys)
                    else:
                        print('Error in load_sft_weight missing_keys',missing_keys)
                if incompatible_keys.unexpected_keys:
                    if strict:
                        raise ValueError('Error in load_sft_weight unexpected_keys', incompatible_keys.unexpected_keys)
                    else:
                        print(('Error in load_sft_weight unexpected_keys', incompatible_keys.unexpected_keys))

                if not missing_keys and not incompatible_keys.unexpected_keys:
                    return None
                return missing_keys or incompatible_keys.unexpected_keys
            self: nn.Module
            h = self.register_load_state_dict_post_hook(assert_state_dict_fn)
            # TransformerBase类 可能有自定义额外模块
            self.load_state_dict(weights_dict_new, strict=strict)
            h.remove()



    #保存模型权重，除了llm之外可能还有其他模块
    def save_sft_weight(self, sft_weight_path,
                        merge_lora_weight=False,
                        llm_weight_only = True,
                        max_shard_size="10GB"):
        if self.lora_args is not None and self.lora_args.with_lora:
            if merge_lora_weight:
                # lora 合并权重 转换 hf权重
                self.save_pretrained_merge_lora(sft_weight_path,
                                                llm_weight_only=llm_weight_only,
                                                max_shard_size=max_shard_size)
            else:
                # 只保存 lora 权重
                self.backbone.save_pretrained(sft_weight_path)
        elif self.prompt_args is not None and self.prompt_args.with_prompt:
            self.backbone.save_pretrained(sft_weight_path)
        else:
            # 保存hf权重
            config = self.get_llm_model().config
            config.save_pretrained(os.path.dirname(sft_weight_path))
            #torch.save(self.state_dict(),sft_weight_path)
            if llm_weight_only:
                self.get_llm_model().save_pretrained(sft_weight_path, max_shard_size=max_shard_size)
            else:
                save_checkpoint_to_hf_format(self, sft_weight_path, max_shard_size=max_shard_size)


    #只保存llm hf 权重
    def save_llm_sft_weight(self, sft_weight_path, merge_lora_weight=False,
                            llm_weight_only = True,
                            max_shard_size="10GB"):
        self.save_sft_weight(sft_weight_path,
                             merge_lora_weight=merge_lora_weight,
                             llm_weight_only=llm_weight_only,
                             max_shard_size=max_shard_size)


ModelWeightMinMax = ModelWeightMixin