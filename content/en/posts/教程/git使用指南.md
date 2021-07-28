---
title: "Git使用指南"
date: 2021-06-04T15:01:38+08:00
draft: false
image: images/posts/git.jpg
categories:
    - 教程
tags:
    - git
---

## 建立仓库

初始化，将当前目录作为git仓库

```bash
## 将当前目录作为git仓库
git init
## 指定目录作为git仓库
git init repo
```

## 添加文件

git可以理解为一个文件管理系统，需要在仓库中加入指定新文件

```bash
## 添加指定文件
git add filename
## 添加当前文件夹下所有文件
git add .
```

## 提交到仓库

文件添加到git后，只是被写入了索引，但是还没有将文件真正的送入仓库，所以使用提交来把文件送入仓库。

-m 添加注释信息
-a 自动提交而不需要每一个都add。但是，**只适用于被修改的文件**，新文件不会自动提交。

```bash
git commit -m "comment"
```

## 发布版本

将修改后的一个版本推送到服务器上

```bash
git push ssh://example.com/~/www/project.git
```

## 删除文件

从资源库中删除文件

```bash
git rm file
```

## 分支与合并

分支在本地完成速度快。使用branch创建一个新的分支

```bash
git branch test
```

branch只是创建了一个新的分支，当前我们还是留在了原来的分支下，所以使用checkout目录来更改分支

```bash
git checkout test
```

第一个分支（主分支）一般是"main"，对于在分支上的修改不会反应在主分支上，所以想在主分支上提交修改，需要切回主分支，然后使用合并命令

```bash
git checkout master
git merge test
```

使用-d标识来删除分支

```bash
git branch -d test
```

使用-m/-M表示来对分支进行重命名

```bash
git branch -M main
```

