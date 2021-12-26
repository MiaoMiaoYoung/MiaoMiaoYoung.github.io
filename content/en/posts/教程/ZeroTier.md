---
title: "ZeroTier内网穿透"
date: 2021-01-15T14:24:19+08:00
draft: false
categories:
    - 教程
tags:
    - 内网穿透
    - Linux

Author: MiaoMiaoYang
---

> 注意：不是Zotero文献管理软件！
>
> **ZeroTier**是无公网IP的内网穿透的一种解决办法


## 注册账户

> https://my.zerotier.com/

![1.png](https://s2.loli.net/2021/12/15/NPOEYW8zZK3MQjq.png)

## 创建网络

点击"Create A Network"创建网络

![2.png](https://s2.loli.net/2021/12/15/oCj6HKwTGiD8cYV.png)

可以看到创建的网络ID (Network ID)，之后连接都是通过这个Network ID来连接的

![3.png](https://s2.loli.net/2021/12/15/KBTGh15mEM2S3e9.png)

点开这个网络，可以看到Access Control的两种方式，一种是PRIVATE，每次添加新的主机时，需要手动勾选是否允许连接。另一种是PUBLIC，表示加入网络后自动分配IP并允许连接

![4.png](https://s2.loli.net/2021/12/15/gtsA1GoaHEcQVlN.png)

到此，一个中转的ZeroTier就配置完成了，接下来只需要其他设备安装所对应的客户端，然后加入到这个网络中就好了

## Windows

> https://www.zerotier.com/download/

下载Windows客户端

![5.png](https://s2.loli.net/2021/12/15/1CQRspe62gqGTOz.png)

安装成功后，下面输入Network ID后“Join Network”

![6.png](https://s2.loli.net/2021/12/15/q3CdRxrSFMn5scL.png)


在ZeroTier的网页端，如果选择了PRIVATE模式，则需要点开当前的网络，对这台设备进行授权

![9.png](https://s2.loli.net/2021/12/15/UgZJesI45yGf7vz.png)

授权成功后，可以看到授权的用户为1：

![10.png](https://s2.loli.net/2021/12/15/1HtDQeIKMEN3u7q.png)

Windows配置完成，可以在本地看到加入的网络：

![11.png](https://s2.loli.net/2021/12/15/vtrxDfoyKNJjX5g.png)

## Ubuntu

> https://www.zerotier.com/download/

跟着官网指示一步步来：

```bash
curl -s https://install.zerotier.com | sudo bash
```

![12.png](https://s2.loli.net/2021/12/15/aPkVl1xOcfjUu6Z.png)

启动服务：

```bash
zerotier-one -d
```

> 这里遇到了报错： zerotier-one: fatal error: cannot bind to local control interface port 9993
> 
> 解决办法：https://blog.csdn.net/qq_33887096/article/details/114532957
> 
> ```bash 
> killall -9 zerotier-one   # 杀死zerotier所有进程
> netstat -lp | grep zero   # 查看9993端口是否被占用，如果还有占用的，多执行killall命令，杀死所有zerotier进程
> zerotier-one -d           #启动zerotier客户端
> zerotier-cli listnetworks #列出连接的zerotier网络
> ```

![14.png](https://s2.loli.net/2021/12/15/lFnK64JRsI3uELP.png)

查看服务状态


```bash
zerotier-cli status
```

加入网络：

```bash
zerotier-cli join [Network-ID] ## 加入后会提示 200 join OK
```

![15.png](https://s2.loli.net/2021/12/15/paDxBZ79UfwziHW.png)

同上，如果Network选择的是PRIVATE模式，那么需要进行认证

使用ifconfig查看Ubuntu当前网络，可以看到已经添加了：

![16.png](https://s2.loli.net/2021/12/15/GF27kq4MdSlwv8I.png)

--------------------------------

加入、离开、列出网络状态：

```bash
zerotier-cli join Network ID
zerotier-cli leave Network ID
zerotier-cli listnetworks
```
