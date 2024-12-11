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

## Base

### LLM Auto-regressive Decoding

> https://blog.csdn.net/qq_47564006/article/details/135750787

自回归解码

在自然语言处理(NLP)中，大型语言模型(LLM)如Transformer进行推理时，自回归解码是一种生成文本的方式。在自回归解码中，模型在生成下一个单词时会依赖于它之前生成的单词。

使用自回归解码的公式可以表示为以下步骤:

初始化序列:设$(x_1,x_2,…, x_{t-1})$是目前已生成的单词序列。

计算下一个单词的概率分布:使用语言模型计算在给定上下文之后下一个单词的概率分布:

$$P(x_{t} | x_1,x_2, ... , x_{t-1})$$

这一步骤通常使用softmax函数完成，它将单词的logit转换成概率分布。

选择下一个单词:根据概率分布选择下一个单词$x_t$。这可以通过不同的策略来完成，如:

贪婪解码(Greedy Decoding):选择具有最高概率的单词。$x_t= \argmax P(x_{t} | x_1,x_2, ... , x_{t-1})$

随机抽样(Sampling): 根据概率分布随机选择单词，这允许生成更多样化的文本。

束搜索(Beam Search): 维护一个宽度为(k)的束(beam)，在每一步选择概率最高的(k)个单词组合作为候选，然后在这些候选中选择最终的单词序列。

更新序列:将选定的单词($x_t$)添加到序列中。

重复上述步骤，直到遇到序列结束标记，或者生成了所需长度的文本

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

### inference in multi-GPU

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


### Errors

#### piece id is out of range.

```bash
  File "/scratch/eyu/code/datagen/caption.py", line 93, in <module>
    predicts = model.generate({ "image": image.cuda(), "prompt": prompt})
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/data/eyu/workspace/LAVIS/lavis/models/blip2_models/blip2_vicuna_instruct.py", line 386, in generate
    output_text = self.llm_tokenizer.batch_decode(outputs, skip_special_tokens=True)
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/tokenization_utils_base.py", line 3469, in batch_decode
    return [
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/tokenization_utils_base.py", line 3470, in <listcomp>
    self.decode(
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/tokenization_utils_base.py", line 3509, in decode
    return self._decode(
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/tokenization_utils.py", line 931, in _decode
    filtered_tokens = self.convert_ids_to_tokens(token_ids, skip_special_tokens=skip_special_tokens)
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/tokenization_utils.py", line 912, in convert_ids_to_tokens
    tokens.append(self._convert_id_to_token(index))
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/models/llama/tokenization_llama.py", line 129, in _convert_id_to_token
    token = self.sp_model.IdToPiece(index)
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/sentencepiece/__init__.py", line 1179, in _batched_func
    return _func(self, arg)
  File "/anaconda3/envs/cdd/lib/python3.8/site-packages/sentencepiece/__init__.py", line 1172, in _func
    raise IndexError('piece id is out of range.')
IndexError: piece id is out of range.

```

```python
## /anaconda3/envs/cdd/lib/python3.8/site-packages/transformers/models/llama/tokenization_llama.py
def _convert_id_to_token(self, index):
    """Converts an index (integer) in a token (str) using the vocab."""
    
    token = self.sp_model.IdToPiece(index)
    return token
```


```python
def _convert_id_to_token(self, index):
    """Converts an index (integer) in a token (str) using the vocab."""
    if index >= self.sp_model.vocab_size():
        return ""
    
    if index < 0:
        return ""

    token = self.sp_model.IdToPiece(index)
    return token
```


## OpenCLIP

## Bert

> https://towardsdatascience.com/how-to-use-bert-from-the-hugging-face-transformer-library-d373a22b0209

In this article, I will demonstrate how to use BERT using the Hugging Face Transformer library for four important tasks. I will also show you how you can configure BERT for any task that you may want to use it for, besides just the standard tasks that it was designed to solve.

Note that this article was written in January 2021, so earlier/future versions of the Hugging Face library may be a little different and the code in this article may not necessarily work.

### A quick review of the architecture of BERT

