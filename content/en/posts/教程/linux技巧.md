---
title: "linux"
date: 2021-03-11T11:02:33+08:00
draft: false
categories:
    - 教程
tags:
    - linux
    - docker
    - tar
    - 传输文件
    - 中文编码
    - 多显卡
    - 镜像服务站
    - 终端代理
enableTocContent: true
---




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


## 终端代理

教程：

> https://zhuanlan.zhihu.com/p/46973701

![V2rayN.png](https://s2.loli.net/2021/12/08/ZuCBp9U6GVwFvML.png)

在本机上打开代理，打开局域网连接的选项，找到代理的地址：SOCKS5，找到本机在局域网的ip地址

![V2rayN-1.png](https://s2.loli.net/2021/12/08/Yfte4p9vJdD5Z6u.png)

![http_proxy.png](https://s2.loli.net/2021/12/08/m6BOd1qDJtHQYLa.png)

通过http_proxy命令进行ip终端代理

```bash
all_proxy="socks5://192.168.31.79:10808" make -j4
```
