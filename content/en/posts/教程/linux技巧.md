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
    - 开机自启
enableTocContent: true
---




## docker创建容器

```bash
nvidia-docker run -it --net=host --shm-size 6G -v /home/MiaoMiaoYang:/MiaoMiaoYang miaomiaoyang/pytorch:v12 
## --shm-size 指定容器内存的大小
```

## docker apt 提示 Operation not permitted

https://blog.csdn.net/zhou920786312/article/details/119713645

设置privileged为true完全获得root权限

docker run -it --privileged=true centos:7.7.1908 bash

## 中文编码

```bash
export LANG=C.UTF-8
source /etc/profile
```

## 多显卡运行程序

CUDA_VISIBLE_DEVICES=0,1 XXX

## Ubuntu 镜像服务站

```bash
cp   /etc/apt/sources.list   /etc/apt/sources.list.bak
vim /etc/apt/sources.list
apt-get update
```

> https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

## pip 镜像服务站

> https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

## 计算文件数

```bash
ls -l | grep -c '^-'
```

## 传输文件

```bash
scp    local_file   remote_username@remote_ip:remote_file 
scp -r local_folder remote_username@remote_ip:remote_folder 
```

## 断点续传

```bash
apt-get install rsync
rsync --partial --progress -e ssh /path/to/local/file user@remote:/path/to/remote/file
```

--partial 实现断点续传

--progress 显示传输进度

## MD5

```bash
md5sum <文件路径>
```


## Ubuntu 版本

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

## Ubuntu 应用开机自启

> <https://zhuanlan.zhihu.com/p/98804785>

Ubuntu 18.04之后使用systemd管理系统，systemd默认读取[/etc/systemd/system]目录下的配置文件，并链接到[/lib/systemd/system/]目录下的脚本文件

1. 所以想要设置开机自启动，就需要修改启动脚本：

```bash
cd /lib/systemd/system
ls -lh
sudo vim rc.local.service
```

在末尾添加[Install]字段 (rc.local.service文件没有的话就新建一个)：

```yaml
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

# This unit gets pulled automatically into multi-user.target by
# systemd-rc-local-generator if /etc/rc.local is executable.
[Unit]
Description=/etc/rc.local Compatibility
ConditionFileIsExecutable=/etc/rc.local
After=network.target

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
RemainAfterExit=yes

[Install]  
WantedBy=multi-user.target  
Alias=rc-local.service
```

2. 创建rc.local监本，并添加执行权限

```bash
sudo touch /etc/rc.local
# 重要！！
sudo chmod a+x /etc/rc.local
```

3.  在[/etc/systemd/system]目录下创建软链接

```bash
ln -s /lib/systemd/system/rc.local.service /etc/systemd/system/
```

4. 在rc.local脚本中添加开机自启动的内容


5. 测试reboot



## Linux 命令别名

在~/.bashrc文件（用户配置文件）中修改：

```bash
alias work='cd /mnt/cache/ga/MiaoMiaoYang/VesselSeg/; conda activate miao-torch'
alias data='cd /mnt/petrelfs/ga/'
alias pid='squeue | grep ga'
alias nv='WatchNV(){ swatch -n $1 nv always;};WatchNV'
```

其中 nv 表示了带参数的命令的写法

## Device or resource busy 查找文件占用进程

- https://zhuanlan.zhihu.com/p/467274841

```
rm -rf .ps_00000097*
rm: cannot remove ‘.ps_000000978eec4c0100000088’: Device or resource busy
rm: cannot remove ‘.ps_000000979b8e2f0100000089’: Device or resource busy
```

使用以下命令查找进程

```bash
lsof | grep <设备或资源名>
```

## 分割文件

> https://deepinout.com/linux-cmd/linux-file-process-cmd/linux-cmd-split.html

按照大小将大文件分割成若干小文件

```bash
split -b 10G <file> PREFIX
```

split 参数：

    -a：指定输出文件名的后缀长度，默认为2个(aa,ab...)

    -d：指定输出文件名的后缀用数字代替

    -b：指定输出文件的最大字节数，如1k,1m...

    -C：指定每一个输出文件中单行的最大字节数

    -l：指定每一个输出文件的最大行数


合并文件

```bash
cat splog* > newLog.log
```
