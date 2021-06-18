---
title: "从头再来之线性代数"
date: 2021-06-16T15:01:38+08:00
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
- [方程组的集合解释](#方程组的集合解释)
  - [行图像 (Row picture)](#行图像-row-picture)
  - [列图像 (Column picture)](#列图像-column-picture)
  - [矩阵](#矩阵)
- [消元法求解线性方程组](#消元法求解线性方程组)
  - [消元得到上三角矩阵](#消元得到上三角矩阵)
  - [消元法失效](#消元法失效)
  - [回代](#回代)
  - [矩阵形式描述消元法](#矩阵形式描述消元法)
    - [使用行进行计算](#使用行进行计算)
    - [消元矩阵](#消元矩阵)
  - [置换矩阵 (pemutation)](#置换矩阵-pemutation)
  - [矩阵的逆](#矩阵的逆)
- [矩阵的乘法和逆](#矩阵的乘法和逆)
  - [矩阵乘法](#矩阵乘法)
    - [点乘法](#点乘法)
    - [列向量法](#列向量法)
    - [行向量法](#行向量法)
    - [列 X 行](#列-x-行)
    - [分块乘法](#分块乘法)
  - [矩阵的逆 (Inverse)](#矩阵的逆-inverse)
    - [逆是否存在](#逆是否存在)
    - [奇异矩阵](#奇异矩阵)
    - [可逆矩阵](#可逆矩阵)
    - [矩阵乘积的逆](#矩阵乘积的逆)
    - [矩阵转置的逆](#矩阵转置的逆)
- [矩阵A的LU分解](#矩阵a的lu分解)
- [置换、转置与向量空间](#置换转置与向量空间)
  - [置换 (Permutation, $P$)](#置换-permutation-p)
  - [转置 (Transpose)](#转置-transpose)
  - [对称矩阵 (symmetric)](#对称矩阵-symmetric)
  - [向量空间](#向量空间)
    - [列空间](#列空间)

## 前沿

MIT 18.06，之前看过，但是都忘了，所以这回快速的复习一下，记好一些的笔记，要做题！

重振小镇做题家之荣耀，我辈义不容辞！

https://mitmath.github.io/1806/

![](./images/Gilbert%20Strang.jpg)

贴一张老爷子的照片，感谢！

---------------------------------

## 方程组的集合解释

> **线性代数：求解方程组**

$$\begin{cases}& 2x - y =0 \\\\ &-x + 2y = 3 \end{cases} \rightarrow \begin{bmatrix} 2 &-1 \\\\ -1 &2 \end{bmatrix} \begin{bmatrix}\bold{x} \\\\\bold{y} \end{bmatrix} = \begin{bmatrix} 0 \\\\ 3 \end{bmatrix} \rightarrow AX=B $$


### 行图像 (Row picture)

![](./images/1.jpg)

两条直线的交点就是这个方程组的解

### 列图像 (Column picture)

$$ \begin{bmatrix} 2 &-1 \\\\ -1 &2 \end{bmatrix} \begin{bmatrix} \bold{x} \\\\ \bold{y} \end{bmatrix} =  \begin{bmatrix} 0 \\\\ 3 \end{bmatrix}\rightarrow x \begin{bmatrix} 2 \\\\ -1 \end{bmatrix} + y \begin{bmatrix} -1 \\\\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 3 \end{bmatrix} \rightarrow Ax=b$$

这个方程的目的就是找到合适的$x$和$y$使得前两个向量组合可以得到后一个向量 **[也就是找到正确的线性组合]**，这里是列向量的线性组合

![](./images/2.png)

新的问题：**对于任意的b(右侧向量)，是否都能求解$Ax=b$**
也就是：列的线性组合能否覆盖整个空间？


### 矩阵

方程的矩阵形式：

$$Ax=b$$

矩阵A乘以向量x得到右侧的向量b

矩阵和向量的乘法的两种解：

- 使用列图像进行乘法（推荐）

    矩阵的每一列都看成是一列向量，外部的向量b其实就是每一列向量的系数

    或者可以将矩阵的每一列看成一个空间的基地，外部的向量b就是根据这个基地在每个方向上的长度

$$ \begin{bmatrix}     2 &5 \\\\ 1 & 3 \end{bmatrix} \begin{bmatrix}     1\\\\2 \end{bmatrix} = 1 \begin{bmatrix}     2\\\\ 1  \end{bmatrix} + 2 \begin{bmatrix}     5\\\\ 3 \end{bmatrix} =\begin{bmatrix}     12\\\\ 7 \end{bmatrix} $$

- 使用行图像进行计算

$$ \begin{bmatrix} 2 &5 \end{bmatrix} \begin{bmatrix}     1 \\\\ 2 \end{bmatrix} =12 $$

## 消元法求解线性方程组

### 消元得到上三角矩阵

$$ \begin{cases}     x+  &2y+ &z  &=2  \\\\     3x+ &8y+ &z  &=12 \\\\         &4y+ &z  &=2 \end{cases} \rightarrow Ax=b \qquad A=\begin{bmatrix}     1 &2 &1 \\\\     3 &8 &1 \\\\     0 &4 &1 \end{bmatrix} $$

按顺序进行消元，对角线上的元素称为主元(pivot)，因为需要使用对角线上的元素迭代的消去下面等式中的对应元素。但是0不能作为主元

$$ A= \begin{bmatrix}      1 &2 &1 \\\\      3 &8 &1 \\\\      0 &4 &1  \end{bmatrix} \stackrel{(2,1)}{\rightarrow} \begin{bmatrix} 1 &2 &1  \\\\      0 &2 &-2 \\\\      0 &4 &1  \end{bmatrix} \stackrel{(3,2)}{\rightarrow} \begin{bmatrix} 1 &2 &1  \\\\      0 &2 &-2 \\\\      0 &0 &5  \end{bmatrix} = U$$

> 箭头上方表示想要消去的元素的位置

这里消元的目的就是为了从$A$得到上三角矩阵$U$.

### 消元法失效

如果主元是0的时候，需要进行行交换，让非0元素占据主元的位置。

如果行交换无法使主元是非0元素，那么这个方程就没有解，这个矩阵也就是不可逆的。

### 回代

当使用消元法从$A$得到$U$之后，就需要把右侧向量$b$带入，引入$b$作为新的一列向量加入到矩阵中，也就是**增广矩阵**

$$ \begin{bmatrix}       1 &2 &1 &2 \\\\       3 &8 &1 &12 \\\\       0 &4 &1 &2   \end{bmatrix} $$

因为对左侧矩阵进行变化的同时，右侧向量也会跟着做同样的变化，所以按照上面的消元法：

$$  \begin{bmatrix}       1 &2 &1 &2 \\\\       3 &8 &1 &12\\\\       0 &4 &1 &2  \end{bmatrix}  \stackrel{(2,1)}{\rightarrow}  \begin{bmatrix}  1 &2 &1  &2  \\\\       0 &2 &-2 &6 \\\\       0 &4 &1  &2   \end{bmatrix}  \stackrel{(3,2)}{\rightarrow}  \begin{bmatrix}  1 &2 &1  &2 \\\\       0 &2 &-2 &6 \\\\       0 &0 &5  &-10  \end{bmatrix} \rightarrow c=\begin{bmatrix}    2 \\\\ 6 \\\\ -10\end{bmatrix}$$

所以最终方程的形式是这样的：

$$\begin{cases}     x+  &2y+ &z   &=2  \\\\         &2y- &2z  &=6 \\\\             &    &5z  &=-10\end{cases}\rightarrow Ux=c$$

接下来进行回代求解：$z=-2; y=1; x=2$

### 矩阵形式描述消元法

#### 使用行进行计算

$$ \begin{bmatrix}     1 &2 &7 \end{bmatrix} \begin{bmatrix}     2 & 3 & 4 \\\\     1 & 3 & 4 \\\\     2 & 3 & 5 \end{bmatrix} =  \begin{bmatrix}2 &3 &4\end{bmatrix}\times 1 + ... + \begin{bmatrix}2 &3 &5\end{bmatrix}\times 7 = \begin{bmatrix}18 &30 &47\end{bmatrix}  $$

**左行右列，左乘行变换，右乘列变换**

- 列向量是乘在矩阵的**右边**，对矩阵的每一列进行线性合并，得到的是**列向量**
- 行向量是乘在矩阵的**左边**，对矩阵的每一行进行线性合并，得到的是**行向量**

#### 消元矩阵

$$\begin{bmatrix}      1 &2 &1 \\\\      3 &8 &1 \\\\      0 &4 &1  \end{bmatrix} \stackrel{(2,1)}{\rightarrow} \begin{bmatrix} 1 &2 &1  \\\\      0 &2 &-2 \\\\      0 &4 &1  \end{bmatrix} \Rightarrow \begin{bmatrix}     1  &0 &0 \\\\     -3 &1 &0 \\\\     0  &0 &1 \end{bmatrix} \begin{bmatrix}        1 &2 &1 \\\\        3 &8 &1 \\\\        0 &4 &1   \end{bmatrix} = \begin{bmatrix}   1 &2 &1  \\\\        0 &2 &-2 \\\\        0 &4 &1     \end{bmatrix}$$

原来的消元法就变成了一个特定的矩阵：**消元矩阵**

$$E_{21} = \begin{bmatrix}     1  &0 &0 \\\\     -3 &1 &0 \\\\     0  &0 &1 \end{bmatrix}$$

他的每一行都是对矩阵的行变换，同时也被称为**初等矩阵$E$**，因为是对(2,1)位置上进行消元，所以可以写成$E_{21}$

所以，整个过程使用矩阵形式表达：

$$E_{32}(E_{21}A)=U$$

矩阵乘法满足结合律，所以可以将括号移动，变成一个矩阵，来实现所有的消元任务。但是矩阵乘法不满足交换律，不可轻易调换他们的顺序

$$(E_{32}E_{21})A=U$$

### 置换矩阵 (pemutation)

对行进行调换：

$$ \begin{bmatrix}     0 &1 \\\\     1 &0 \end{bmatrix} \begin{bmatrix}     a &b \\\\     c &d \end{bmatrix} = \begin{bmatrix}     c &d \\\\     a &b \end{bmatrix} $$

其中，$P=\begin{bmatrix}    0 &1 \\\\    1 &0\end{bmatrix}$就是**置换矩阵**，将两行进行位置的调换

同理，如果想对列进行置换，那么需要将矩阵进行右乘，**左行右列**

可以看到，因为想要消除置换矩阵带来的影响，那就是把它再置换回去，那么置换矩阵的逆就是置换矩阵的转置

$$P^{-1}=P^{T}$$

分清**转置(T，是一个操作)** 和 **置换(P，是一个矩阵)**，两个不一样的东西

### 矩阵的逆

$$\begin{bmatrix}     1  &0 &0 \\\\     -3 &1 &0 \\\\     0  &0 &1 \end{bmatrix} \begin{bmatrix}        1 &2 &1 \\\\        3 &8 &1 \\\\        0 &4 &1   \end{bmatrix} = \begin{bmatrix}   1 &2 &1  \\\\        0 &2 &-2 \\\\        0 &4 &1     \end{bmatrix}$$

初等矩阵$E_{21} = \begin{bmatrix}     1  &0 &0 \\\\     -3 &1 &0 \\\\     0  &0 &1 \end{bmatrix}$，从行2中减去了三倍的行1，现在我想回做这一步，也就是找到某一个矩阵取消这次消元（左乘），即两者相成为单位阵$I$：

$$E^{-1}_{21}E_{21}=I$$

那么对于$E_{21}$来说，他的含义相当于是从行2减去了三倍的行1，那么想消去这个行变换的影响，就应该让行2加回来三倍的行1，所以

$$E^{-1}_{21}=\begin{bmatrix}     1  &0 &0 \\\\     3 &1 &0 \\\\     0  &0 &1 \end{bmatrix}$$

## 矩阵的乘法和逆

### 矩阵乘法

矩阵乘法：$AB=C$

#### 点乘法

其中矩阵$C$的3行4列的元素$C_{34}=A_{row-3}\cdot B_{col-4}=\sum_{k=1}^{n}{a_{3k}b_{k4}}$

#### 列向量法

$$A_{m\times n}B_{n\times p} = C_{m\times p}$$

可以将乘法考虑成一个矩阵右乘以一个列向量，得到一个列向量。也就是**矩阵A**右乘矩阵B中的**每一个列向量**

那么，**矩阵C的各列是矩阵A中各列的线性组合**

#### 行向量法

与列向量法类似，可以将乘法考虑成矩阵B左乘矩阵A中的行向量，

**矩阵C的各行是矩阵B中各行的线性组合**

#### 列 X 行

常规方法中，是A的行$\times$B的列，得到是相对应位置的标量

但是这里可以是A的列$\times$B的行

$AB$是A的各列$\times$B的各行的矩阵的和


#### 分块乘法

将矩阵进行分块，对每一个分块进行乘法

$$ \begin{bmatrix}   A_{1} & A_{2} \\\\   A_{3} & A_{4} \end{bmatrix} \begin{bmatrix}   B_{1} & B_{2} \\\\   B_{3} & B_{4} \end{bmatrix} = \begin{bmatrix}   A_{1}B_{1} + A_{2}B_{3} & A_{1}B_{2}+A_{2}B_{4} \\\\   A_{3}B_{1} + A_{4}B_{3} & A_{3}B_{2}+A+{4}B_{4} \end{bmatrix} $$


### 矩阵的逆 (Inverse)

只考虑方阵(square matrix) $A$

#### 逆是否存在

如果存在，可以成立：$A^{-1}A=I$，$I$为单位阵

其中，这里的是左逆，也可以有右逆，表达为：$AA^{-1}=I$

对于方阵，左逆=右逆，即$A^{-1}A=I=AA^{-1}$

如果逆存在，那么矩阵A是可逆的，也就是**非奇异**的(non-singular)

#### 奇异矩阵

如果存在非0向量$x$使得$Ax=0$，那么这个矩阵$A$是奇异的

也就是其实在矩阵A中的列向量，最少有一对向量是共平面的


#### 可逆矩阵

求矩阵的逆：

$$ \begin{bmatrix}   1 & 3 \\\\ 2 &7 \end{bmatrix} \begin{bmatrix}   a & c \\\\ b &d \end{bmatrix} = \begin{bmatrix}   1 & 0 \\\\ 0 &1 \end{bmatrix} \rightarrow AA^{-1}=I $$

> Gauss-Jordan：同时处理两个方程组

对增广矩阵($[AI]$)进行消元，得到$E[A|I]=[EA|EI]=[I|E]$，那么$E$就是$A^{-1}$

$$ \begin{bmatrix}  \begin{array}{cc|cc}   1 & 3 & 1 & 0 \\\\    2 &7 & 0 & 1    \end{array}   \end{bmatrix}    \rightarrow  \begin{bmatrix}   \begin{array}{cc|cc}  1 & 3 & 1 & 0 \\\\   0 &1 & -2 & 1  \end{array}  \end{bmatrix}   \rightarrow   \begin{bmatrix}     \begin{array}{cc|cc}  1 & 0 & 7 & -3 \\\\   0 &1 & -2 & 1      \end{array}  \end{bmatrix} $$

#### 矩阵乘积的逆

$A$和$B$都是可逆矩阵，那么他们乘积的逆是$(AB)^{-1}=B^{-1}A^{-1}$

#### 矩阵转置的逆

$$(A^{-1})^{T} A^{T}= I$$

## 矩阵A的LU分解

考虑三维矩阵，对A进行消元得到U，即

$$E_{32}E_{31}E_{21}A=U$$

可以写成$A=LU$形式，即：

$$A=E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}U$$

其中U表示的上三角矩阵，L表示的下三角矩阵

$$ \begin{cases}   A = LU \\\\   EA=U \end{cases} $$

下面讨论这两种形式，为什么要变成$A=LU$的形式

对于$A=LU$如果不存在行互换，消元乘数可以直接写进$L$里面

**举个例子**

$$ E_{32}=\begin{bmatrix}   1 &0 &0 \\\\ 0 &1 &0 \\\\ 0 & -5 &1 \end{bmatrix} E_{31} = I \quad E_{21}=\begin{bmatrix}   1 &0 &0 \\\\ -2 &1 &0 \\\\ 0 &0 &1 \end{bmatrix} $$

对矩阵进行消元，进行上述消元变化：$E_{21}$和$E_{32}$

$$ E=E_{32}E_{31}E_{21} = \begin{bmatrix}   1 &0 &0 \\\\ -2 &1 &0 \\\\ 10 &-5 &1 \end{bmatrix} $$
这种形式下可以看到行1通过行2影响到了行3，在(1,3)位置出现了10

$$ L = E_{21}^{-1}E_{32}^{-1}= \begin{bmatrix}    1 &0 &0 \\\\ 2 &1 &0 \\\\ 0 &0 &1 \end{bmatrix} \begin{bmatrix}    1 &0 &0 \\\\ 0 &1 &0 \\\\ 0 & 5 &1  \end{bmatrix} = \begin{bmatrix}   1 &0 &0 \\\\ 2 &1 &0 \\\\ 0 &5 &1 \end{bmatrix} $$

在这种形势下，2和5不会冲突产生10，也就是消元乘数可以直接写到$L$里

## 置换、转置与向量空间

### 置换 (Permutation, $P$)

置换矩阵是行重新排列了的单位矩阵，是用来完成行互换的矩阵

对于需要进行置换操作的消元，$A=LU$就会变成了$PA=LU$

所有的置换矩阵都是可逆的，并且$P^{T} = P^{-1}$

对于n维方阵，共有$n!$个置换矩阵

### 转置 (Transpose)


$(A^{T})$ $_{ij}$  

$=A_{ji}$

### 对称矩阵 (symmetric)

对称矩阵：转置变换以后，没有变化的矩阵 $A^{T}=A$

所有的矩阵R转置乘以R都是对称的

$$ \begin{bmatrix}   1 &3 \\\\ 2 &3 \\\\ 4 &1 \end{bmatrix} \begin{bmatrix}   1 &2 &4 \\\\ 3 &3 &1 \end{bmatrix} = \begin{bmatrix}   10 &11 &7 \\\\   11 &13 &11 \\\\   7  &11 &17   \end{bmatrix} $$

证明：

$$(R^{T}R)^{T} = R^{T}R$$

### 向量空间

空间：满足加法和数乘（即可以进行线性运算），比如： $\mathbb{R}^{2}$，表示所有的二维实向量。(二维：即向量用两个实数表述)

$$ \begin{bmatrix}   3 \\\\ 2 \end{bmatrix}, \begin{bmatrix}   0 \\\\ 0 \end{bmatrix}, \begin{bmatrix}   \pi \\\\ e \end{bmatrix}, \cdots $$

$\mathbb{R}^{n}$包含所有的n维实向量

子空间：需要满足线性运算，但同时又是空间的子集，比如$\mathbb{R}^{2}$的子空间：

- $\mathbb{R}^{2}$本身
- 所有经过原点的直线
- (0,0)点



#### 列空间

从矩阵中构造一个子空间：

$$A=\begin{bmatrix}  1 &3 \\\\ 2 &3 \\\\ 4 &1 \end{bmatrix}$$

矩阵A的所有列都在$\mathbb{R}^{3}$空间中，他的列的所有线性组合都成一个子空间：**列空间**，记作$C(A)$








