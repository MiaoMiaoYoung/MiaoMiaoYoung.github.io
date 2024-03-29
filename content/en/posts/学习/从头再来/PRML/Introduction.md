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


## 1.2 概率论 (Probability Theory)

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

**当多元变量相互独立时**，期望服从线性性质：

$$\mathbb{E}[ax+by+cz] = a\mathbb{E}[x]+b\mathbb{E}[y]+c\mathbb{E}[z]$$

$$\mathbb{E}[x_{1}x_{2}\cdots x_{n}]=\mathbb{E}[x_{1}]\mathbb{E}[x_{2}]\cdots\mathbb{E}[x_{n}]$$

> 简要证明一下 (Exercise 1.10)
> $$ \begin{aligned} \mathbb{E}[x+z] &=\iint(x+z) p(x) p(z) \mathrm{d} x \mathrm{~d} z \\ &=\int x p(x) \mathrm{d} x+\int z p(z) \mathrm{d} z \\ &=\mathbb{E}[x]+\mathbb{E}[z] \end{aligned} $$
> 
> 因为独立才有$p(x, z)=p(x) p(z)$

#### 条件期望(conditional expectation)

对于一个条件分布，同样有相对应的条件期望

$$\mathbb{E}_{x} [f \mid y]=\sum\_{x} p(x \mid y) $$


#### 方差(variance)和协方差(covariance)

下面讨论方差和协方差，$f(x)$的**方差**定义为：

$$\operatorname{var}[f]=\mathbb{E}\left[(f(x)-\mathbb{E}[f(x)])^{2}\right]$$

它更多评价$f(x)$围绕它均值的变化程度，一般在计算中写成$f(x)$和$f(x)^{2}$的期望形式方便计算：

$$\operatorname{var}[f]=\mathbb{E}\left[f(x)^{2}\right]-\mathbb{E}[f(x)]^{2}$$

特别的，对于随机变量$x$，他的方差是:

$$\operatorname{var}[x]=\mathbb{E}\left[x^{2}\right]-\mathbb{E}[x]^{2}$$

当多变量相互独立是，方差服从性质：

$$\operatorname{var}[nx]=n^{2}\operatorname{var}[x]$$

$$\operatorname{var}[x_{1}x_{2}\cdots x_{n}]=\operatorname{var}[x_{1}]+\operatorname{var}[x_{2}]\cdots\operatorname{var}[x_{n}]$$

> 简要证明一下 (Exercise 1.10)
> $$ \begin{aligned} \operatorname{var}[x+z] &=\iint(x+z-\mathbb{E}[x+z])^{2} p(x) p(z) \mathrm{d} x \mathrm{~d} z \\ &=\int(x-\mathbb{E}[x])^{2} p(x) \mathrm{d} x+\int(z-\mathbb{E}[z])^{2} p(z) \mathrm{d} z \\ &=\operatorname{var}(x)+\operatorname{var}(z) \end{aligned} $$
> 
> 其中 $(x+z-\mathbb{E}[x+z])^{2}=(x-\mathbb{E}[x])^{2}+(z-\mathbb{E}[z])^{2}+2(x-\mathbb{E}[x])(z-\mathbb{E}[z])$，因为独立最后一项积分为0


对于两个随机变量$x$和$y$，他们的**协方差(covariance)的**定义为：

$$ \begin{aligned}  \operatorname{cov}[x, y]  &=\mathbb{E}_{x, y}[\{x-\mathbb{E}[x]\}\{y-\mathbb{E}[y]\}] \\\\ &=\mathbb{E}\_{x, y}[x y]-\mathbb{E}[x] \mathbb{E}[y] \end{aligned}  $$

表达了$x$和$y$ **一起变换** 的程度

对于两个由随机变量组成的向量$\mathbf{x}$和$\mathbf{y}$，他们的协方差以矩阵形式给出：


