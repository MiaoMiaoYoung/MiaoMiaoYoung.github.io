---
title: "Large Language Model"
date: 2023-05-19T15:01:38+08:00
draft: false
categories:
    - 学习
    - work
    - paper
    - LLMs

libraries:
- katex

enableTocContent: true
---

## CODE

### load in 4/8 bit

当模型太大的时候，很难加载到普通显卡中，可以使用4/8 bit模型来进行训练

- https://huggingface.co/docs/transformers/main_classes/quantization


```python
# pip install transformers accelerate bitsandbytes
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "bigscience/bloom-1b7"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", load_in_4bit=True)
```

## inference in multi-GPU

- https://huggingface.co/docs/accelerate/main/en/usage_guides/big_modeling#designing-a-device-map

- 建议使用infer_auto_device_map

```python
import torch
from accelerate import init_empty_weights, load_checkpoint_and_dispatch

with init_empty_weights():
    model = MyModel(...)

model = load_checkpoint_and_dispatch(
    model, checkpoint=checkpoint_file, device_map="auto"
)

input = torch.randn(2,3)
input = input.to("cuda")
output = model(input)
```


---------------------------------------------------------------------



```python
from transformers import LlamaConfig,LlamaForCausalLM,LlamaTokenizer
from accelerate import init_empty_weights,infer_auto_device_map,load_checkpoint_in_model,dispatch_model
import torch

cuda_list = '6,7'.split(',')
memory = '35GiB'
model_path = 'xxx'
no_split_module_classes = LlamaForCausalLM._no_split_modules

max_memory = {int(cuda):memory for cuda in cuda_list}
config = LlamaConfig.from_pretrained(model_path)
with init_empty_weights():
    model = LlamaForCausalLM._from_config(config, torch_dtype=torch.float16) #加载到meta设备中，不需要耗时，不需要消耗内存和显存

device_map = infer_auto_device_map(model, max_memory=max_memory,no_split_module_classes=no_split_module_classes) #自动划分每个层的设备
load_checkpoint_in_model(model,model_path,device_map=device_map) #加载权重
model = dispatch_model(model,device_map=device_map) #并分配到具体的设备上

tokenizer = LlamaTokenizer.from_pretrained(model_path)
torch.set_grad_enabled(False)
model.eval()
sents=['你是谁']
ids = tokenizer(sents,max_length=1800,padding=True,truncation=True,return_tensors="pt")
ids = ids.to(model.device) 
outputs = model.generate(**ids, do_sample=False)
```


## OpenCLIP


