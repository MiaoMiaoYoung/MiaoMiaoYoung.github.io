---
title: "Python"
date: 2021-03-09T11:09:34+08:00
draft: false
image: images/posts/python.jpg
categories:
    - 教程
tags:
    - 文件操作
    - cv2
---

## 文件操作
```Python
# 递归删除一个目录以及目录内的所有内容（包括这个目录）
shutil.rmtree( src )   
# maybe_mkdir_p
```


## pip cv2

```bash
pip install opencv-python
```

安装成功之后Docker ubuntu 中会报错：

```bash
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory
```

解决：

```bash
apt-get install -y libgl1-mesa-dev
apt-get install libglib2.0
```


## 创建虚拟环境

https://docs.python.org/zh-cn/3/library/venv.html

```bash
python3 -m venv /path/to/new/virtual/environment
```

**Optional:**

- system-site-packages: Give the virtual environment access to the system site-packages dir.

    ```bash
    python -m venv ./venv --system-site-packages
    ```

## 忽略警告

```python
import warnings
warnings.filterwarnings("ignore")
```