$$ \begin{aligned} \operatorname{cov}[\mathrm{x}, \mathbf{y}] &=\mathbb{E}_{\mathbf{x}, \mathbf{y}} \left[\\{\mathbf{x}-\mathbb{E}[\mathbf{x}]\\}\left\\{\mathbf{y}^{\mathrm{T}}-\mathbb{E}\left[\mathbf{y}^{\mathrm{T}}\right]\right\\}\right] \\\\ &=\mathbb{E}\_{\mathbf{x}, \mathbf{y}}\left[\mathrm{xy}^{\mathrm{T}}\right]-\mathbb{E}[\mathrm{x}] \mathbb{E}\left[\mathbf{y}^{\mathrm{T}}\right] \end{aligned} $$





### 1.2.3 贝叶斯概率 (Bayesoan probabilities)

> 上面概率解释偏向经典的频率派(frequentist)解释，下面开始转换到贝叶斯的视角：概率其实提供了一种不确定性的量化
> 
> Now we turn to the more general Bayesian view, in which probabilities provide a quantification of uncertainty.

> 贝叶斯派 Vs 频率派：
> 1. 频率学派的参数固定，数据根据固定参数随机产生；**贝叶斯学派认为参数也是一个随机变量，也有概率分布**。也就是说，贝叶斯学派才有$p(\mathbf{w})$ 这个东西
> 2. 频率学派没有先验概率，使用最大似然估计(maximum likelihood estimator,MLE)，容易过拟合，而贝叶斯学派可以使用最大后验估计(MAP)，可以一定程度上避免过拟合。严格来说MAP也不是纯贝叶斯的方法，真正的贝叶斯方法，需要算出参数的概率分布。
> 3. 频率学派的重点是优化问题，优化一个损失函数的目标；贝叶斯学派的重点是积分问题，后验概率中分母的那个积分（也叫配分函数）的计算。
真正的贝叶斯方法除了做MAP之外，一般有两步：1. 贝叶斯推断/估计 计算p(w|D)主要是一个积分问题 2.贝叶斯决策/预测，使用w预测新来的数据的概率
>
>转自：https://zhuanlan.zhihu.com/p/365934431



假设我们观察到的变量是$t_{n}$，我们对一些参数$\mathbf{w}$进行推断时，可以**在观察数据之前** ，以先验概率分布$p(\mathbf{w})$的形式来捕捉(capture)对$\mathbf{w}$的假设

$$p(\mathbf{w} \mid \mathcal{D})=\frac{p(\mathcal{D} \mid \mathbf{w}) p(\mathbf{w})}{p(\mathcal{D})}$$

**似然(likelihood)：** 贝叶斯右边的 $p(\mathcal{D} \mid \mathbf{w})$，因为他表达了在$\mathbf{w}$参数下，观察数据集$\mathcal{D}$的概率，可以认为是$\mathbf{w}$的一个函数。注意！似然不是$\mathbf{w}$上的概率分布，并且对于$\mathbf{w}$的积分不一定等于1

因此，贝叶斯公式可以表达为下述：

$$\text { posterior } \propto \text { likelihood } \times\text { prior }$$

$$p(\mathbf{w} \mid \mathcal{D}) \propto p(\mathcal{D} \mid \mathbf{w}) \times p(\mathbf{w})$$

$$\text { 后验 } \propto \text { 似然 } \times\text { 先验 }$$

> 这里其实主要描述的是对$\mathbf{w}$的不确定性的测量，先验、后验、似然都是针对$\mathbf{w}$来说的

贝叶斯公式中的分母 $p(\mathcal{D})$是为了概率进行归一化的，可以表达为下面的这种形式：

$$p(\mathcal{D})=\int p(\mathcal{D} \mid \mathbf{w}) p(\mathbf{w}) \mathrm{d} \mathbf{w}$$

-------------------------------------------------

**共轭先验：**

