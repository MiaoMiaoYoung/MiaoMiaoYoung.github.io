---
title: "MITK安装教程 21.09.05"
date: 2021-09-05T11:02:33+08:00
draft: false
categories:
    - 教程
tags:
    - MITK
    - VS2019
    - QT
    - CMake
    - docker

enableTocContent: true
---

> **没有什么是重装一次电脑解决不了问题的**

> 之前在B站上传过一次视频，但是太早，了，很多东西都忘记了。正好机器重装了一下系统，详细记录一下这次的MITK安装过程。（

{{< bilibili BV1Bs411F7eS >}}

## VS2019安装

### 下载Visual Studio Installer安装包

> https://visualstudio.microsoft.com/zh-hans/downloads/

Visual Studio 现在统一由安装包进行管理，下载之后点击之后，可以选择要安装的内容：

![1.jpg](https://i.loli.net/2021/09/02/dovlVAkp4cja3PX.jpg)

> 社区版足够满足日常需求。专业和企业版的功能更偏向团队合作以及一些专业开发。

### Visual Studio 安装

1. 选择**使用C++的桌面开发**，安装C++基本环境

    ![2.jpg](https://i.loli.net/2021/09/02/Vx1uYN9pG4l3fZC.jpg)

    > 在选择**使用C++的桌面开发**之后，右边框安装的详细信息中便会显示具体的安装内容

2. 在单个组件中，勾选"C++/CLI支持"

    ![3.jpg](https://i.loli.net/2021/09/02/7LEBX6yh1txHjY4.jpg)

    勾选之后可能增加的不光是"C++/CLI支持"这一个组件，可能包含了上游组件，比如图中的".NET Framework XXX"，不要去掉勾选，留着就行。
    
3. 选择安装位置

    最好保持默认的C:系统盘的位置不要改变。
    ![4.jpg](https://i.loli.net/2021/09/02/rjlVQIE1JXUG2y9.jpg)

    ![5.jpg](https://i.loli.net/2021/09/02/VvcfkUFPCXlA4aN.jpg)

    > 因为我的主力语言现在不是C，C:在固态上，容量小，所以尽量把不经常用的东西搞到F:机械盘上。
    >
    > 但是这个在后面就遇到了Windows Kits安装在F:/下，而不是指定的F:/install/下的问题。
    >
    > 所以，后面无奈又卸载了Windows SDK，重新下载安装了SDK进行安装：

    ![8.jpg](https://i.loli.net/2021/09/02/9wTsEkiqfcSt1Kr.jpg)

    ![9.jpg](https://i.loli.net/2021/09/02/hXbsYM4B5lRPUi9.jpg)

    ![10.jpg](https://i.loli.net/2021/09/02/Eqldv65GA2jenmV.jpg)

    ![12.jpg](https://i.loli.net/2021/09/02/eY5LKyHFkCOjupg.jpg)

    > **注意**，正常步骤中，SDK安装的选项中不包含 "Debugging Tools for Windows"，所以需要下面的第三步进行更改配置，添加这一必需选项

    ![15.jpg](https://i.loli.net/2021/09/02/VHL2vwSC1f4tegT.jpg)

    ![16.jpg](https://i.loli.net/2021/09/02/A6yIuFgjeX8ovCx.jpg)

### Windows SDK配置

> 如果不是为了安装MITK，仅为了安装VS2019可以不用设置Windows SDK
> 上回书说道，我因为更改了安装位置，所以导致Windows Kits安装位置不对，所以卸载重新安装了一下，在安装过程中配置好了，这里就不需要再添加了。所以这里简单演示一下配置流程，重要是安装上Debugging Tools for Windows.

1. 控制面板中找到Windows Software Development kit

    ![17.jpg](https://i.loli.net/2021/09/02/CvmRbTDIOJsow2n.jpg)

2. 点中SDK右键选择更改

3. 选择更改

    ![18.jpg](https://i.loli.net/2021/09/02/GE2iX9BpFzOTD6Z.jpg)

4. 勾选"Debugging Tools for Windows"后点击 "Change"

    ![19.jpg](https://i.loli.net/2021/09/02/KfTU12rMq5aoVEI.jpg)

### VS2019 测试

1. 打开VS2019后，点击创建新项目：

    ![20.jpg](https://i.loli.net/2021/09/02/NYE7xOo98C5X12A.jpg)

2. 选择"空项目"，下一步

    ![21.jpg](https://i.loli.net/2021/09/02/HdcX7rUkeZnGMDC.jpg)

3. 配置新项目，选择项目位置，下一步

    ![22.jpg](https://i.loli.net/2021/09/02/rlywAeUhGSuNOo4.jpg)

4. "源文件"右键，选择添加→新建项

    ![23.jpg](https://i.loli.net/2021/09/02/gF1tbhf97UeNzmT.jpg)

    ![24.jpg](https://i.loli.net/2021/09/02/ldqtp5JsoRbhEzK.jpg)

5. 经典Hello一下world

    ![25.jpg](https://i.loli.net/2021/09/02/O1eRK8liwn2yV5D.jpg)

## CMake安装

跟着操作一步一步来就好

![1.png](https://i.loli.net/2021/09/02/ni6uTvZbePthz31.png)
![2.png](https://i.loli.net/2021/09/02/cyIWZl4oVi1CSgX.png)
![3.png](https://i.loli.net/2021/09/02/hazrx1QXI27vUpY.png)
![4.png](https://i.loli.net/2021/09/02/UZCBGW67cXtTnSa.png)
![5.png](https://i.loli.net/2021/09/02/H6Q2MfP95wRtySv.png)
![6.png](https://i.loli.net/2021/09/02/gvwOlRy9ue8VQfh.png)
![7.png](https://i.loli.net/2021/09/02/AesxEaQMzKSPgnT.png)


## QT安装

### 离线安装和在线安装

1. 可以采用下载离线安装包的方式，方便快捷一些。但是在5.15版本之后，QT不再提供离线安装，所以最新版本的只更新到了5.14版本

    > https://download.qt.io/archive/qt/

    ![1.png](https://i.loli.net/2021/09/02/cg1oSbuyT8EXajG.png)
    ![2.png](https://i.loli.net/2021/09/02/tWOZjcSXUqNRm61.png)
    ![3.png](https://i.loli.net/2021/09/02/kgjcoM9Y5iF4dON.png)

2. 使用在线安装包，可以使用清华镜像站来下载在线安装包

    > https://mirrors.tuna.tsinghua.edu.cn/qt/official_releases/online_installers/

    ![5.png](https://i.loli.net/2021/09/02/hBsICQR5NWJFDpZ.png)

    **这里使用的是这种方式**

---------------------------------------------------------

### 在线安装步骤

> 注意，这里在安装MITK过程中走了弯路，因为MITK目前只支持到QT5.12.9，而我之前安装成了QT6
> 并且，因为QT5.15才支持MSVC2019，所以这里最终选择的QT版本是**QT5.15**

1. 首先需要提供一个QT账户，这里注册一下就好
 
![6.png](https://i.loli.net/2021/09/02/x1oGhe5unQ3Kcrk.png)

2. 个人用户使用

![7.png](https://i.loli.net/2021/09/02/9WBL6FHm2gGlPZo.png)

3. 下一步

![8.png](https://i.loli.net/2021/09/02/Hef3EsJzlMXx75D.png)
![9.png](https://i.loli.net/2021/09/02/JZoK31BHzIn5rYh.png)

4. 选择安装路径，并关联主要格式 

![10.png](https://i.loli.net/2021/09/02/DRM5OFfXJZzE2cs.png)

5. 选择安装包

> 这里是QT6版本的安装，但是不适合MITK
![11.png](https://i.loli.net/2021/09/02/s5Yhy3WwLQzf1Fj.png)

> 这里是QT5.15版本的安装，配合MITK
![36.png](https://i.loli.net/2021/09/02/hIYWEZJDLTVMjgQ.png)

------------------------------

![37.png](https://i.loli.net/2021/09/02/m376qBJPNl4AcO8.png)
下面中默认选择了CMake和Ninjia，这里因为之前自己安装了CMake，所以就不需要了，取消勾选了这两项

6. 下一步
   
![13.png](https://i.loli.net/2021/09/02/mItWUgcQKJTi5SO.png)
![14.png](https://i.loli.net/2021/09/02/5u4BSQhmRFTDHsw.png)
![15.png](https://i.loli.net/2021/09/02/DiXhzdfsNtHpG85.png)


7. QT安装完成

![18.png](https://i.loli.net/2021/09/02/4zhIRZ1DgQuM5XB.png)

8. 配置系统环境变量

![40.png](https://i.loli.net/2021/09/02/SipjoO1l2hFeKwa.png)

### VS2019+QT

1. 建一个新的VS2019空项目，找到 “扩展” → “管理扩展”

![19.png](https://i.loli.net/2021/09/02/dHBgLfMOECRUsyc.png)

2. 在联机中搜索QT，找到官方扩展包“QT Visual Studio Tools”，选择下载

![20.png](https://i.loli.net/2021/09/02/GXPqf2hkRioUHer.png)

3. 下载完毕后，关闭VS2019**所有**窗口后，扩展自动开始安装

![21.png](https://i.loli.net/2021/09/02/bEtGLIpsmHFl4aP.png)
 
![22.png](https://i.loli.net/2021/09/02/gMQidZu8LHx9Gh7.png)
![23.png](https://i.loli.net/2021/09/02/1LC4xfmhklqoEHV.png)
![24.png](https://i.loli.net/2021/09/02/rxERYoMAHag7e8D.png)
![25.png](https://i.loli.net/2021/09/02/CiLrGN1WzshOXE9.png)

4. 安装完成后，需要对QT扩展进行设置。打开一个VS2019空项目。“扩展” → “Qt VS Tools” → “Options”

![26.png](https://i.loli.net/2021/09/02/tWDUmFwJgKdj19X.png)

“Qt” → “Versions” → 点击加号增加一个空的Qt版本 → 点击Path一栏，找到目标QT版本中的bin/qmake.exe选中，Version自动填充

![38.png](https://i.loli.net/2021/09/02/hZmMUXiAI7SFeDO.png)
![39.png](https://i.loli.net/2021/09/02/YvSiAMb2OXrt3UH.png)

### 测试

1. 创建新项目中选择 “Qt Widgets Applications”

![28.png](https://i.loli.net/2021/09/02/JvLTC2dM9ioZPYr.png)

2. 配置项目名称和位置

![29.png](https://i.loli.net/2021/09/02/NALWxX6EQmpPbcM.png)

3. 下一步

![30.png](https://i.loli.net/2021/09/02/xleIEdU3MjVw4Jz.png)

4. 这里只是为了测试，就仅选择了DEBUG模式
![31.png](https://i.loli.net/2021/09/02/cQypA5VuvYi94ws.png)

5. 下一步
![32.png](https://i.loli.net/2021/09/02/MU7aGhbYNOnzWHg.png)

6. 直接运行即可，可以弹出一个程序框，安装成功

![35.png](https://i.loli.net/2021/09/02/HAymi1bG2KqRkOM.png)


## MITK安装

### 下载MITK源码

在MITK的Github仓库中下载MITK源码，这里选择的使用git进行下载，也可以直接在网站中选择下载.zip压缩包

![36.png](https://i.loli.net/2021/09/05/OhC18q7pMmykZr2.png)
![38.png](https://i.loli.net/2021/09/05/7IbCJOQ392GSyMt.png)

下载（解压）后的MITK文件夹示意图

![39.png](https://i.loli.net/2021/09/05/iUJ38epShB7InRx.png)

### CMake构建MITK项目

1. MITK使用的是CMake的超级构建技术，所以打开CMake：

   - "Where is the source code:" 选择MITK源码所在的文件夹。（即上图中所示解压后的MITK文件夹）

   - "Where to build the binaries:" 选择将要构建MITK源码的文件夹。（这个文件夹可以是还没有新建的，之后会让新建）

![40.png](https://i.loli.net/2021/09/05/vCKhn6WmDG24f5R.png)


2. 选择好源码所在的路径和构建的目录之后，点击"Configure"进行第一次设置

![41.png](https://i.loli.net/2021/09/05/ujAiDlVLzpvr4PF.png)

3. 因为之前选择的"Where to build the binaries:"文件夹还没有被新建出来，所以这里提示是否新建，肯定新建

![42.png](https://i.loli.net/2021/09/05/I4d5jqoc7xEeg8p.png)

4. 这里选择生成器，因为我们之前是安装的VS2019，所以选择2019的这个

![43.png](https://i.loli.net/2021/09/05/y83DXjg2OhYcLvx.png)

5. 平台选择x64平台

![44.png](https://i.loli.net/2021/09/05/6fmpqvViNM9UyH1.png)

---------------------------------------------------------

**第一次Configure后**

可以看到提示报错了，报错信息是无法下载patch.exe，以前没遇到这个错，所以先不管他，继续下面的操作：

6. 勾选上面的Grouped和Advanced，将CMake条目按组显示并显示高级的设置选项

![45.png](https://i.loli.net/2021/09/05/ZkyjtBadsQvNTl9.png)

7. 在MITK目录下，勾选**MITK_BUILD_ALL_PLUGINS**和**MITK_BUILD_EXAMPLES**。表示安装MITK中所有的插件和案例，建议勾选，没有需求也可以不用勾选。

![46.png](https://i.loli.net/2021/09/05/eRAXaM4PtYKnk32.png)
![47.png](https://i.loli.net/2021/09/05/uJZVnK2MGLYoSe3.png)

8. 在MITK目录下，勾选**MITK_USE_Python3**，表示构建MITK中相关的Python3插件，其中提供了MITK官方的Python调用方法，如果没有Python相关需求的可以不用勾选。

![48.png](https://i.loli.net/2021/09/05/KABMG8NZta5hCrq.png)

9. 在CMAKE目录下，将CMAKE_INSTALL_PREFIX设置为相关路径，如果不使用编译包进行安装的话，可以省略这一步，其实就是为C盘节省一些空间

![49.png](https://i.loli.net/2021/09/05/BzYoSZAfLpemxCO.png)

10. 再次点击 "Configure"

---------------------------------------------------------

**第贰次Configure后**

![50.png](https://i.loli.net/2021/09/05/nyOEpl8USCQLvI9.png)

没有报错了，但是因为之前的勾选了一些新项目，所以还有一些红色背景的条目，所以再次点击**Configure**进行设置

---------------------------------------------------------

**第③次Configure后**

![51.png](https://i.loli.net/2021/09/05/5Yi9WBvkRLnE6lK.png)

没有报错，并且没有红色背景的待选项，所以可以点击**Generate**进行项目的生成

![52.png](https://i.loli.net/2021/09/05/2Ls4zWpKNhgm6nf.png)

项目生成后，可以直接点击**Open Project**打开项目，其实就是打开了构建项目中的**MITK-superbuild.sln**


```
20>F:\install\MITK\MITK\Modules\Core\src\DataManagement\mitkSlicedGeometry3D.cpp(1,1): error C2220: 以下警告被视为错误 [F:\install\MITK\MITK-build\MITK-build\Modules\Core\MitkCore.vcxproj]
20>F:\install\MITK\MITK\Modules\Core\src\DataManagement\mitkSlicedGeometry3D.cpp(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 [F:\install\MITK\MITK-build\MITK-build\Modules\Core\MitkCore.vcxproj]
```


```
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmiod/modsopcommon.h(1,1): error C2220: 以下警告被视为错误 (编译源文件 F:\install\MITK\MITK\Modules\Multilabel\autoload\DICOMSegIO\mitkDICOMSegmentationIO.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\Multilabel\autoload\DICOMSegIO\MitkDICOMSegIO.vcxproj]
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmiod/modsopcommon.h(1,1): error C2220: 以下警告被视为错误 (编译源文件 F:\install\MITK\MITK\Modules\Multilabel\autoload\DICOMSegIO\mitkDICOMQIIOActivator.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\Multilabel\autoload\DICOMSegIO\MitkDICOMSegIO.vcxproj]
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmiod/modsopcommon.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 (编译源文件 F:\install\MITK\MITK\Modules\Multilabel\autoload\DICOMSegIO\mitkDICOMSegmentationIO.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\Multilabel\autoload\DICOMSegIO\MitkDICOMSegIO.vcxproj]
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmiod/modsopcommon.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 (编译源文件 F:\install\MITK\MITK\Modules\Multilabel\autoload\DICOMSegIO\mitkDICOMQIIOActivator.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\Multilabel\autoload\DICOMSegIO\MitkDICOMSegIO.vcxproj]
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmseg/segment.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 (编译源文件 F:\install\MITK\MITK\Modules\Multilabel\autoload\DICOMSegIO\mitkDICOMSegmentationIO.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\Multilabel\autoload\DICOMSegIO\MitkDICOMSegIO.vcxproj]
```


```
20>F:\install\MITK\MITK-build\ep\include\boost/spirit/home/support/char_encoding/iso8859_1.hpp(1,1): error C2220: 以下警告被视为错误 (编译源文件 F:\install\MITK\MITK\Modules\ModelFit\src\Common\mitkFormulaParser.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\ModelFit\MitkModelFit.vcxproj]
20>F:\install\MITK\MITK-build\ep\include\boost/spirit/home/support/char_encoding/iso8859_1.hpp(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 (编译源文件 F:\install\MITK\MITK\Modules\ModelFit\src\Common\mitkFormulaParser.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\ModelFit\MitkModelFit.vcxproj]
```


```
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmseg/segment.h(1,1): error C2220: 以下警告被视为错误 (编译源文件 F:\install\MITK\MITK\Modules\DICOMPM\autoload\DICOMPMIO\mitkDICOMPMIO.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\DICOMPM\autoload\DICOMPMIO\MitkDICOMPMIO.vcxproj]
20>F:\install\MITK\MITK-build\ep\include\dcmtk/dcmseg/segment.h(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 (编译源文件 F:\install\MITK\MITK\Modules\DICOMPM\autoload\DICOMPMIO\mitkDICOMPMIO.cpp) [F:\install\MITK\MITK-build\MITK-build\Modules\DICOMPM\autoload\DICOMPMIO\MitkDICOMPMIO.vcxproj]
```

```
20>F:\install\MITK\MITK\Modules\Core\test\mitkAffineTransformBaseTest.cpp(1,1): error C2220: 以下警告被视为错误 [F:\install\MITK\MITK-build\MITK-build\Modules\Core\test\MitkCoreTestDriver.vcxproj]
20>F:\install\MITK\MITK\Modules\Core\test\mitkAffineTransformBaseTest.cpp(1,1): warning C4819: 该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失 [F:\install\MITK\MITK-build\MITK-build\Modules\Core\test\MitkCoreTestDriver.vcxproj]

```

### 编译MITK项目

这里等待的时间会非常漫长，而且会报很多错

1. 打开项目后，直接Ctrl+F5进行编译。（这期间可以通过VS2019上面的搜索，搜索“错误”，打开“错误列表”）

![53.png](https://i.loli.net/2021/09/05/kNsWFflIrumzhEi.png)

2. 第一次编译出错

![54.png](https://i.loli.net/2021/09/05/9MNE8X6RKbYv7n1.png)

在错误列表中，“警告”不用管，只管“错误”就行（MITK本身的警告级别很高，其实有一些错误可以在CMake中降低警告等级就不会报错了，但是这里还是没有手动调整CMake的警告等级）

![55.png](https://i.loli.net/2021/09/05/mXdebnxY5giWzkB.png)

可以看到，这次编译时因为一些包没有下载好导致的，所以切换一下网络，再次进行Ctrl+F5进行编译

3. 第二次编译出错

在错误列表中可以看到，**“以下警告视为错误”**，但是我们不知道是什么警告，所以双击这个错误，然后切换到**输出**，就可以看到在编译过程中的警告提示

![57.png](https://i.loli.net/2021/09/05/L6FPSmKEYNJ1CUp.png)

这个警告是经常遇到的一个警告：**该文件包含不能在当前代码页表示的字符**

其实就是编译过程中，这个文件的字符集不符合编译要求，所以只要把这个文件改一下编码方式就行，我一般改成的是GBK。

![58.png](https://i.loli.net/2021/09/05/mFoVhJkNg6ZbeMa.png)

在VS2019中这个文件的标签中，点击右键，可以打开这个文件所在的位置，然后我这里是通过VSCode进行更换字符集的

![59.png](https://i.loli.net/2021/09/05/LoDySrndmN9lgpk.png)
![60.png](https://i.loli.net/2021/09/05/YsWUrAGpXN6otBl.png)
![61.png](https://i.loli.net/2021/09/05/1JrPWKwmx5zlp9N.png)

更改好之后再次进行Ctrl+F5进行编译

4. 第三-五次次编译出错

这次非常幸运没有出现其他的报错，大部分报错都是之前的字符集不符合要求，所以按照之前的步骤更改了字符集就可以

![63.png](https://i.loli.net/2021/09/05/7ambGd4qtMyfIB3.png)
![69.png](https://i.loli.net/2021/09/05/5BqIjgvfxmA6zhu.png)
![73.png](https://i.loli.net/2021/09/05/mWjEKx4wc3Uu2JS.png)

5. 编译成功

当出现这个提示的时候，就**说明编译成功了**

![76.png](https://i.loli.net/2021/09/05/ZCnfEbQeuUK19vP.png)

因为这里的编译项目是左边栏中的“ALL_BUILD”，他只是负责构建项目，并没有进行打开，所以会提示无法启动程序

![77.png](https://i.loli.net/2021/09/05/SsjvEg3KTOm6HVG.png)

在 XXX/MITK-build/MITK-build/bin 中，找到 startMitkWorkBench_debug.bat，双击打开，可以打开编译好之后的MITK

![78.png](https://i.loli.net/2021/09/05/Mb98heUIlykj31p.png)

通过Window打开Show View，可以看到比.exe多得多的插件

![79.png](https://i.loli.net/2021/09/05/YeQ7PKHoyzfFEAD.png)


6. Release版本

之前默认编译的是DEBUG，是方便开发的版本，之后的如果要在此基础上进行开发，那就需要Release进行最后的封装，所以这里也顺便编译了一下Release版本

![80.png](https://i.loli.net/2021/09/05/SnWEVLxvfP8Jq6c.png)

就是将之前的DEBUG x64改为了Release x64，其中的报错和之前一样，这里就不重复了
