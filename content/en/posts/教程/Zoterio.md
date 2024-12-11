---
title: "Zoterio"
date: 2021-11-12T14:24:19+08:00
draft: false
categories:
    - 教程
tags:
    - Zoterio
    - 坚果云
    - paper
---

## 坚果云解决方案

1. 注册坚果云账户，用上交点击账户，选择用户信息

![1.png](https://s2.loli.net/2021/12/15/InvWOZYlsJRuFkQ.png)


2. 在安全选项中选择添加应用，将名字命名为zotero (小写，图示有误)

![2.png](https://s2.loli.net/2021/12/15/AXifglrmkepYZqy.png)

![3.png](https://s2.loli.net/2021/12/15/vcagGz6ESQkPYr8.png)

3. 添加应用后可以看到生成了密码

![4.png](https://s2.loli.net/2021/12/15/F3eN46kUCKSIjLu.png)

5. 打开Zotero首选项，在同步中设置文件同步的方式，使用WebDAV，将URL设置为坚果云的服务器地址（即上图中坚果云示例中的服务器地址，因为这里默认是小写的zotero，所以坚果云中如果设置成大写的Zotero是不行的，大小写敏感），密码设置为上面生成的密码

![5.png](https://s2.loli.net/2021/12/15/NCy8vjxRJmKLhiX.png)

6. 因为并没有实现建立zotero文件夹，所以同步过程中会请求建立zotero文件夹

![6.png](https://s2.loli.net/2021/12/15/PCodBv5buQyOVmF.png)

同步成功后：

![7.png](https://s2.loli.net/2021/12/15/jPilBSr1EqexDmO.png)

> 使用了ZotFile对文件名进行重设置，但是好像暂时没有发现它的真实用处，这里暂时不讲，到此坚果云也可以同步Zotero的文件

## 标签设计

1. 任务： Segmentation, Classificaion, Generation ...
2. 器官： Skin, Liver, Pancreas, Protast ...
    - 包含肿瘤： Tumor
3. 方法： Geometry / Pixel / Multi-Annotation ...
4. 数据： CT / MR / Ultrasound / JPG
5. 包含了数据集： dataset
6. 包含了代码： code
7. 特定数据集上的任务： ImageNet-LT, Cifar-100-LT, MSD

## 插件

- zotero-citation 快捷引用

    > https://github.com/MuiseDestiny/zotero-citation


- zotero-pdf-translate 文献翻译

    > https://github.com/windingwind/zotero-pdf-translate