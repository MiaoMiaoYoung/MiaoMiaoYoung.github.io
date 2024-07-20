---
title: "Python是世界上最好的语言*不是*"
date: 2024-06-11T11:09:34+08:00
draft: false
image: images/posts/python.jpg
categories:
    - 教程
tags:
    - python
---

## 编程语言

- 机器语言

  - 计算机实际运算时得到的指令

    ```
    0000 0000 = 0
    0000 0001 = 1
    0000 0010 = 2
    0000 0011 = 3

    0000 0100 = 4
    0000 0101 = 5
    0000 0110 = 6
    0000 0111 = 7

    100 000 = add
    100 010 = sub
    ```

    bit -> 一位字节，一位0/1，最小的储存单位

- 汇编语言 = 机器语言

    汇编语言和机器语言实质是相同的，都是直接对硬件操作，只不过指令采用了英文缩写的标识符，容易识别和记忆。

    机器语言                       汇编语言
    100 000 0000 0011 0000 0100 -> ADD $3 $4


- 高级程序语言

    C/C++、Java、C#、Python、PHP、JavaScript、Go、Objective-C、Swift ……

    都是高级语言，方便人类编写

    但是不能直接被机器识别，需要**编译器**转换成机器语言才能让计算机执行


## 数据类型

都是用0/1bit来数据带来一个问题，怎么表示不同的数据，比如小数，整数、文字...

同时，不同数据类型下的操作符对应着不同的结果

python自动处理数据类型，但是有时候也会出现错位的情况，需要自己调整

int 整数
float 浮点数（也就是小数）
str 字符串 （文字类型）


```python
a = 1

## type: 得到a的数据类型
print(type(a))
# <class 'int'>
print(a)
# 1

print(type(float(a)))
# <class 'float'>
print(float(a))
# 1.0


print(type(str(a)))
# <class 'float'>
print(str(a))
# 1

print(a + a)
# 2
print(str(a) + str(a))
# 11
```


## 变量



## 逻辑语句


## 数据结构


## 函数

