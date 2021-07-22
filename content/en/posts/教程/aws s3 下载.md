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

![1.jpg](https://i.loli.net/2021/07/22/5AIPLRMyXkUSOBp.jpg)


创建组

![2.jpg](https://i.loli.net/2021/07/22/XjVkK13NInCAfy6.jpg)


设置组名

![3.jpg](https://i.loli.net/2021/07/22/beHQjXGOaMqR9LY.jpg)


设置策略：s3-readonly和审核

![4.jpg](https://i.loli.net/2021/07/22/VJIYnqivh1cRZUF.jpg)

![5.jpg](https://i.loli.net/2021/07/22/Aj9l2G1R6NdUMhX.jpg)

## 创建用户

![6.jpg](https://i.loli.net/2021/07/22/xEh6wqjKukJ5vNc.jpg)

设置用户名，访问权限

![7.jpg](https://i.loli.net/2021/07/22/n9GT5ivPA4oxeyU.jpg)


将用户添加到组

![8.jpg](https://i.loli.net/2021/07/22/usmWrP3Y25NnwLb.jpg)


之后一路next，直到获得访问密钥

![9.jpg](https://i.loli.net/2021/07/22/W7HtJ2XNVDypQZg.jpg)


## 安装CLI

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html
https://awscli.amazonaws.com/AWSCLIV2.msi

## 配置CLI

将前面的访问ID和私有访问密钥

![10.jpg](https://i.loli.net/2021/07/22/nvogW2RzHVhEDjL.jpg)

## aws s3命令下载数据集

```bash
aws s3 cp "s3://ml-inat-competition-datasets/2021/train.tar.gz" ./ --recursive
```

![11.jpg](https://i.loli.net/2021/07/22/EaqGP4Mm3sBxgSW.jpg)


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