BERT is a bidirectional transformer pre-trained using a combination of masked language modeling and next sentence prediction. The core part of BERT is the stacked bidirectional encoders from the transformer model, but during pre-training, a masked language modeling and next sentence prediction head are added onto BERT. When I say “head”, I mean that a few extra layers are added onto BERT that can be used to generate a specific output. The raw output of BERT is the output from the stacked Bi-directional encoders. This fact is especially important as it allows you to essentially do anything with BERT, and you will see examples of this later on in the article.

There are many tasks that BERT can solve that hugging face provides, but the ones that I will be going over in this article are Masked Language Modeling, Next Sentence Prediction, Language Modeling, and Question Answering. I will also demonstrate how to configure BERT to do any task that you want besides the ones stated above and that hugging face provides.

Before I discuss those tasks, I will describe how to use the BERT Tokenizer.

### BERT Tokenizer

The BERT Tokenizer is a tokenizer that works with BERT. It has many functionalities for any type of tokenization tasks. You can download the tokenizer using this line of code:

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
```

Unlike the BERT Models, you don’t have to download a different tokenizer for each different type of model. You can use the same tokenizer for all of the various BERT models that hugging face provides.

Given a text input, here is how I generally tokenize it in projects:

```python
encoding = tokenizer.encode_plus(text, add_special_tokens = True,    truncation = True, padding = "max_length", return_attention_mask = True, return_tensors = "pt")
```

As BERT can only accept/take as input only 512 tokens at a time, we must specify the truncation parameter to True. The add special tokens parameter is just for BERT to add tokens like the start, end, [SEP], and [CLS] tokens. Return_tensors = “pt” is just for the tokenizer to return PyTorch tensors. If you don’t want this to happen(maybe you want it to return a list), then you can remove the parameter and it will return lists.

In the code below, you will see me not adding all the parameters I listed above and this is primarily because this is not necessary as I am not tokenizing text for a real project. In a real machine learning/NLP project, you will want to add these parameters, especially the truncation and padding as we have to do this for each batch in the dataset in a real project.

tokenizer.encode_plus() specifically returns a dictionary of values instead of just a list of values. Because tokenizer.encode_plus() can return many different types of information, like the attention_masks and token type ids, everything is returned in a dictionary format, and if you want to retrieve the specific parts of the encoding, you can do it like this:

```python
input = encoding["input_ids"][0]
attention_mask = encoding["attention_mask"][0]
```

Additionally, because the tokenizer returns a dictionary of different values, instead of finding those values as shown above and individually passing these into the model, we can just pass in the entire encoding like this

```python
output = model(**encoding) 
```

One more very important thing about the tokenizer to know is that you can specify to retrieve specific tokens if desired. For example, if you are doing masked language modeling and you want to insert a mask at a location for your model to decode, then you can simply retrieve the mask token like this

```python
mask_token = tokenizer.mask_token
```

and you can simply insert it into your input by concatenating it with your input text.

You can also retrieve many other tokens, like the [SEP] token, in the same way.

I typically use the tokenizer.encode_plus() function to tokenize my input, but there is another function that can be used to tokenize input, and this tokenizer.encode(). Here is an example of this:

```python
encoding = tokenizer.encode(text, return_tensors = "pt")
```

The main difference between tokenizer.encode_plus() and tokenizer.encode() is that tokenizer.encode_plus() returns more information. Specifically, it returns the actual input ids, the attention masks, and the token type ids, and it returns all of these in a dictionary. tokenizer.encode() only returns the input ids, and it returns this either as a list or a tensor depending on the parameter, return_tensors = “pt”.

### Masked Language Modeling

Masked Language Modeling is the task of decoding a masked token in a sentence. In simple terms, it is the task of filling in the blanks.

Instead of just getting the best candidate word to replace the mask token, I will demonstrate how you can take the top 10 replacement words for the mask token, and here is how you can do this:

```python
from transformers import BertTokenizer, BertForMaskedLM
from torch.nn import functional as F
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased',    return_dict = True)

