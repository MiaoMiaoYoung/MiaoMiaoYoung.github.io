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
## pip pyradiomics

在使用pytorch官方docker镜像时，安装pyradiomics时会报错

1. 首先是镜像中没有gcc编译器，而pyradiomics是需要gcc来进行编译的
2. ERROR: Cannot uninstall 'ruamel-yaml'
    
    这个是因为原先的镜像中已经有了ruamel.yaml和ruamel.yaml.clib，如果单独卸载ruamel.yaml会报错："It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall."

    - 通过pip -V找到site-packages的路径
    - 删除site-packages文件夹内所有ruamel的文件
    - 再次进行pip install pyradiomics的安装

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
