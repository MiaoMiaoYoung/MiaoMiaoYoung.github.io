---
title: "linux"
date: 2021-03-11T11:02:33+08:00
draft: false
categories:
    - work
tags:
    - linux
    - ubuntu
    - docker
    - 综合
---


- [docker创建容器](#docker创建容器)
- [中文编码](#中文编码)
- [多显卡运行程序](#多显卡运行程序)
- [ubuntu 镜像服务站](#ubuntu-镜像服务站)
- [pip 镜像服务站](#pip-镜像服务站)
- [linux 文件数](#linux-文件数)
- [linux 传输文件](#linux-传输文件)
- [ubuntu 版本](#ubuntu-版本)
- [显示网速](#显示网速)
- [tar](#tar)
  - [tar 仅打包](#tar-仅打包)
  - [tar.gz 压缩打包](#targz-压缩打包)


## docker创建容器

```bash
nvidia-docker run -it --net=host --shm-size 6G -v /home/MiaoMiaoYang:/MiaoMiaoYang miaomiaoyang/pytorch:v12 
## --shm-size 指定容器内存的大小
```

## 中文编码

```bash
export LANG=C.UTF-8
source /etc/profile
```

## 多显卡运行程序

CUDA_VISIBLE_DEVICES=0,1 XXX

## ubuntu 镜像服务站

```bash
cp   /etc/apt/sources.list   /etc/apt/sources.list.bak
vim /etc/apt/sources.list
apt-get update
```

> https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

## pip 镜像服务站

> https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

## linux 文件数

```bash
ls -l | grep -c '^-'
```

## linux 传输文件

```bash
scp    local_file   remote_username@remote_ip:remote_file 
scp -r local_folder remote_username@remote_ip:remote_folder 
```

## ubuntu 版本

```bash
cat /proc/version
```

## 显示网速

```bash
apt-get install nload 
nload -u H
```

## tar

### tar 仅打包

```bash
## 打包
tar -cvf code.tar.gz *.* m* r*
## 解压
tar -xvf code.tar.gz
```

### tar.gz 压缩打包

```bash
## 打包压缩
tar -zcvf code.tar.gz *.* m* r*
## 解压到当前目录下
tar -zxvf code.tar.gz
```




