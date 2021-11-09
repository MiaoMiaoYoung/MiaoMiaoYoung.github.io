---
title: "Dockerfile"
date: 2021-04-15T12:24:19+08:00
draft: False
categories:
    - 教程
tags:
    - linux
    - ubuntu
    - docker
---

## 编写Dockerfile

### FROM

定制的镜像都是基于FROM镜像的，所以需要找一个基础镜像

```bash
## 基础镜像
FROM pytorch/pytorch:latest
## 维护者信息
LABEL maintainer "MiaoMiaoYang"
```

### RUN

RUN 相当于在容器中执行命令，有以下两种方式

- Shell格式
    ```bash
    RUN <命令行命令>
    ```

- Exec格式
    ```bash
    RUN ["可执行文件","参数1","参数2",...]
    ```

注意：Dockerfile的指令每执行一次，都会在docker上新建一层，如果无意义的层过多，会造成镜像膨胀过大。

```bash
FROM centos
RUN yum install wget
RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
RUN tar -xvf redis.tar.gz

#### 可简化为以下格式
#### 使用 \  进行换行
#### 使用 && 符号进行连接

FROM centos
RUN yum install wget \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
    && tar -xvf redis.tar.gz
```

### CMD指令

类似于RUN指令，但是RUN在docker build构建镜像时构建，CMD在docker run时运行

### COPY指令

从上下文目录中复制文件或目录到容器里的指定路径

```bash
## [--chown=<user>:<group>]：可选参数，用户改变复制到容器内文件的拥有者和属组。
COPY [--chown=<user>:<group>] <源路径1>...  <目标路径>
COPY [--chown=<user>:<group>] ["<源路径1>",...  "<目标路径>"]
```

### ADD指令

与COPY使用格式一致，不同的是在拷贝tar压缩文件（gzip,bzip2,xz）时，会自动进行复制并解压到目标路径。但是当压缩文件很大的情况下，会导致镜像构建很慢，或者导致崩溃。

### ENV指令

设置环境变量

### EXPOSE指令

声明端口，在运行时用于随机端口映射

## 构建Docker镜像

在Dockerfile文件的存放目录下，执行构建动作
```bash
docker build -t [image name]:[image label] .
## example
docker build -t miaomiaoyang/pytorch:test .
```
最后的.表示本次执行的上下文路径

## 启动Docker容器

```bash 
nvidia-docker run -itd --name nnunet --shm-size 6G -p 8000:80 -p 10022:22 -p 5000:5000 -v /home/MiaoMiaoYang:/MiaoMiaoYang miaomiaoyang/pytorch:test /bin/bash
```

## Pytorch 示例

- Dockerfile
    ```bash
    FROM pytorch/pytorch:latest
    ## 维护者信息
    LABEL maintainer "MiaoMiaoYang"

    ARG DEBIAN_FRONTEND=noninteractive
    ENV TZ=Asia/Shanghai

    ## 换源，将sources.list/requirements.txt放在    Dockerfile同目录下
    ADD sources.list /etc/apt/
    ADD requirements.txt /installer/

    RUN apt-get update \
        && apt-get upgrade --assume-yes \
        && apt-get install vim              --assume-yes \ 
        ## 添加SSHD服务
        && apt-get install openssh-server   --assume-yes \ 
        && apt-get install openssh-client   --assume-yes \
        && echo 'root:123456'|chpasswd \
        && mkdir -p /var/run/sshd \
        && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config \
        ## pip 添加库
        && pip config set global.index-url https://pypi.douban.com/simple/ \
        && pip install --no-cache-dir -r /installer/requirements.txt

    ## 开放端口22，镜像启动时启动SSHD服务
    EXPOSE  22
    CMD     ["/usr/sbin/sshd", "-D"]
    ```

```
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
```
原因是ubuntu 18.04后没有默认的系统时区，装一些包的时候会让我们选择默认时区

- requirement.txt
    ```bash
    dicom2nifti==2.2.12
    imageio==2.9.0
    matplotlib==3.3.4
    MedPy==0.4.0
    natsort==7.1.1
    packaging==20.9
    pandas==1.2.3
    Pillow==8.0.0
    pydicom==2.1.2
    pyOpenSSL==19.1.0
    PyWavelets==1.1.1
    PyYAML==5.3.1
    scikit-image==0.18.1
    scikit-learn==0.24.1
    scipy==1.6.1
    SimpleITK==2.0.2
    six==1.14.0
    sklearn==0.0
    tqdm==4.46.0
    traceback2==1.4.0
    ```




