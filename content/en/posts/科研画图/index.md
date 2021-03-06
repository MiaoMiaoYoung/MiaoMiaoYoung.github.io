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

### 去掉边框

```python
ax = plt.gca()  # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')  # 将右边 边沿线颜色设置为空 其实就相当于抹掉这条边
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
```

### 中心在(0,0)的坐标轴

```python
# 设置中心的为（0，0）的坐标轴
ax.spines['bottom'].set_position(('data', 0))  # 指定 data 设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
# plt.xticks(rotation=45)#x轴数值倾斜45度显示
plt.xlim(-4.0, 5.0) #x轴数值设置
plt.ylim(-0.2, 0.5)
```

