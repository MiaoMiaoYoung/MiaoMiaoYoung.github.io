---
title: "PRML-Introduction"
date: 2021-06-18T15:01:38+08:00
draft: false
categories:
    - work
    - mathematics
    - machine learning

tags:
    - math
    - PRML
    - machine learning

libraries:
    - katex

enableTocContent: true
---




## 前沿

2021.06.18 开始从头攻克PRML


## 1.2 概率论

### 联合概率、边缘概率和条件概率

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

### 1.2.1 概率密度 (Probability densities)

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

对于多个连续型变量$x_{1},\cdots,x_{D}$，组成的向量$\mathbf{x}$

定义联合概率密度$p(\mathrm{x})=p\left(x_{1}, \ldots, x_{D}\right)$

多元概率密度必须满足

$$\begin{array}{r} p(\mathbf{x}) \geqslant 0 \\\\ \\\\ \int p(\mathbf{x}) \mathrm{d} \mathbf{x}=1\end{array}$$

> 如果$\mathbf{x}$是一个离散变量，那么$p(\mathbf{x})$有时成为概率质量函数(probability mass function)；
> 
> 因为他被视为一组集中在$\mathbf{x}$上的概率质量

对于概率密度来说，求和、乘法法则、贝叶斯同样适用于**概率密度**

$$ \begin{aligned} p(x) &=\int p(x, y) \mathrm{d} y \\\\ p(x, y) &=p(y \mid x) p(x) \end{aligned} $$


### 1.2.2 期望(Expectations)和协方差(Covariances)

对于函数$f(x)$，在一个概率分配$p(x)$下的平均值成为期望(Expectations)，记为$\mathbb{E}[f]$

#### 离散型分布

$$\mathbb{E}[f]=\sum_{x} p(x) f(x)$$
平均值由不同$x$对应的概率进行加权


#### 连续性分布

$$\mathbb{E}[f]=\int p(x) f(x) \mathrm{d} x$$

如果从概率分布或者概率密度中取出有限数量的N个点，那么期望可以近似为:

$$\mathbb{E}[f] \simeq \frac{1}{N} \sum_{n=1}^{N} f\left(x_{n}\right)$$

这个结果在采样方法中特别有用，采样当中一般会$N\rightarrow \infty$

#### 多元期望

有时会考虑多变量函数的期望，但是在这个期望的计算过程中，**需要指明是根据哪个变量的分布进行的平均**，使用下标来进行指明

$$\mathbb{E}_{x}[f(x, y)]$$

表示函数$f(x,y)$相对于$x$分布的相对值，最后的结果是关于$y$的一个函数

#### 条件期望(conditional expectation)

对于一个条件分布，同样有相对应的条件期望

$$\mathbb{E}_{x} [f \mid y]=\sum\_{x} p(x \mid y) $$


---------------------------------

下面讨论方差和协方差，$f(x)$的**方差**定义为：

$$\operatorname{var}[f]=\mathbb{E}\left[(f(x)-\mathbb{E}[f(x)])^{2}\right]$$

它更多评价$f(x)$围绕它均值的变化程度，一般在计算中写成$f(x)$和$f(x)^{2}$的期望形式方便计算：

$$\operatorname{var}[f]=\mathbb{E}\left[f(x)^{2}\right]-\mathbb{E}[f(x)]^{2}$$

特别的，对于随机变量$x$，他的方差是:

$$\operatorname{var}[x]=\mathbb{E}\left[x^{2}\right]-\mathbb{E}[x]^{2}$$

对于两个随机变量$x$和$y$，他们的**协方差(covariance)的**定义为：

$$ \begin{aligned}  \operatorname{cov}[x, y]  &=\mathbb{E}_{x, y}[\{x-\mathbb{E}[x]\}\{y-\mathbb{E}[y]\}] \\\\ &=\mathbb{E}\_{x, y}[x y]-\mathbb{E}[x] \mathbb{E}[y] \end{aligned}  $$

表达了$x$和$y$一起变换的程度

对于两个由随机变量组成的向量$\mathbf{x}$和$\mathbf{y}$，他们的协方差以矩阵形式给出：


$$ \begin{aligned} \operatorname{cov}[\mathrm{x}, \mathbf{y}] &=\mathbb{E}_{\mathbf{x}, \mathbf{y}} \left[\\{\mathbf{x}-\mathbb{E}[\mathbf{x}]\\}\left\\{\mathbf{y}^{\mathrm{T}}-\mathbb{E}\left[\mathbf{y}^{\mathrm{T}}\right]\right\\}\right] \\\\ &=\mathbb{E}\_{\mathbf{x}, \mathbf{y}}\left[\mathrm{xy}^{\mathrm{T}}\right]-\mathbb{E}[\mathrm{x}] \mathbb{E}\left[\mathbf{y}^{\mathrm{T}}\right] \end{aligned} $$


### 1.2.3 贝叶斯概率 (Bayesoan probabilities)

> 上面概率解释偏向经典的频率派(frequentist)解释，下面开始转换到贝叶斯的视角：概率其实提供了一种不确定性的量化
> 
> Now we turn to the more general Bayesian view, in which probabilities provide a quantification of uncertainty.



