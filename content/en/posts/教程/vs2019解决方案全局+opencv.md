---
title: "opencv：vs2019下的全局配置"
date: 2021-03-11T11:02:33+08:00
draft: false
categories:
    - 教程
tags:
    - vs2019
    - code
    - vs
    - opencv
---

## Opencv的安装

1. 官网 https://opencv.org/ 下载opencv安装包：opencv-XXX.exe

2. 双击运行安装包，选择安装目录，点击Extract进行下一步。(其实就是解压)

![1.png](https://i.loli.net/2021/07/24/K9mHI5fxk2ezipX.png)
![2.png](https://i.loli.net/2021/07/24/lOESZWBgIb7urGJ.png)

提取之后，目标文件夹文件如图所示：

![3.png](https://i.loli.net/2021/07/24/vnz24T6eGWx1yCh.png)

3. 配置环境变量

右键单击“我的电脑” → 属性 → 高级系统设置 → 环境变量，（win10系统可直接在搜索框中输入“环境变量”）

![4.png](https://i.loli.net/2021/07/24/qNglLKTsjRbhtSi.png)

> 库巴鸭桑！

找到环境变量，选中Path变量，单击编辑

![5.jpg](https://i.loli.net/2021/07/24/P4CxYw9BqZLhUkl.jpg)

单击浏览，选中” (opencv在你电脑中的安装位置)/opencv/build/x64/vc15/bin”，点击确定

![6.jpg](https://i.loli.net/2021/07/24/iApHf1NJLoMrCq3.jpg)

**配置完成**

## Opencv的VS2019全局环境配置

> 这里目的在于配置解决方案的VS2019全局配置，这样可以直接导入每个学生的项目，不需要再对每一个学生配置环境，直接运行即可

### 创建一个空项目

![7.jpg](https://i.loli.net/2021/07/24/7JUl95aRAijsPo6.jpg)

创建一个空项目，不赘述了

### 配置全局设置

“视图” → “属性管理器”

![8.jpg](https://i.loli.net/2021/07/24/ZgSkTHFQBOqWvYa.jpg)

打开之后如下图所示：

![9.jpg](https://i.loli.net/2021/07/24/iYs6LkXKnSQ8vAO.jpg)

如果是对某一个项目进行设置，可以直接对项目名右键属性，进行设置。

或是对某一个模态进行设置，比如"DEBUG|x64"

--------------------------------------

但是我们现在想的对所有的项目进行设置，所以点击上面的黑色小扳手图标进行全局设置

![10.jpg](https://i.loli.net/2021/07/24/DKZMVu8XtCvyTkm.jpg)

### Opencv的配置

1. VC++目录 → 包含目录

    ![](./images/11.jpg)

    ```
    F:\install\opencv\opencv\build\include
    F:\install\opencv\opencv\build\include\opencv
    F:\install\opencv\opencv\build\include\opencv2
    ```

2. VC++目录 → 库目录

    ![](./images/12.jpg)

    ```
    F:\install\opencv\opencv\build\x64\vc15\lib
    ```

3. 链接器 → 输入 → 附加依赖项

    填入库目录 (F:\install\opencv\opencv\build\x64\vc15\lib) 中的两个.lib，以d结尾的为DEBUG模式下的附加依赖项

    ```
    opencv_world341.lib
    opencv_world341d.lib
    ```

![](./images/15.jpg)

直接导入学生的项目即可

**完成！**

> 学生一般使用DEBUG模式进行练习，所以在直接导入项目 .vcxproj 文件时，项目的DEBUG设置会盖过全局设置，成为学生电脑上的设置
> 这个时候使用release模式就可以，直接批判成绩即可