text = "The capital of France, " + tokenizer.mask_token + ", contains the Eiffel Tower."
input = tokenizer.encode_plus(text, return_tensors = "pt")
mask_index = torch.where(input["input_ids"][0] == tokenizer.mask_token_id)
output = model(**input)
logits = output.logits
softmax = F.softmax(logits, dim = -1)
mask_word = softmax[0, mask_index, :]
top_10 = torch.topk(mask_word, 10, dim = 1)[1][0]
for token in top_10:
   word = tokenizer.decode([token])
   new_sentence = text.replace(tokenizer.mask_token, word)
   print(new_sentence)
```

Hugging Face is set up such that for the tasks that it has pre-trained models for, you have to download/import that specific model. In this case, we have to download the Bert For Masked Language Modeling model, whereas the tokenizer is the same for all different models as I said in the section above.

Masked Language Modeling works by inserting a mask token at the desired position where you want to predict the best candidate word that would go in that position. You can simply insert the mask token by concatenating it at the desired position in your input like I did above. The Bert Model for Masked Language Modeling predicts the best word/token in its vocabulary that would replace that word. The logits are the output of the BERT Model before a softmax activation function is applied to the output of BERT. In order to get the logits, we have to specify return_dict = True in the parameters when initializing the model, otherwise, the above code will result in a compilation error. After we pass the input encoding into the BERT Model, we can get the logits simply by specifying output.logits, which returns a tensor, and after this we can finally apply a softmax activation function to the logits. By applying a softmax onto the output of BERT, we get probabilistic distributions for each of the words in BERT’s vocabulary. Word’s with a higher probability value will be better candidate replacement words for the mask token. In order to get the tensor of softmax values of all the words in BERT’s vocabulary for replacing the mask token, we can specify the masked token index, which we get using torch.where(). Because in this particular example I am retrieving the top 10 candidate replacement words for the mask token(you can get more than 10 by adjusting the parameter accordingly), I used the torch.topk() function, which allows you to retrieve the top k values in a given tensor, and it returns a tensor containing those top k values. After this, the process becomes relatively simple, as all we have to do is iterate through the tensor, and replace the mask token in the sentence with the candidate token. Here is the output the code above compiles:

```
The capital of France, paris, contains the Eiffel Tower. 
The capital of France, lyon, contains the Eiffel Tower. 
The capital of France, lille, contains the Eiffel Tower. 
The capital of France, toulouse, contains the Eiffel Tower. 
The capital of France, marseille, contains the Eiffel Tower. 
The capital of France, orleans, contains the Eiffel Tower. 
The capital of France, strasbourg, contains the Eiffel Tower. 
The capital of France, nice, contains the Eiffel Tower. 
The capital of France, cannes, contains the Eiffel Tower. 
The capital of France, versailles, contains the Eiffel Tower.
```

and you can see that Paris is indeed the top candidate replacement word for the mask token.

If you want to only get the top candidate word, you can do this:

```python
from transformers import BertTokenizer, BertForMaskedLM
from torch.nn import functional as F
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased',    return_dict = True)

text = "The capital of France, " + tokenizer.mask_token + ", contains the Eiffel Tower."
input = tokenizer.encode_plus(text, return_tensors = "pt")

mask_index = torch.where(input["input_ids"][0] == tokenizer.mask_token_id)

logits = model(**input)
logits = logits.logits

softmax = F.softmax(logits, dim = -1)
mask_word = softmax[0, mask_index, :]
top_word = torch.argmax(mask_word, dim=1)

print(tokenizer.decode(top_word))
```

Instead of using torch.topk() for retrieving the top 10 values, we just use torch.argmax(), which returns the index of the maximum value in the tensor. The rest of the code is pretty much the same thing as the original code.

### Language Modeling

Language Modeling is the task of predicting the best word to follow or continue a sentence given all the words already in the sentence.

```python
import transformers
from transformers import BertTokenizer, BertLMHeadModel
import torch
from torch.nn import functional as F

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertLMHeadModel.from_pretrained('bert-base-uncased', return_dict=True, is_decoder = True)

