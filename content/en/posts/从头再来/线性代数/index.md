---
title: "重生之线性代数"
date: 2019-09-16T15:01:38+08:00
draft: false
categories:
    - work
    - mathematics
    - matrix
tags:
    - math
    - Linear Algebra
---

## 前沿

MIT 18.06，之前看过，但是都忘了，所以这回快速的复习一下，记好一些的笔记，要做题！

重振小镇做题家之荣耀，我辈义不容辞！

https://mitmath.github.io/1806/

---------------------------------

## 方程组的集合解释

> 线性代数：求解方程组

$$
\left\{
\begin{aligned}
    & 2x - y =0 \\
    & -x + 2y = 3
\end{aligned}
\right.

\rightarrow

\begin{bmatrix}
    2  &-1 \\
    -1 &2
\end{bmatrix}
\begin{bmatrix}
    \bold{x} \\
    \bold{y}
\end{bmatrix}
=
\begin{bmatrix}
    0 \\
    3
\end{bmatrix}

\rightarrow

AX=B
$$

### 行图像 (Row picture)

![](./images/1.jpg)

两条直线的交点就是这个方程组的解

### 列图像 (Column picture)

$$
\begin{bmatrix}
    2  &-1 \\
    -1 &2
\end{bmatrix}
\begin{bmatrix}
    \bold{x} \\
    \bold{y}
\end{bmatrix}

\rightarrow

x
\begin{bmatrix}
    2 \\ -1
\end{bmatrix}
+
y
\begin{bmatrix}
    -1 \\ 2
\end{bmatrix}
=
\begin{bmatrix}
    0 \\ 3
\end{bmatrix}
$$

这个方程的目的就是找到合适的$x$和$y$使得前两个向量组合可以得到后一个向量 **[也就是找到正确的线性组合]**，这里是列向量的线性组合

![](./images/2.png)

### 矩阵




