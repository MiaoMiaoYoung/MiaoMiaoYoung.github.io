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

2. 将本机的SSH Key放到用户目录的~/.ssh目录下，.ssh目录权限为700 (chmod 700 .ssh)

3. 将id_rsa.pub文件改名为：authorized_keys，authorized_keys权限为600 

[注意，这里的权限是严格的700和600不能放松或者收紧，不然就还是需要密码登陆]

>https://www.androiddev.net/ssh-public-key-authentication-error/

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

## ASCII 艺术

```bash
watch -tn1 'pyfiglet -f slant `date +%T` | cowsay --random'
while sleep 3; do clear; fortune | cowsay --random | lolcat; done
while true; do clear; fortune | cowsay --random | lolcat; sleep 6; done
```

## PowerShell 运行脚本限制

在windows PowerShell上运行.bat脚本，会出现 **“ XXX， 因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies”** 的报错

这是因为PowerShell运行脚本权限限制

在PowerShell中直接输入get-ExecutionPolicy可以查看PowerShell权限，Restricted (限制)

在管理员模式下通过set-ExecutionPolicy命令修改权限，RemoteSigned为允许本地运行脚本，但是阻止远程；AllSigned为本地和远程都可运行脚本

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

![7.png](https://s2.loli.net/2024/01/21/debfQUpazyuT4Cc.png)

## 别名 Alias

- https://blog.csdn.net/Tos_CSDN/article/details/130821910

```bash
Get-Alias -name *                     ## 查看别名
Set-Alias -Name Edit -Value notepad   ## 创建一个别名notepad——>Edit
notepad c:\alias.ps1                  ## 创建一个powershell脚本文件y
Export-Alias c:\alias.ps1             ## 将别名导出到C:\alias.ps1
del alias:Edit                        ## 删除别名Edit
$alias:Edit                           ## 查看别名，不存在
Import-Alias -Force c:\alias.ps1      ## 将C:\alias.ps1导入powershell
$alias:Edit                           ## 查看别名，存在
```

但是这个只能在一个powershell窗口里存在，下面是创建永久别名的方法

- https://blog.csdn.net/u013391094/article/details/129340006

对于Powershell来说，有一个变量 Profile 定义了Powershell启动时默认加载的配置文件，查看变量的方法： 

```bash
Get-Variable Profile

# Name                           Value
# ----                           -----
# PROFILE                        C:\Users\XXX\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

注意，虽然有这个变量，但是不代表这个文件真的存在（甚至上层文件夹都不存在），查看这个文件是否存在方法：

```bash
Test-Path $profile
```

上面返回的 False 代表这个路径不存在（一般该文件在没有单独创建之前都是不存在的）

创建这个路径的方法：

```bash
New-Item -Type file -Force $profile

#  目录: C:\Users\XXX\Documents\WindowsPowerShell
#
#  Mode                 LastWriteTime         Length Name
#  ----                 -------------         ------ ----
#  -a----         2024/1/21     18:31              0 Microsoft.PowerShell_profile.ps1
```

将别名配置添加到Profile变量指向的配置文件中，可以使用notepad进行编辑。 这里为了演示方便，所以使用命令行进行操作，执行命令： 

```bash
Add-Content $Profile 'Set-Alias ll ls'
```


## history

- 显示时间戳

```bash
history | format-list
```

- 列出所有的历史记录

https://blog.csdn.net/Distiny_R/article/details/127909804