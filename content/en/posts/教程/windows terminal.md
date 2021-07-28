---
title: "Windows Terminal调教指南"
date: 2021-07-22T14:24:19+08:00
draft: false
categories:
    - 教程
tags:
    - shell
    - code
    - windows shell
---

> 官方教程：https://docs.microsoft.com/zh-cn/windows/terminal/
> https://github.com/microsoft/terminal

## SSH

### SSH 配置

打开Windows Terminal中的设置settings.json文件

![1.jpg](https://i.loli.net/2021/07/22/8JU3DX51VPCaeMu.jpg)

![2.jpg](https://i.loli.net/2021/07/22/YhzG8ScvQxOU7ow.jpg)

"profiles" → "list" 中添加新的会话窗口，其中填写可配置字段：

- guid: 唯一标识码
    
    可通过guid生成工具产生，如：https://www.guidgen.com/

- name: 远程终端的名字
- commandline： 打开终端执行的命令行
  
    可在该命令行中写入ssh命令和对应远程地址

- hidden: (bool) 该终端是否在选项中可见
- icon: 终端的图标
- fontSize: 字号大小
- cursorColor: 光标颜色

最终效果如下：

```json
{
    "guid": "{ffe6d8bc-3a50-48cb-80fc-69f062c95eb4}",
    "hidden": false,
    "name": "name",
    "commandline": "ssh user@ip -p22",
    "icon": "F:/installer/图标/ubuntu.jfif",
    "fontSize": 8,
    "cursorColor": "#000000"
}
```

![3.jpg](https://i.loli.net/2021/07/22/kYwjXN6E3xlVvua.jpg)

### 密码登陆效果

![4.jpg](https://i.loli.net/2021/07/22/HPZlzfaAjqTed4I.jpg)

### SSH 免密登陆

很多服务器都是需要认证的，ssh认证是其中的一种。在客户端生成公钥，**把生成的公钥添加到服务器**，你以后连接服务器就不用每次都输入用户名和密码了。

1. 创建SSH Key

    ```bash
    ssh-keygen
    ```

    在git-bash下输入上述bash命令，如果不想要密码可以在要求输入密码的时候按两次回车，表示密码为空，并且确认密码为空

    ![5.jpg](https://i.loli.net/2021/07/22/2RaeMUkWjzTQo4C.jpg)

    这时，C:用户/User/.ssh下，就生成了SSH公钥

    ![6.jpg](https://i.loli.net/2021/07/22/9kRXbMidF6qNxoH.jpg)

2. 将本机的SSH Key放到用户目录的~/.ssh目录下，目录权限为700

3. 将id_rsa.pub文件改名为：authorized_keys

## 拆分窗口

1. 复制并拆分窗口 Alt+Shift+D

2. 创建垂直窗格 Alt+Shift+'+'

3. 创建水平窗格 Alt+Shift+'-'


## 美化

### 背景图片

"profiles" → "defaults" 中添加字段：

```json
"backgroundImage" : "F:\\pictures\\collection\\nichijou\\LQs9bx.jpg",
"backgroundImageOpacity": 0.15
```
