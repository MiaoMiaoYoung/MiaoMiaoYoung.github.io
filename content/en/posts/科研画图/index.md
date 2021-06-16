---
title: "科研画图"
date: 2021-06-05T11:16:18+08:00
draft: false
categories:
    - work
    - code
tags:
    - 画图
---

## matlibplot

### 限制画布范围

只显示一定区域的图像，超出这个区域的图像不进行绘制

```python
plt.xlim(xmin=-30,xmax=30)
plt.ylim(ymin=-30,ymax=30)
```

### 网格

```python
plt.grid(True)
```

### 箭头

```python
plt.arrow(x=0, y=0, dx=2, dy=-1,width=0.005,head_width=0.1,ec='r',fc='r')
plt.arrow(x=0, y=0, dx=-1, dy=2,width=0.005,head_width=0.1,ec='r',fc='r')

plt.xlim(xmin=-3,xmax=3)
plt.ylim(ymin=-3,ymax=3)
plt.grid(True)
plt.show()
```

也可以使用在标注过程中产生的箭头

```python
plt.annotate("(2,-1)", xy=(2, -1), xytext=(0, 0), arrowprops=dict(arrowstyle="simple", color="r"))

plt.xlim(xmin=-3, xmax=3)
plt.ylim(ymin=-3, ymax=3)
plt.grid(True)
plt.show()
```
