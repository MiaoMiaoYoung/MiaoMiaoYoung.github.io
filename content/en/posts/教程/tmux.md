---
title: "tmux调教指南"
date: 2023-10-01T14:36:46+08:00
draft: False
categories:
    - 教程
tags:
    - linux
---

快捷键 <ctrl+b> 是连按的，然后松开再输入新的指令

## 会话管理

### 新建会话

```bash
tmux new -s <session-name>
```

### 分离会话

```bash
tmux detach
```

> 快捷键 <ctrl+b> + d

上面命令执行后，就会退出当前 Tmux 窗口，但是会话和里面的进程仍然在后台运行。

### 接入会话

```bash
# 使用会话编号
tmux attach -t 0

# 使用会话名称
tmux attach -t <session-name>
```

## 窗格管理

### 划分窗格

```bash
# 划分上下两个窗格
tmux split-window 
# 快捷键 <Ctrl+b> + "


# 划分左右两个窗格
tmux split-window -h
# 快捷键 <Ctrl+b> + %
```

## 窗口管理

### 新建窗口

```bash
# 新建窗口
tmux new-window -n <window-name>
# <Ctrl+b> + c
```

### 切换窗口

```bash
# 切换到指定编号的窗口
tmux select-window -t <window-number>

# 切换到指定名称的窗口
tmux select-window -t <window-name>
```

### 快捷键

<Ctrl+b> + c：创建一个新窗口，状态栏会显示多个窗口的信息。
<Ctrl+b> + p：切换到上一个窗口（按照状态栏上的顺序）。
<Ctrl+b> + n：切换到下一个窗口。
<Ctrl+b> + <number>：切换到指定编号的窗口，其中的<number>是状态栏上的窗口编号。
<Ctrl+b> + w：从列表中选择窗口。

------------------------------------------

## Q&A

### 分辨率，出现好多点

ctrl  + b
shift + d

选择分辨率最小的窗口退出，再attach进来

