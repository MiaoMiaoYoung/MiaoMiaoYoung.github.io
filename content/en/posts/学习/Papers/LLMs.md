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


## OpenCLIP


