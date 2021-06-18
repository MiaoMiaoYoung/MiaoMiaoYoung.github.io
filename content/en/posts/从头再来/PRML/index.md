---
title: "PRML"
date: 2021-06-18T15:01:38+08:00
draft: false
categories:
    - work
    - mathematics
    - matrix
tags:
    - math
    - Linear Algebra
libraries:
    - katex
---

- [前沿](#前沿)
- [1. Introduction](#1-introduction)
  - [1.2 概率论](#12-概率论)
    - [联合概率、边缘概率和条件概率](#联合概率边缘概率和条件概率)
    - [1.2.1 概率密度 (Probability densities)](#121-概率密度-probability-densities)

## 前沿

2021.06.18 开始从头攻克PRML

## 1. Introduction

### 1.2 概率论

#### 联合概率、边缘概率和条件概率

对于两个随机变量$X$和$Y$

$X$可以取值：$x_{i}$，其中$i=1,\cdots,M$；同理，$Y$可以取值：$y_{j}$，其中$j=1，,\cdots, L$

考虑一个$N$次实验

令得到$X=x_{i}$且$Y=y_{j}$的结果实验次数为$n_{ij}$

令得到$X=x_{i}$结果的实验次数为$c_{i}$

令得到$Y=y_{j}$的结果的试验次数为$r_{j}$

**联合概率(joint probability)**

那么$X=x_{i}$且$Y=y_{j}$的联合概率是$p\left(X=x_{i}, Y=y_{j}\right)=\frac{n_{i j}}{N}$

**边缘概率(marginal probability)**

$X=x_{i}$边缘概率是$p\left(X=x_{i}\right)=\frac{c_{i}}{N}=\sum_{j=1}^{L} p\left(X=x_{i}, Y=y_{j}\right)$

**条件概率(conditional probability)**

当给定$X=x_{i}$时，$Y=y_{j}$的条件概率是$p\left(Y=y_{j} \mid X=x_{i}\right)=\frac{n_{i j}}{c_{i}}$

----------------------

由上面的概率定义，可以得到下面两个法则：

**概率的求和法则**

$$p(X)=\sum_{Y} p(X, Y)$$

通过$p\left(X=x_{i}\right)=\sum_{j=1}^{L} p\left(X=x_{i}, Y=y_{j}\right)$得到

**概率的乘法法则**

$$p(X, Y)=p(Y \mid X) p(X)$$

由$p\left(X=x_{i}, Y=y_{j}\right)=\frac{n_{i j}}{N}=\frac{n_{i j}}{c_{i}} \cdot \frac{c_{i}}{N}=p\left(Y=y_{j} \mid X=x_{i}\right) p\left(X=x_{i}\right)$得到

----------------------

**联合概率满足对称性**

$$p(X, Y)=p(Y, X)$$

**贝叶斯公式**

$$p(Y \mid X)=\frac{p(X \mid Y) p(Y)}{p(X)}$$

可以使用求和法则将分母表达为下面的式子：

$$p(X)=\sum_{Y} p(X \mid Y) p(Y)$$

#### 1.2.1 概率密度 (Probability densities)

**概率密度**

对于落在$(x,x+\delta x)$区间的实值**连续变量**$x$，$p(x)\delta x, \delta x\rightarrow \infty$被称为$x$的概率密度

**连续型变量的概率表示**

$$p(x \in(a, b))=\int_{a}^{b} p(x) \mathrm{d} x$$

其中，满足一下两条性质

$$p(x) \geqslant 0$$

$$\int_{-\infty}^{\infty} p(x) \mathrm{d} x=1$$

**累计密度函数(cumulative distribution)**

$x$在$(-\infty, z)$上的概率，成为累计密度函数

$$P(z)=\int_{-\infty}^{z} p(x) \mathrm{d} x$$

**多个连续型变量**

p19