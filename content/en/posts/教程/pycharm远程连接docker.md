---
title: "Pycharm远程连接Docker容器"
date: 2021-03-11T10:37:48+08:00
draft: False
categories:
    - work
tags:
    - pycharm
    - docker
    - ubuntu
    - linux
---

参考：
- https://blog.csdn.net/hanchaobiao/article/details/84069299
- https://blog.csdn.net/Thanours/article/details/109271836
  
平台：ubuntu 18.04

## 启动docker容器，映射端口

```bash
nvidia-docker run -it --name nnunet --shm-size 6G -p 8000:80 -p 10022:22 -p 5000:5000 -v /home/MiaoMiaoYang:/MiaoMiaoYang miaomiaoyang/pytorch:nnunet
## --net=host存在的情况下，端口映射不管用，所以需要把网络模式更改一下
```

## 容器修改，建立ssh

- 修改root密码
    ```bash
    passwd:123456
    ```
- 安装ssh
    ```bash
    apt-get install openssh-server
    apt-get install openssh-client
    ```
- 检查是否启动
    ```bash
    ps -e |grep ssh
    ```
    如果看到sshd说明已经启动了

- 允许root账户登录ssh
    ```bash
    vim /etc/ssh/sshd_config
    ## 注意，这里是sshd，还有一个类似的ssh是没有的
    ```
    vim中使用/PermitRootLogin进行搜索，将下述字段替换
    ```
    #LoginGraceTime 2m
    #PermitRootLogin prohibit-password
    #StrictModes yes
 
    LoginGraceTime 2m
    PermitRootLogin yes
    StrictModes yes
    ```
    然后，重启ssh使设置生效
    ```bash
    service ssh restart
    ```


- 测试容器是否能与外部通信

    ```bash
    ssh root@127.0.0.1 -p 10022
    ```

    ![1.jpg](https://i.loli.net/2021/07/22/WaoA9JXpxOuQvHy.jpg)


## pycharm远程连接

- 设置pycharm
    ![2.jpg](https://i.loli.net/2021/07/22/4X6Lsb2tEzkavVx.jpg)

    Pycharm $\rightarrow$ Tools $\rightarrow$ Deployment $\rightarrow$  Configuration  

- 配置SFTP远程服务器
    ![5.jpg](https://i.loli.net/2021/07/22/1IFxy58D2GkNJaM.jpg) 
    
    - host: 服务器地址
    - Username: docker中的用户名 (不是主机的user)
    - Password: docker中用户的密码
    - 端口：10022 (docker中的端口)
    
    点击Test Connection测试链接是否成功，测试成功如下图所示：
    ![4.jpg](https://i.loli.net/2021/07/22/YXr9J4qkOdPpFNH.jpg)


- 将本地代码与远程服务器代码连接
    ![6.jpg](https://i.loli.net/2021/07/22/FcoM9BReS3b2AhG.jpg)
    Mappings中，Local path为本地项目地址，Deployment path为远程服务器地址，点击OK

- 将代码上传到服务器进行调试测试
    ![8.jpg](https://i.loli.net/2021/07/22/PWsa4Ylhw8U952S.jpg)


## pycharm配置docker服务

- 配置Python编译器

    ![15.jpg](https://i.loli.net/2021/07/22/SFrpvM86l3baCfJ.jpg)

    File $\rightarrow$ Settings，配置项目编译器（Project Interpreter），选择SSH Interpreter，选择现有服务器设定，Pycharm会自动选中之前STFP的设定。
    之后选择Move this server to IDE settings，之后Next。

    ![16.jpg](https://i.loli.net/2021/07/22/6oBesWOAmLdwNCy.jpg)
    选择远程主机中Python的路径，然后Finish。
    （docker中可能没有sudo，就不需要选了）

    ![18.jpg](https://i.loli.net/2021/07/22/OKnNbkJhsivBS35.jpg)
    可以看到，已经加入了远程的编译器了

    ![20.jpg](https://i.loli.net/2021/07/22/fTdSMhOFQYP3xrX.jpg)
    配置Python运行设置