如果后验概率$p(\mathbf{w} \mid \mathcal{D})$和先验概率$p(\mathbf{w})$满足同样的分布律，那么先验分布和后验分布被称作共轭分布。先验分布叫做似然函数的共轭先验分布。

$$p(\mathbf{w} \mid \mathcal{D}) = \frac{p(\mathbf{w} , \mathcal{D})}{p(\mathcal{D})}$$

举个例子：

Beta分布是二项式分布的共轭先验分布。

Dirichlet分布是多项式分布的共轭分布。

常见的共轭分布可以在[wikipedia](https://en.wikipedia.org/wiki/Conjugate_prior)上查到

> 共轭的意思就是，以Beta分布和二项式分布为例，**数据**符合二项式分布时，**参数**的先验分布和后验分布都能保持Beta分布的形式
> 
> 这种能够在先验分布中赋予参数明确的物理意义，这个物理意义可以延续到后续分布中进行解释

### 1.2.4 高斯分布

#### 单实值变量高斯

单实值变量$x$的高斯分布定义为：

$$\mathcal{N}\left(x \mid \mu, \sigma^{2}\right)=\frac{1}{\left(2 \pi \sigma^{2}\right)^{1 / 2}} \exp \left\\{-\frac{1}{2 \sigma^{2}}(x-\mu)^{2}\right\\}$$

其中两个参数：$\mu$：均值；$\sigma^{2}$: 方差 

$\sigma$称为标准差，$\beta=\frac{1}{\sigma^{2}}$方差的倒数称为精度(precision)

可以看到高斯分布满足概率的条件：

$$\int_{-\infty}^{\infty} \mathcal{N}\left(x \mid \mu, \sigma^{2}\right) \mathrm{d} x=1$$

$$\mathcal{N}\left(x \mid \mu, \sigma^{2}\right)>0$$

高斯的均值：

$$\mathbb{E}[x]=\int_{-\infty}^{\infty} \mathcal{N}\left(x \mid \mu, \sigma^{2}\right) x \mathrm{~d} x=\mu$$

$$\mathbb{E}\left[x^{2}\right]=\int_{-\infty}^{\infty} \mathcal{N}\left(x \mid \mu, \sigma^{2}\right) x^{2} \mathrm{~d} x=\mu^{2}+\sigma^{2}$$

结合上式可得高斯的方差：

$$\operatorname{var}[x]=\mathbb{E}\left[x^{2}\right]-\mathbb{E}[x]^{2}=\sigma^{2}$$


#### 多元高斯

对于包含着连续变量的 $D$ 维向量 $\mathbf{x}$ ，高斯分布以如下形式给出：

$$\mathcal{N}(\mathrm{x} \mid \mu, \Sigma)=\frac{1}{(2 \pi)^{D / 2}} \frac{1}{|\Sigma|^{1 / 2}} \exp \left\\{-\frac{1}{2}(\mathrm{x}-\mu)^{\mathrm{T}} \Sigma^{-1}(\mathrm{x}-\mu)\right\\}$$

$\mathbf{\mu}$称为均值，$D\times D$的矩阵$\Sigma$称为协方差，$|\Sigma|$表示$\Sigma$的行列式

#### 单变量高斯的N次观察

现在，假设我们有一个观察到的数据集$\bm{x}=\left(x_{1}, \ldots, x_{N}\right)^{\mathrm{T}}$，表示对一个变量$x$的$N$次观察

> 注意，这里的$\bm{x}$和上面的多变量高斯中的$\mathbf{x}$不同，这里指的是对一个变量$x$(标量)的N次观察得到的数据集，多变量高斯中的$\mathbf{x}=\left(x_{1}, \ldots, x_{N}\right)^{\mathrm{D}}$ 指的是多个变量

我们假设观测值独立于均值为$\mu$，方差为$\sigma^{2}$的高斯，并且希望从这个数据集中确定高斯的参数

**独立同分布 (independent and identically distributed, i.i.d)**：从同一个分布中独立抽取的数据点

> Data points that are drawn independently from the same distribution are said to be independent and identically distributed, which is often abbreviated to i.i.d.

因为数据集是独立同分布的，所以他们的联合概率根据乘法法则就可以直接给出：

$$p\left(\bm{x} \mid \mu, \sigma^{2}\right)=\prod_{n=1}^{N} \mathcal{N}\left(x_{n} \mid \mu, \sigma^{2}\right)$$

> 这个时候，最重要的不是看数据点怎么样了，而是把$p\left(\bm{x} \mid \mu, \sigma^{2}\right)$看成是$\mu$和$\sigma$的函数，这也是贝叶斯派比较重要的一个观点，下面就是要怎么去求解这两个参数

![](./images/1.jpg)

书里面对于高斯的likelihood函数我觉得说的比较清楚，也就是在参数$\mu$，$\sigma$下，观察数据得到的概率，图中的公式(1.53)也就是上面的公式$p\left(\bm{x} \mid \mu, \sigma^{2}\right)$。

#### 求解最大似然(MAP)

所以，最大似然其实就是在求解 $\max{p\left(\bm{x} \mid \mu, \sigma^{2}\right)}$，非常容易理解

因为高斯的形式当中有求积，所以取对数变成求和

$$\ln p\left(\bm{x} \mid \mu, \sigma^{2}\right)=-\frac{1}{2 \sigma^{2}} \sum_{n=1}^{N}\left(x_{n}-\mu\right)^{2}-\frac{N}{2} \ln \sigma^{2}-\frac{N}{2} \ln (2 \pi)$$

所以 $\max{\ln p\left(\bm{x} \mid \mu, \sigma^{2}\right)}$

$$\mu_{\mathrm{ML}}=\frac{1}{N} \sum_{n=1}^{N} x_{n}$$

$$\sigma_{\mathrm{ML}}^{2}=\frac{1}{N} \sum_{n=1}^{N}\left(x_{n}-\mu_{\mathrm{ML}}\right)^{2}$$

得到的 $\mu_{\mathrm{ML}}$ 和 $\sigma_{\mathrm{ML}}^{2}$ 被称作采样均值 (sample mean) 和 采样方差 (sample variance)。并且这个是有偏估计，可以通过计算$\mathbb{E}[\mu_{ML}]$和$\mathbb{E}[\sigma_{ML}^{2}]$得到

$$\mathbb{E}\left[\mu_{\mathrm{ML}}\right]=\mu$$

$$\mathbb{E}\left[\sigma_{\mathrm{ML}}^{2}\right]=\left(\frac{N-1}{N}\right) \sigma^{2}$$

> 这里需要推导一下，首先是$\mathbb{E}\left[\mu_{\mathrm{ML}}\right]$是无偏的：
> 
> $$\mathbb{E}\left[\mu_{\mathrm{ML}}\right] =\mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N} x_{n}\right] =\frac{1}{N} \sum_{n=1}^{N} \mathbb{E}\left[ x_{n}\right] = \mu$$
>  
> 其次，$\mathbb{E}\left[\sigma_{\mathrm{ML}}^{2}\right]$是有偏的
> 
> $$ \begin{aligned}     \mathbb{E}\left[\sigma_{\mathrm{ML}}^{2}\right]      & = \mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}\left(x_{n}-\mu_{\mathrm{ML}}\right)^{2}\right] \\\\     & = \mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}\left(x_{n}^{2}+\mu_{\mathrm{ML}}^{2}-2x_{n}\mu_{\mathrm{ML}}\right)\right] \\\\     & = \mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}x_{n}^{2}-\frac{1}{N}\sum_{n=1}^{N}\left(2x_{n}\mu_{\mathrm{ML}}\right)+\mu_{\mathrm{ML}}^{2}\right] \\\\     & = \mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}x_{n}^{2}-\frac{1}{N}2\mu_{\mathrm{ML}}\sum_{n=1}^{N}\left(x_{n}\right)+\mu_{\mathrm{ML}}^{2}\right] \\\\     & = \mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}x_{n}^{2}-2\mu_{\mathrm{ML}}^{2}+\mu_{\mathrm{ML}}^{2}\right] \\\\     & = \mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}x_{n}^{2}-\mu_{\mathrm{ML}}^{2}\right]  \end{aligned} $$
> 
> 这里最好分开看容易理解
> 
>
> 对于第一项 $\mathbb{E}\left[\frac{1}{N} \sum_{n=1}^{N}x_{n}^{2}\right] = \frac{1}{N} \sum_{n=1}^{N}\mathbb{E}\left[x_{n}^{2} \right]$,
>
> 其中，根据方差公式可以得到： $\mathbb{E}\left[x_{n}^{2}\right]=\sigma^{2}+\mu^{2}$
> 
> 对于第二项 $\mathbb{E}\left[\mu_{\mathrm{ML}}^{2}\right]$可以看做是对$\mu_{\mathrm{ML}}$的估计，即根据方差公式可以得到：
> 
> $$ \begin{aligned} \mathbb{E}\left[\mu_{\mathrm{ML}}^{2}\right]&=\mathbb{D}(\mu_{\mathrm{ML}})+\mathbb{E}\left[\mu_{\mathrm{ML}}\right]^{2}\\\\ &=\mathbb{D}\left[\frac{1}{N} \sum_{n=1}^{N} x_{n}\right] + \mathbb{E}\left[\mu\right]^{2} \\\\ &=\frac{1}{N^{2}}\sum_{n=1}^{N}\mathbb{D}\left[x_{n}\right] + \mathbb{E}\left[\mu\right]^{2} \\\\ &=\frac{1}{N}\mathbb{D}[x]+\mu^{2} \\\\ &=\frac{1}{N}\sigma^{2} + \mu^{2} \end{aligned} $$
> 
> 其中$\mathbb{D}$为方差符号
> 
> 上述都用到的一个概念：$x_{i}$是$\bm{x}$的一个实例，$\bm{x}$服从什么分布，$x_{i}$也服从，即$\mathbb{E}[x_{i}]=\mathbb{E}[\bm{x}]$, $\mathbb{D}[x_{i}]=\mathbb{D}[\bm{x}]$
> 
> 综上：
> $$\mathbb{E}\left[\sigma_{\mathrm{ML}}^{2}\right]=\sigma^{2}+\mu^{2} - (\frac{1}{N}\sigma^{2}+\mu^{2})=\frac{N-1}{N}\sigma^{2}$$

