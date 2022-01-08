---
title: "群晖折腾指北"
date: 2022-01-04T15:01:38+08:00
draft: false
categories:
    - 教程
tags:
    - Synology
    - 群晖

enableTocContent: true
---

## 安装 Docker

在群晖的 套件中心 -> 所有套件 -> 搜索 "Docker" 就可以找到，之间安装就好


官方docker hub源可能因为众所周知的原因特别的慢，这就需要换一个源：<https://blog.csdn.net/weixin_33621280/article/details/112905964>

![1.png](https://s2.loli.net/2022/01/05/EmypMH1DBqSPLTa.png)
![3.png](https://s2.loli.net/2022/01/05/4NhRF1BYWQPXKb3.png)
![4.png](https://s2.loli.net/2022/01/05/gd9m1X75WDAF2vM.png)


Docker -> 注册表 -> 设置 中，选中第一个Docker官方的"Docker Hub"项目，选择编辑，启用注册表镜像，在镜像中添加下面的
```
https://registry.docker-cn.com
http://hub-mirror.c.163.com
https://mirror.ccs.tencentyun.com
https://docker.mirrors.ustc.edu.cn
https://dockerhub.azk8s.cn
```


如果新增加一个，则会出现注册表回传错误结果或者结果为空


## Jellyfin 家庭影院

> <https://zhuanlan.zhihu.com/p/384241222?ivk_sa=1024320u>
> 
> Jellyfin 是一个自由的软件媒体系统，用于控制和管理媒体和流媒体。用于管理媒体和提供媒体服务。大白话讲就是用照片墙的形式展示你自己的电影、电视剧等多媒体数据，并提供多平台访问播放服务。

这里采用docker的形式安装jellyfin


1. 下载jellyfin/jellyfin镜像

    在docker的注册表中搜索jellyfin，找到jellyfin/jellyfin的镜像

    [这个最后是通过梯子和手动docker pull完成的，不得不说页面的东西还是太难用了...]

    ![2.png](https://s2.loli.net/2022/01/05/yYN2UBEIK9RbmfZ.png)

2. 启动镜像，进行一些常规设置

    - 在高级设置中添加开机自启动
        ![5.png](https://s2.loli.net/2022/01/05/vm52tehBGyd1zio.png)
    - 添加外部挂载：
        /media 挂载为影片
        /config 挂载为设置
        ![6.png](https://s2.loli.net/2022/01/05/HwZmJDxQOPjcf1G.png)
    - 端口可以设置，也可以选择自动映射
        ![7.png](https://s2.loli.net/2022/01/05/V31yRNQJti7AcK4.png)

    设置完成后就可以启动镜像了

    ![8.png](https://s2.loli.net/2022/01/05/zK3QpSrsOt6Yq79.png)

3. 在网页端打开群晖的ip地址+相应端口就可以看到Jellyfin的欢迎界面和相关提示设置信息了

    ![9.png](https://s2.loli.net/2022/01/05/yl1hKOL2a8QPNi5.png)



4. 安装Jellyfin套件
   
   - 在套件中心->设置->套件来源中新增套件来源 <https://packages.synocommunity.com>
   - 在套件中心搜索Jellyfin，找到进行安装

![10.png](https://s2.loli.net/2022/01/05/E5eVGpThKxnZA3v.png)

![11.png](https://s2.loli.net/2022/01/05/gE8IieM2lHdwhZK.png)


> 但是现在还有问题，就是刮削的问题，导入多部影片只显示一部的问题

5. 设置 -> 控制台 -> 媒体库 -> [电影] -> 管理媒体库

将 "启用实时监控"、"电影院数据下载器"全部取消勾选，重新扫描一下媒体库，就可以了