text = "A knife is very "
input = tokenizer.encode_plus(text, return_tensors = "pt")
output = model(**input).logits[:, -1, :]
softmax = F.softmax(output, -1)
index = torch.argmax(softmax, dim = -1)
x = tokenizer.decode(index)
print(x)
```

Language Modeling works very similarly to Masked language modeling. To start off, we have to download the specific Bert Language Model Head Model, which is essentially a BERT model with a language modeling head on top of it. One additional parameter we have to specify while instantiating this model is the is_decoder = True parameter. We have to specify this parameter if we want to use this model as a standalone model for predicting the next best word in the sequence. The rest of the code is relatively the same as the one in masked language modeling: we have to retrieve the logits of the model, but instead of specifying the index to be that of the masked token, we just have to take the logits of the last hidden state of the model(using -1 index), compute the softmax of these logits, find the largest probability value in the vocabulary, and decode and print this token.

### Next Sentence Prediction

Next Sentence Prediction is the task of predicting whether one sentence follows another sentence. Here is my code for this:

```python
from transformers import BertTokenizer, BertForNextSentencePrediction
import torch
from torch.nn import functional as F

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')

prompt = "The child came home from school."
next_sentence = "He played soccer after school."

encoding = tokenizer.encode_plus(prompt, next_sentence, return_tensors='pt')
outputs = model(**encoding)[0]
softmax = F.softmax(outputs, dim = 1)

print(softmax)
```

Next Sentence prediction is the task of predicting how good a sentence is a next sentence for a given sentence. In this case, “The child came home from school.” is the given sentence and we are trying to predict whether “He played soccer after school.” is the next sentence. To do this, the BERT tokenizer automatically inserts a [SEP] token in between the sentences, which represents the separation between the two sentences, and the specific Bert For Next Sentence Prediction model predicts two values of whether the sentence is the next sentence. Bert returns two values in a tensor: the first value represents whether the second sentence is a continuation of the first, and the second value represents whether the second sentence is a random sequence or not a good continuation of the first. Unlike Language Modeling, we don’t retrieve any logits because we are not trying to compute a softmax on the vocabulary of BERT; we are simply trying to compute a softmax on the two values that BERT for next sentence prediction returns so that we can see which value has the highest probability value, and this will represent whether the second sentence is a good next sentence for the first. Once we get the softmax values, we can simply look at the tensor by printing it out. Here are the values that I got:

tensor([[0.9953, 0.0047]])
Because the first value is considerably higher than the second index, BERT believes that the second sentence follows the first sentence, which is the correct answer.

### Extractive Question Answering

Extractive Question Answering is the task of answering a question given some context text by outputting the start and end indexes of where the answer lies in the context. Here is my code for extractive question answering:

```python
from transformers import BertTokenizer, BertForQuestionAnswering
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

question = "What is the capital of France?"
text = "The capital of France is Paris."

inputs = tokenizer.encode_plus(question, text, return_tensors='pt')
start, end = model(**inputs)
start_max = torch.argmax(F.softmax(start, dim = -1))
end_max = torch.argmax(F.softmax(end, dim = -1)) + 1 ## add one ##because of python list indexing
answer = tokenizer.decode(inputs["input_ids"][0][start_max : end_max])
print(answer)
```

Similar to the other three tasks, we begin by downloading the specific BERT model for Question Answering, and we tokenize our two inputs: the question and the context. Unlike the other models, the process is relatively straightforward for this model as it outputs the values for each word in the tokenized input. As I mentioned before, the way extractive question answering works is by computing the best start and end indexes for where the answer is located in the context. The model returns values for all of the words in context/input corresponding to how good they would be a start value and end value for the given question; in other words, each of the words in the input receives a start and end index score/value representing whether they would be a good start word for the answer or a good end word for the answer. The rest of this process is fairly similar to what we did on the other three programs; we compute the softmax of these scores to find the probabilistic distribution of values, retrieve the highest values for both the start and end tensors using torch.argmax(), and find the actual tokens that correspond to this start : end range in the input and decode them and print them out.

### Using BERT for any task you want

Although Text Summarization, Question answering, and a basic Language Model are especially important, often, people want to use BERT for other unspecified tasks, especially in research. The way that they do this is by taking the raw outputs of the stacked encoders of BERT, and attaching their own specific model to it, most commonly a linear layer, and then fine-tuning this model on their specific dataset. When doing this in Pytorch using the Hugging Face transformer library, it is best to set this up as a Pytorch deep learning model like such:

```python
from transformers import BertModel
class Bert_Model(nn.Module):
   def __init__(self, class):
       super(Bert_Model, self).__init__()
       self.bert = BertModel.from_pretrained('bert-base-uncased')
       self.out = nn.Linear(self.bert.config.hidden_size, classes)
   def forward(self, input):
       _, output = self.bert(**input)
       out = self.out(output)
       return out
