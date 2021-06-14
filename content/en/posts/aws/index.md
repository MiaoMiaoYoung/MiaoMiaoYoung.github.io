---
title: "AWS s3 下载"
date: 2021-03-29T14:06:50+08:00
draft: False
categories:
    - work
tags:
    - aws下载
---

## 创建AWS账户

## 创建组

进入控制台：https://console.aws.amazon.com/

![](images/1.jpg)

创建组

![](images/2.jpg)

设置组名

![](images/3.jpg)


设置策略：s3-readonly和审核

![](images/4.jpg)

![](images/5.jpg)

## 创建用户

![](images/6.jpg)

设置用户名，访问权限

![](images/7.jpg)

将用户添加到组

![](images/8.jpg)

之后一路next，直到获得访问密钥

![](images/9.jpg)

## 安装CLI

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html
https://awscli.amazonaws.com/AWSCLIV2.msi

## 配置CLI

将前面的访问ID和私有访问密钥
![](images/10.jpg)

## aws s3命令下载数据集

```bash
aws s3 cp "s3://ml-inat-competition-datasets/2021/train.tar.gz" ./ --recursive
```

## 加速

https://blog.csdn.net/xuanwu_yan/article/details/79160034

修改配置文件vim ~/.aws/config，末尾加入
```
[default]
output = json 
s3 = 
  max_concurrent_requests =500 
  max_queue_size = 10001 
  multipart_threshold = 500MB
```