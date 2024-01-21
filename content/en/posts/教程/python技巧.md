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

## Python虚拟环境

### 创建虚拟环境

https://docs.python.org/zh-cn/3/library/venv.html

```bash
python -m venv /path/to/new/virtual/environment
```

**Optional:**

- system-site-packages: Give the virtual environment access to the system site-packages dir.

    ```bash
    python -m venv ./venv --system-site-packages
    ```

### 激活虚拟环境

windows环境下，进入虚拟环境路径下的Scripts文件夹中

使用cmd命令行，输入activate激活虚拟python环境，注意！powershell有可能不太行，更改一下Powershell的脚本运行权限；是activate不是activate.bat


## 忽略警告

```python
import warnings
warnings.filterwarnings("ignore")
```

## mio

### get_files_name

```python
## 按顺序得到当前目录下，所有文件（包括文件夹）的名字
def get_files_name(dire):
    '''
    按顺序得到当前目录下，所有文件（包括文件夹）的名字
    :param dire: 文件夹目录
    :return:files[list]，当前目录下所有的文件（包括文件夹）的名字，顺序排列
    '''

    assert os.path.exists(dire), "{} is not existed".format(dire)
    assert os.path.isdir(dire), "{} is not a directory".format(dire)

    files = os.listdir(dire)
    files = natsort.natsorted(files)
    return files
```

### get_json

```python
## get json content as dict
def get_json(file):
    import json
    with open(file, 'r', encoding='utf-8') as f:
        dicts = json.load(f)
    return dicts
```

### get_csv

```python
## 获取csv文件
def get_csv(file, delimiter=','):
    import csv
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        result = list(reader)
    return result
```

### save_csv

```python
def save_csv(file, headers, rows, delimiter=','):
    import csv
    with open(file, 'w') as f:
        writer = csv.writer(f, delimiter=delimiter)
        if headers is not None:
            writer.writerow(headers)
        writer.writerows(rows)
```

### save_json

```py
## save dict as json
def save_json(dicts, file, indent=2):
    import json
    info = json.dumps(dicts, indent=indent, ensure_ascii=False)
    with open(file, 'w', encoding='utf-8') as f:  # 使用.dumps()方法时，要写入
        f.write(info)
```