## 1.5 决策论 (Decision Theory)

> 决策论在于概率论相结合时，可以让我们在涉及不确定性的情况下做出最佳决策

问题：给定一个向量$\mathbf{x}$与相应的目标$\mathbf{t}$，求对于$\mathbf{x}$中的一个新的值，预测得到的$\mathbf{t}$

以检测X-ray的癌症病症为例，输入的$\mathbf{x}$是图像中像素值的集合，输出的变量$t$将代表是不是患有癌症 

> 有癌症以$C_{1}$代表，没有癌症以$C_{2}$代表，同时可以使用数字来代替符号，即$t=0 \leftrightarrow C_{1};\quad t=0 \leftrightarrow C_{2}$

我们现在关心的是，对于一副给定病人X-ray的图像，去判断病人患癌的概率，即$p(C_{k}|\mathbf{x})$，可以使用贝叶斯公式进行如下表达：

$$p(C_{k}|\mathbf{x})=\frac{p(\mathbf{x}|C_{k})p(C_{k})}{p(\mathbf{x})}$$

> 这里，$p(C_{k})$可以成为对类别$C_{k}$的先验（即在不做X-ray之前，判断一个人是否患癌的概率）；
> 
> $p(\mathbf{x}|C_{k})$成为相对应的后验

### 1.5.1 最小误差



