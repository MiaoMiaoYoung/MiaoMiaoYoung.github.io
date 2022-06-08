---
title: "群晖折腾指北-22.06.07"
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

## 意外断电

家里意外断电之后，有一块硬盘正在读写数据，导致了群晖的报警，**此硬盘处于严重状态**

![15.png](https://s2.loli.net/2022/06/07/uPo7GXJ4TAEYbvw.png)

> https://kb.synology.cn/zh-cn/DSM/tutorial/Drive_in_abnormal_statuses

后来根据上面的指导，停用了硬盘，但是存储空间出现了堪用的警告，于是暑期回家后，想着怎么解决这个问题

首先想的就是一次停电会造成影响，但是损失一块硬盘觉得太难过了，于是看看硬盘是不是真的损坏了

> https://kb.synology.cn/zh-cn/DSM/tutorial/What_do_I_do_when_a_volume_crashes

首先在群晖上，执行了完整的SMART测试和IronWolf测试，显示都是正常和良好


![17.png](https://s2.loli.net/2022/06/07/dSbspHtPgXl7DWj.png)

然后又在diskgenius上进行了检测，发现健康状态也是良好

![16.png](https://s2.loli.net/2022/06/07/DUfi6YLFt8swXl9.png)

在diskgenius上检测了坏道，发现只有一个坏块，进行修复了一下，应该说硬盘状态还是不错的，但是在插到群晖上时发现群晖还是认为这块硬盘处于严重状态，不让使用

![18.png](https://s2.loli.net/2022/06/07/Zyvw1iPN43ltFUX.png)

很多文章说可以考虑重新初始化一下SMART信息，但是这个操作还是比较复杂的，而且我看了一下我的硬盘SMART的信息基本显示出来这块硬盘还是非常好的，没有严重的状态

然后就看到了这个博客：

> https://serverfault.com/questions/1095545/synology-storage-manager-rejects-healthy-disks-as-critical-because-of-reset-c

发现了群晖中的日志系统会记录每个硬盘的状况和操作，于是在群晖里打开了这个硬盘的日志

![14.png](https://s2.loli.net/2022/06/07/NYyQX26CLiAvadD.png)


发现确实这个硬盘的所有动作都被群晖记录了下来，然后每回这个硬盘重新连接到NAS上，群晖就会检测到这个硬盘曾经出现过问题，所以不让用，那么接下来解决办法就比较清楚了，找到这个日志，并且删除它，看看能不能成功

```bash
root@diskstation:/# grep -r ZR52AGQE /var/*
...
Binary file /var/log/synolog/.SYNODISKDB matches
Binary file /var/log/synolog/.SYNODISKHEALTHDB matches
Binary file /var/log/synolog/.SYNODISKTESTDB matches
...
```

**ZR52AGQE**为硬盘的序列号，不是机器的序列号，这个可以找出硬盘日志的位置，一般是在 /var/log/synolog 中，注意，这里要管理员权限，可以sudo su一下

在/var/log/synolog中可以看到数据库文件.SYNODISKDB记录了硬盘的动作和操作信息，使用sqlite3命令行对这个数据库进行操作

![13.png](https://s2.loli.net/2022/06/07/so2LZ6tUp8WxXDQ.png)

首先查看一下日志，发现确实很多关于这个硬盘的错误信息，然后将这个硬盘的日志全部删去

```SQL
SELECT * FROM logs WHERE serial = 'ZR52AGQE';
DELETE FROM logs WHERE serial = 'ZR52AGQE';
DELETE FROM logs WHERE serial ='ZR52AGQE';
```
操作完之后，重启NAS，发现问题解决了

接下来就是把这块“崭新”的硬盘，重新加入到存储池就好，修复一下存储空间就好

后面为了防止再次断电的意外发生，还是鼓捣了一台UPS对群晖进行意外断电的保护