```

As you can see, instead of downloading a specific BERT Model already designed for a specific task like Question Answering, I downloaded the raw pre-trained BertModel, which does not come with any heads attached to it.

To get the size of the raw BERT outputs, simply use self.bert.config.hidden_size, and attach this to the number of classes you want your linear layer to output.

To use the code above for sentiment analysis, which is surprisingly a task that does not come downloaded/already done in the hugging face transformer library, you can simply add a sigmoid activation function onto the end of the linear layer and specify the classes to equal 1.

```python
from transformers import BertModel
class Bert_Model(nn.Module):
   def __init__(self, class):
       super(Bert_Model, self).__init__()
       self.bert = BertModel.from_pretrained('bert-base-uncased')
       self.out = nn.Linear(self.bert.config.hidden_size, classes)
       self.sigmoid = nn.Sigmoid()
   def forward(self, input, attention_mask):
       _, output = self.bert(input, attention_mask = attention_mask)
       out = self.sigmoid(self.out(output))
       return out
```

I hope that you found this content easy to understand. If you think that I need to elaborate further or clarify anything, drop a comment below.


## LLavA

> https://zhuanlan.zhihu.com/p/690771106
>
> https://zhuanlan.zhihu.com/p/698218006

### 配置环境

检查环境是否配好



```python
# inference.py
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'


from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path
from llava.eval.run_llava import eval_model

# llava-1.5预训练权重
model_path = "/model/llava-v1.5-13b"

tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path),
    load_4bit=True
)

# 文本提示
prompt = "what does this image describe?"
# 测试图片路径
image_file = "n02509815_6586.JPEG"
 
args = type('Args', (), {
    "model_path": model_path,
    "model_base": None,
    "model_name": get_model_name_from_path(model_path),
    "query": prompt,
    "conv_mode": None,
    "image_file": image_file,
    "sep": ",",
    "temperature": 0,
    "top_p": None,
    "num_beams": 1,
    "max_new_tokens": 512
})()

eval_model(args)

# The image features a small red panda sitting on a tree branch, surrounded by leaves. The panda appears to be looking at something, possibly observing its surroundings or focusing on a specific object. The scene captures the panda's natural habitat and behavior, as they are known to climb trees for safety and to search for food.
```


### 训练

```bash
# --num_train_epochs 1 \
# --save_strategy "steps" \
# --save_steps 24000 \
# --save_total_limit 1 \
# --report_to wandb
# 改成
--num_train_epochs 20 \
--save_strategy "epoch" \
--save_total_limit 10 \
--report_to tensorboard
```

- CUDA Out-of-Memory (OOM)

  在script添加参数 --bit 4/8，但是同时会报错

  > ValueError: You cannot perform fine-tuning on purely quantized models. Please attach trainable adapters on top of the quantized model to correctly perform fine-tuning. Please see: https://huggingface.co/docs/transformers/peft for more details

  可以配合lora使用

  如果不想使用lora，那么可以把模型换成vicuna-7b或者vit-base的，让模型更小点



- lora finetune

  merge_lora_weights.py

  > ValueError: The generation config instance is invalid

  此错误似乎是升级变压器版本时发生的问题。我通过在vicuna的generation_config.json文件中手动添加do_sample：true来解决此问题。

  https://github.com/haotian-liu/LLaVA/issues/1144


## Blip

