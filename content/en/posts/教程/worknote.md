---
title: "Work Note"
date: 2022-07-12T11:16:18+08:00
draft: false
categories:
    - 教程
tags:
    - python
    - code    
---

## 平滑一组数据 (Smooth)

```python
from scipy.ndimage import gaussian_filter1d
import numpy as np
gaussian_filter1d([1.0, 2.0, 3.0, 4.0, 5.0], 1)
gaussian_filter1d([1.0, 2.0, 3.0, 4.0, 5.0], 4)
import matplotlib.pyplot as plt
np.random.seed(280490)
x = np.random.randn(101).cumsum()
y3 = gaussian_filter1d(x, 3)
y6 = gaussian_filter1d(x, 6)
plt.plot(x, 'k', label='original data')
plt.plot(y3, '--', label='filtered, sigma=3')
plt.plot(y6, ':', label='filtered, sigma=6')
plt.legend()
plt.grid()
plt.show()
```
