---
title: "MITK插件教程 21.09.05"
date: 2021-09-05T11:02:33+08:00
draft: false
categories:
    - 教程
tags:
    - MITK

enableTocContent: true
---

> **通过编译好的MITK生成自己的插件**

> MITK提供了两种不同的编写方式，一种是生成自己的应用，一种是作为插件嵌套在MITK中，这里介绍的是插件形式
> 
> https://docs.mitk.org/nightly/index.html

## 生成MITK插件

> (不知道为啥现在的MITK不编译生成 MitkPluginGenerator.exe 了，但是不要紧，我们有以前的MitkPluginGenerator还可以用

```bash
MitkPluginGenerator.exe ^
-plugin-symbolic-name org.commontk.tagA.tagB ^
-view-name "View Name" ^
-project-name "Project_Name" ^
-project-app-name "App_Name" ^
-o DIR
```

- plugin-symbolic-name: 插件的唯一标识符，因为是MITK之外的插件，所以前两个org.commontk标识不能动，TagA习惯上定义为器官，TagB习惯上定义为功能
- view-name: 插件在MITK中显示的名称（可以带空格）
- project-name: 项目名称，不能带空格等特殊字符，用于编程时的项目名称
- project-app-name: 项目中的App名称，一般和上面设置成一样的
- o: 插件源码生成的位置

Example:

```
MitkPluginGenerator.exe ^
-plugin-symbolic-name org.commontk.organ.cad ^
-view-name "Tooth CAD" ^
-project-name "ToothCAD" ^
-project-app-name "ToothCAD" ^
-o D:\
```

![1.png](https://i.loli.net/2021/09/05/Ofb3LvU7IPF8BXq.png)

生成的插件源码文件夹如下图所示

![2.png](https://i.loli.net/2021/09/05/q1fil5NKEDt3ysY.png)

## CMake构建MITK插件项目

1. 构建MITK插件项目

    打开CMake，同MITK编译道理相同

   - "Where is the source code:" 设置成源码位置
   - "Where to build the binaries:" 设置成项目构建位置

    ![3.png](https://i.loli.net/2021/09/05/5p7zBlMfTm8YUj3.png)

    点击Configure进行第一次设置，编译器选择VS2019，平台选择x64

2. **添加MITK路径**

    因为已经编译好了MITK，所以这里直接导入就行了，如果不添加MITK路径，这个插件首先会自己下载MITK重新先进行一遍MITK的编译

    ![4.png](https://i.loli.net/2021/09/05/h2nuT6bU3RKEZsL.png)

    MITK的额外路径设置为：XXX/MITK-build/MITK-build/

    ![5.png](https://i.loli.net/2021/09/05/xH1T6nWUgpI8lus.png)

3. 配置其他插件

    因为插件需要使用Python，所以这里勾选Python选项，如果还有其他需求则勾选其他选项。

    ![6.png](https://i.loli.net/2021/09/05/cVioSy5AaqFzpLv.png)

    配置好后进行"Configure"

4. 这里需要检查一下
    
    需要检查一下新增的红色背景的选项是不是填入了相应位置，特别是Python的路径，容易找不到

    ![7.png](https://i.loli.net/2021/09/05/893EUu5XnjRCm6K.png)

    ![8.png](https://i.loli.net/2021/09/05/uYmUls3zBb7MROC.png)

    再进行一次"Configure"


5. 全部配置好后，进行"Generate"生成

    ![9.png](https://i.loli.net/2021/09/05/a8uVDAQF7Jmi1hE.png)
    
    通过"Open Projects"打开VS2019项目

## VS2019进行构建

1. 同MITK编译时相同，这个项目是超级编译的项目，Ctrl+F5进行编译，将项目构建出来

    ![10.png](https://i.loli.net/2021/09/05/31Frivd7VbXSyz6.png)

2. 这里报错：**无法打开文件“OpenMP::OpenMP_CXX.lib”**
   
   OpenMP是VS自带的多线程编译，这里打不开是因为CMake没有识别到。所以需要重写一下CMakeLists.txt

   在C/CXX Flags中加入OpenMP相关选项

   ```cmake
   #-----------------------------------------------------------------------------
   # Set C/CXX Flags
   #-----------------------------------------------------------------------------

   find_package(OpenMP)
   set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
   ```

   重写CMakeLists.txt后，需要删除之前项目，重新通过CMake构建MITK插件项目

3. 报错：**LNK1104无法打开文件“Qt5::WebEngine.lib”**

    ![14.png](https://i.loli.net/2021/09/05/JywHSU3sNB7CM1i.png)

    虽然有问题，但是可以看到，这里的XX/ToodCAD-build文件夹已经生成，并且生成了ToothCAD.sln

    ![15.png](https://i.loli.net/2021/09/05/nY2m5AHTuZB76cN.png)

    ToothCAD-superbuild.sln是超级构建的项目，但是里面没有具体代码

    ToothCAD.sln中包含着咱们一般熟悉的项目

    ![16.png](https://i.loli.net/2021/09/05/OTQiBKgMILb1tkU.png)

    其中：
    
    - **org_commonth_organ_cad**中包含着实际的代码，所以修改这个项目中的代码就行
    - **ToothCAD**设置为启动项目

    右键**ToothCAD**，打开属性，在链接器 → 输入 → 附加依赖项中，删除**Qt5::WebEngine.lib**一项

    Ctrl+F5进行编译

4. 编译完成

![17.png](https://i.loli.net/2021/09/05/cTg1N5nlryCiS9X.png)

可以在插件中找到自己生成的插件ToothCAD
