---
title: "MITK学习笔记"
date: 2022-01-09T11:02:33+08:00
draft: false
categories:
    - 教程
tags:
    - MITK

enableTocContent: true
---


## Step1

学习MITK基本的框架，导入一张2D图片的方法

- 在最开始，需要登记一个独立的Qmitk的全局实例，即：
  ```C++
  // Register Qmitk-dependent global instances
  QmitkRegisterClasses()
  ```
  头文件：***QmitkRegisterClasses.h***


- 第一步：基本的初始化：
  创建一个数据储存(DataStorage)，这个数据储存可以操作所有的数据项目，他被渲染机制用来渲染所有的数据项目。头文件：***mitkStandaloneDataStorage.h***
  ```C++
  // Create a DataStorage
  // The DataStorage manages all data objects. It is used by the
  // rendering mechanism to render all data objects
  // We use the standard implementation mitk::StandaloneDataStorage.
  mitk::StandaloneDataStorage::Pointer ds = mitk::StandaloneDataStorage::New();
  ```

- 第二步：数据载入
  载入数据节点：例如：图像格式、表层格式。
  ```C++
  // Load datanode (eg. many image formats, surface formats, etc.)
  mitk::IOUtil::Load(String FilePath,mitk::StandaloneDataStorage DataStorage/**ds*/);
  ```

- 第三步：创建一个窗口并将数据储存传送给他
  - 创建一个渲染窗口，头文件：***QmitkRenderWindow.h***
    ```C++
    // Create a RenderWindow
    QmitkRenderWindow renderWindow;
    ```
  - 告诉这个渲染窗口哪一个数据储存需要渲染，头文件：***QmitkRenderWindow.h***
    ```C++
    // Tell the RenderWindow which (part of) the datastorage to render
    renderWindow.GetRenderer()->SetDataStorage(ds);
    ```
  - 初始化这个渲染窗口
    ```C++
    // Initialize the RenderWindow
    auto geo = ds->ComputeBoundingGeometry3D(ds->GetAll());
    //ds->GetAll()：返回DataStorage中所有的数据 返回：SetOfObjects::ConstPointer
    //ds->ComputeBoundingGeometry3D：计算输入数据与轴平行的几何边界 返回：mitk::TimeGeometry::Pointer 
    mitk::RenderingManager::GetInstance()->InitializeViews(geo);
    ```
  -  选择一个切片
      ```C++
      mitk::SliceNavigationController::Pointer sliceNaviController = renderWindow.GetSliceNavigationController();
      if (sliceNaviController)
        sliceNaviController->GetSlice()->SetPos(0);
      ```

- 第四步：Qt显示
  ```C++
  renderWindow.show();
  renderWindow.resize(256, 256);
  ```

<br>

源码：[..\MITK\Examples\Tutorial\Step1]
```C++
/*===================================================================

The Medical Imaging Interaction Toolkit (MITK)

Copyright (c) German Cancer Research Center,
Division of Medical and Biological Informatics.
All rights reserved.

This software is distributed WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.

See LICENSE.txt or http://www.mitk.org for details.

===================================================================*/

#include "QmitkRegisterClasses.h"
#include "QmitkRenderWindow.h"

#include <mitkStandaloneDataStorage.h>

#include <QApplication>
#include <itksys/SystemTools.hxx>

#include <mitkIOUtil.h>

//##Documentation
//## @brief Load image (nrrd format) and display it in a 2D view
int main(int argc, char *argv[])
{
  QApplication qtapplication(argc, argv);

  if (argc < 2)
  {
    fprintf(stderr, "Usage:   %s [filename] \n\n", itksys::SystemTools::GetFilenameName(argv[0]).c_str());
    return 1;
  }

  // Register Qmitk-dependent global instances
  QmitkRegisterClasses();

  //*************************************************************************
  // Part I: Basic initialization
  //*************************************************************************

  // Create a DataStorage
  // The DataStorage manages all data objects. It is used by the
  // rendering mechanism to render all data objects
  // We use the standard implementation mitk::StandaloneDataStorage.
  mitk::StandaloneDataStorage::Pointer ds = mitk::StandaloneDataStorage::New();

  //*************************************************************************
  // Part II: Create some data by reading a file
  //*************************************************************************

  // Load datanode (eg. many image formats, surface formats, etc.)
  mitk::IOUtil::Load(argv[1], *ds);

  //*************************************************************************
  // Part IV: Create window and pass the datastorage to it
  //*************************************************************************

  // Create a RenderWindow
  QmitkRenderWindow renderWindow;

  // Tell the RenderWindow which (part of) the datastorage to render
  renderWindow.GetRenderer()->SetDataStorage(ds);

  // Initialize the RenderWindow
  auto geo = ds->ComputeBoundingGeometry3D(ds->GetAll());
  mitk::RenderingManager::GetInstance()->InitializeViews(geo);
  // mitk::RenderingManager::GetInstance()->InitializeViews();

  // Select a slice
  mitk::SliceNavigationController::Pointer sliceNaviController = renderWindow.GetSliceNavigationController();
  if (sliceNaviController)
    sliceNaviController->GetSlice()->SetPos(0);

  //*************************************************************************
  // Part V: Qt-specific initialization
  //*************************************************************************
  renderWindow.show();
  renderWindow.resize(256, 256);

// for testing
#include "../QtTesting.h"
  if (strcmp(argv[argc - 1], "-testing") != 0)
    return qtapplication.exec();
  else
    return QtTesting();

  // cleanup: Remove References to DataStorage. This will delete the object
  ds = nullptr;
}
/**
\example Step1.cpp
*/

```

## Step2

在 <a href=".\MITK-1.md">Step1</a> 导入一张图片的基础上，学习导入多张图片

- 第二步：数据载入（多个图片）
  ```C++
  for (int i = 1; i < argc; ++i)
  {
    // For testing
    if (strcmp(argv[i], "-testing") == 0)
      continue;

    //*********************************************************************
    // Part III: Put the data into the datastorage
    //*********************************************************************
    // Add the node to the DataStorage
    mitk::IOUtil::Load(argv[i], *ds);
  }
  ```

  其余步骤相同


## Step3

在 <a href=".\MITK-1.md">Step1</a> 导入一张2D图片的基础上，学习导入一张3D图片，3D图片其实就是很多2D图片的叠加，之后经过渲染形成的

- 第二步：导入图片
  
  - 将图片数据导入到DataStorage，并且用指针进行指向，装载数据节点
    ```C++
    // Load datanode (eg. many image formats, surface formats, etc.)
    mitk::StandaloneDataStorage::SetOfObjects::Pointer dataNodes = mitk::IOUtil::Load(argv[i], *ds);
    ```

  - 判断数据节点是否为空，如果为空则报错
    ```C++
    if (dataNodes->empty())
    {
      fprintf(stderr, "Could not open file %s \n\n", argv[i]);
      exit(2);
    }
    ```

  - 抓取数据树(DataTree)的节点
    ```C++
    mitk::DataNode::Pointer node = dataNodes->at(0);
    ```

- 第三步：将所有的图片进行体渲染
  
  - 创建一个图片指针
    ```C++
    mitk::Image::Pointer image = dynamic_cast<mitk::Image *>(node->GetData());
    ```

  - 检查图片是否为空：***image.IsNotNull()***
   
  - 将DataTree的节点设置为进行体渲染
    ```C++
    // Set the property "volumerendering" to the Boolean value "true"
    node->SetProperty("volumerendering", mitk::BoolProperty::New(true));
    ```

  - 创建一个传递函数，分配视觉的一些参数（如：色彩，不透明度）给这些灰度值数据,***体重建***
    ```C++
    // Create a transfer function to assign optical properties (color and opacity) to grey-values of the data
    mitk::TransferFunction::Pointer tf = mitk::TransferFunction::New();
    tf->InitializeByMitkImage(image);
    ```

    - 设置色彩传递函数的RGB值
      颜色传递函数主要是确定体素的颜色值或灰度值, 由类vtkColorTransferFunction实现
      ```C++
      // Set the color transfer function AddRGBPoint(double x, double r, double g, double b)
      tf->GetColorTransferFunction()->AddRGBPoint(tf->GetColorTransferFunction()->GetRange()[0], 1.0, 0.0, 0.0);
      tf->GetColorTransferFunction()->AddRGBPoint(tf->GetColorTransferFunction()->GetRange()[1], 1.0, 1.0, 0.0);
      //x代表体素点的灰度值, r代表红色分量, g代表绿色分量, b代表蓝色分量, 他们的范围均为( 0, 1)，0代表完全, 1代表完全不
      ```
    
    - 设置不透明度传递函数
      不透明度传递函数主要是确定各体素的不透明度, 由vtkPieceWiseFunction来设置, vtkPieceWiseFunction定义了分段函数映射,由AddPoint()和AddSegment()实现数值点的添加
      ```C++
      // Set the piecewise opacity transfer function AddPoint(double x, double y)
      tf->GetScalarOpacityFunction()->AddPoint(0, 0);
      tf->GetScalarOpacityFunction()->AddPoint(tf->GetColorTransferFunction()->GetRange()[1], 1);
      //x代表体素的灰度值, y代表该体素点的透明度, 其范围为[0,1],0代表完全透明,1代表完全不透明。
      ```

  - 将传递函数的设置导入到DataTree的节点
    ```C++
    node->SetProperty("TransferFunction", mitk::TransferFunctionProperty::New(tf.GetPointer()));
    ```
  - 完整代码：
    ```C++
    // Check if the data is an image by dynamic_cast-ing the data
    // contained in the node. Warning: dynamic_cast's are rather slow,
    // do not use it too often!
    mitk::Image::Pointer image = dynamic_cast<mitk::Image *>(node->GetData());
    if (image.IsNotNull())
    {
      // Set the property "volumerendering" to the Boolean value "true"
      node->SetProperty("volumerendering", mitk::BoolProperty::New(true));

      // Create a transfer function to assign optical properties (color and opacity) to grey-values of the data
      mitk::TransferFunction::Pointer tf = mitk::TransferFunction::New();
      tf->InitializeByMitkImage(image);

      // Set the color transfer function AddRGBPoint(double x, double r, double g, double b)
      tf->GetColorTransferFunction()->AddRGBPoint(tf->GetColorTransferFunction()->GetRange()[0], 1.0, 0.0, 0.0);
      tf->GetColorTransferFunction()->AddRGBPoint(tf->GetColorTransferFunction()->GetRange()[1], 1.0, 1.0, 0.0);

      // Set the piecewise opacity transfer function AddPoint(double x, double y)
      tf->GetScalarOpacityFunction()->AddPoint(0, 0);
      tf->GetScalarOpacityFunction()->AddPoint(tf->GetColorTransferFunction()->GetRange()[1], 1);

      node->SetProperty("TransferFunction", mitk::TransferFunctionProperty::New(tf.GetPointer()));
    }
    ```
- 第四步：将渲染窗口作为一个3D视图
  ```C++
  // Create a renderwindow
  QmitkRenderWindow renderWindow;

  // Tell the renderwindow which (part of) the datastorage to render
  renderWindow.GetRenderer()->SetDataStorage(ds);

  // Use it as a 3D view!
  renderWindow.GetRenderer()->SetMapperID(mitk::BaseRenderer::Standard3D);

  // Reposition the camera to include all visible actors
  renderWindow.GetRenderer()->GetVtkRenderer()->ResetCamera();
  ``` 
  
源码：[..\MITK\Examples\Tutorial\Step3]
```C++
/*===================================================================

The Medical Imaging Interaction Toolkit (MITK)

Copyright (c) German Cancer Research Center,
Division of Medical and Biological Informatics.
All rights reserved.

This software is distributed WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.

See LICENSE.txt or http://www.mitk.org for details.

===================================================================*/

#include "QmitkRegisterClasses.h"
#include "QmitkRenderWindow.h"

#include <mitkIOUtil.h>
#include <mitkProperties.h>
#include <mitkRenderingManager.h>
#include <mitkStandaloneDataStorage.h>
#include <mitkTransferFunction.h>
#include <mitkTransferFunctionProperty.h>

#include <itksys/SystemTools.hxx>

#include <QApplication>

//##Documentation
//## @brief Change the type of display to 3D
//##
//## As in Step2, load one or more data sets (many image, surface
//## and other formats), but display it in a 3D view.
//## The QmitkRenderWindow is now used for displaying a 3D view, by
//## setting the used mapper-slot to Standard3D.
//## Since volume-rendering is a (rather) slow procedure, the default
//## is that images are not displayed in the 3D view. For this example,
//## we want volume-rendering, thus we switch it on by setting
//## the Boolean-property "volumerendering" to "true".
int main(int argc, char *argv[])
{
  QApplication qtapplication(argc, argv);
  if (argc < 2)
  {
    fprintf(
      stderr, "Usage:   %s [filename1] [filename2] ...\n\n", itksys::SystemTools::GetFilenameName(argv[0]).c_str());
    return 1;
  }

  // Register Qmitk-dependent global instances
  QmitkRegisterClasses();

  //*************************************************************************
  // Part I: Basic initialization
  //*************************************************************************

  // Create a DataStorage
  mitk::StandaloneDataStorage::Pointer ds = mitk::StandaloneDataStorage::New();

  //*************************************************************************
  // Part II: Create some data by reading files
  //*************************************************************************
  int i;
  for (i = 1; i < argc; ++i)
  {
    // For testing
    if (strcmp(argv[i], "-testing") == 0)
      continue;

    //*********************************************************************
    // Part III: Put the data into the datastorage
    //*********************************************************************
    // Load datanode (eg. many image formats, surface formats, etc.)
    mitk::StandaloneDataStorage::SetOfObjects::Pointer dataNodes = mitk::IOUtil::Load(argv[i], *ds);

    if (dataNodes->empty())
    {
      fprintf(stderr, "Could not open file %s \n\n", argv[i]);
      exit(2);
    }
    mitk::DataNode::Pointer node = dataNodes->at(0);

    // *********************************************************
    // ********************* START OF NEW PART 1 (Step 3a) *****
    // *********************************************************

    //*********************************************************************
    // Part IV: We want all images to be volume-rendered
    //*********************************************************************

    // Check if the data is an image by dynamic_cast-ing the data
    // contained in the node. Warning: dynamic_cast's are rather slow,
    // do not use it too often!
    mitk::Image::Pointer image = dynamic_cast<mitk::Image *>(node->GetData());
    if (image.IsNotNull())
    {
      // Set the property "volumerendering" to the Boolean value "true"
      node->SetProperty("volumerendering", mitk::BoolProperty::New(true));

      // Create a transfer function to assign optical properties (color and opacity) to grey-values of the data
      mitk::TransferFunction::Pointer tf = mitk::TransferFunction::New();
      tf->InitializeByMitkImage(image);

      // Set the color transfer function AddRGBPoint(double x, double r, double g, double b)
      tf->GetColorTransferFunction()->AddRGBPoint(tf->GetColorTransferFunction()->GetRange()[0], 1.0, 0.0, 0.0);
      tf->GetColorTransferFunction()->AddRGBPoint(tf->GetColorTransferFunction()->GetRange()[1], 1.0, 1.0, 0.0);

      // Set the piecewise opacity transfer function AddPoint(double x, double y)
      tf->GetScalarOpacityFunction()->AddPoint(0, 0);
      tf->GetScalarOpacityFunction()->AddPoint(tf->GetColorTransferFunction()->GetRange()[1], 1);

      node->SetProperty("TransferFunction", mitk::TransferFunctionProperty::New(tf.GetPointer()));
    }

    // *********************************************************
    // ******************* END OF NEW PART 1 (Step 3a) *********
    // *********************************************************
  }

  //*************************************************************************
  // Part V: Create window and pass the tree to it
  //*************************************************************************

  // Create a renderwindow
  QmitkRenderWindow renderWindow;

  // Tell the renderwindow which (part of) the datastorage to render
  renderWindow.GetRenderer()->SetDataStorage(ds);

  // *********************************************************
  // ****************** START OF NEW PART 2 (Step 3b) ********
  // *********************************************************
  // Use it as a 3D view!
  renderWindow.GetRenderer()->SetMapperID(mitk::BaseRenderer::Standard3D);

  // Reposition the camera to include all visible actors
  renderWindow.GetRenderer()->GetVtkRenderer()->ResetCamera();

  // *********************************************************
  // ******************* END OF NEW PART 2 (Step 3b) *********
  // *********************************************************

  //*************************************************************************
  // Part VI: Qt-specific initialization
  //*************************************************************************
  renderWindow.show();
  renderWindow.resize(256, 256);

  mitk::RenderingManager::GetInstance()->RequestUpdateAll();

// for testing
#include "../QtTesting.h"
  if (strcmp(argv[argc - 1], "-testing") != 0)
    return qtapplication.exec();
  else
    return QtTesting();
}

/**
\example Step3.cpp
*/

```

## Step4

在 <a href=".\MITK-3.md">Step3</a> 导入一张3D图片的基础上，学习增加多个不同的视图（轴向及矢向），以及展示一个滑轮选项

- 创建Qt页面布局，以及3D渲染窗
  ```C++
  QWidget toplevelWidget;
  QHBoxLayout layout;
  layout.setSpacing(2);
  layout.setMargin(0);
  toplevelWidget.setLayout(&layout);

  // Create a renderwindow
  QmitkRenderWindow renderWindow(&toplevelWidget);
  layout.addWidget(&renderWindow);

  // Tell the renderwindow which (part of) the datastorage to render
  renderWindow.GetRenderer()->SetDataStorage(ds);

  // Use it as a 3D view
  renderWindow.GetRenderer()->SetMapperID(mitk::BaseRenderer::Standard3D);

  // Reposition the camera to include all visible actors
  renderWindow.GetRenderer()->GetVtkRenderer()->ResetCamera();
  ```

- 2D的滑轮效果（以轴面[axial]）
  - 创建一个基于类QmitkRenderWindow的滑片类QmitkSliceWideget，他额外提供了滑片选项
    ```C++
    // Create QmitkSliceWidget, which is based on the class
    // QmitkRenderWindow, but additionally provides sliders
    QmitkSliceWidget view2(&toplevelWidget);
    layout.addWidget(&view2);
    view2.SetLevelWindowEnabled(true);
    // Tell the QmitkSliceWidget which (part of) the tree to render.
    // By default, it slices the data axially
    view2.SetDataStorage(ds);
    ```
  - 从DataStorage中取出一张图片，并且通过这个图片预测他的轴面
    ```C++
    // Get the image from the data storage. A predicate (mitk::NodePredicateBase)
    // is used to get only nodes of the type mitk::Image.
    mitk::DataStorage::SetOfObjects::ConstPointer rs = ds->GetSubset(mitk::TNodePredicateDataType<mitk::Image>::New());

    view2.SetData(rs->Begin(), mitk::SliceNavigationController::Axial);
    ```
  - 在2D中看到切片的位置，并将它显示在3D中
    ```C++
    // We want to see the position of the slice in 2D and the
    // slice itself in 3D: add it to the datastorage!
    ds->Add(view2.GetRenderer()->GetCurrentWorldPlaneGeometryNode());
    ```
  
## Step5

在 <a href=".\MITK-4.md">Step4</a> 多个不同的视图（轴向及矢向）的基础上，增加人机交互

- 页面布局之后，增加交互选项
  注意：渲染器已经知道了他们的DataStorage，因为在渲染窗口注册数据交互(DataInteractors)已经自动完成了，并且只有基础的渲染器和DataStorage互相知道的情况下才会工作。

  - 创造设置点并且为他增加一个数据节点
    ```C++
    // Create PointSet and a node for it
    mitk::PointSet::Pointer pointSet = mitk::PointSet::New();
    mitk::DataNode::Pointer pointSetNode = mitk::DataNode::New();
    ```
  - 将这个数据节点增加到DataTree中
    ```C++
    // Add the node to the tree
    ds->Add(pointSetNode);
    ```
  - 创造设置点与数据的交互器
    ```C++
    // Create PointSetDataInteractor
    mitk::PointSetDataInteractor::Pointer interactor = mitk::PointSetDataInteractor::New();
    ```
  - 设置状态机模式来描述交互流
    ```C++
    // Set the StateMachine pattern that describes the flow of the interactions
    interactor->LoadStateMachine("PointSet.xml");
    ```
  - 设置配置文件
    配置文件用来描述用户出发行为的交互行为，在 ***PointSetConfig.xml*** 中 ***SHIFT+LeftClick*** 触发增加点的行为
    ```C++
    // Set the configuration file, which describes the user interactions that trigger actions
    // in this file SHIFT + LeftClick triggers add Point, but by modifying this file,
    // it could as well be changes to any other user interaction.
    interactor->SetEventConfig("PointSetConfig.xml");
    ```
  - 将数据节点增加到交互器中
    ```C++
    // Assign the pointSetNode to the interactor,
    // alternatively one could also add the DataInteractor to the pointSetNode using the SetDataInteractor() method.
    interactor->SetDataNode(pointSetNode);
    ```


## Step6

在 <a href=".\MITK-5.md">Step5</a> 人机交互的基础上，使用区域增长

- 基本类Step6，集成QWidget
  ```C++
  class Step6 : public QWidget
  {
    Q_OBJECT

    public:

    //构造、析构函数
    Step6(int argc, char* argv[], QWidget* parent=nullptr);
    ~Step6(){};

    //初始化函数，外界调用此函数进行操作
    virtual void Initialize();

    //外界交互，得到阈值的最小值、最大值
    virtual int GetThresholdMin();
    virtual int GetThresholdMax();

    protected:

    //装载数据
    void Load(int argc, char* argv[]);

    //设置窗口
    virtual void SetupWidget();

    //区域增长函数，声明为友元
    template <typename TPixel, unsigned int VImageDimension>
    friend void RegionGrowing(itk::Image<TPixel, VImageDimension> *itkImage, Step6 *step6);

    //变量
    mitk::StandaloneDataStorage::Pointer m_DataStorage;

    mitk::Image::Pointer m_FirstImage;
    mitk::Image::Pointer m_ResultImage;

    mitk::PointSet::Pointer m_Seeds;
    mitk::DataNode::Pointer m_ResultNode;

    //Qt槽函数，信号函数
    public slots:
    virtual void StartRegionGrowing();
  }
  ```
- 装载数据函数 ***Step6::Load()***
  ``` C++
  void Step6::Load(int argc, char *argv[])
  {
    //**********************************************************************
    // Part I: Basic initialization
    //**********************************************************************
  
    m_DataStorage = mitk::StandaloneDataStorage::New();
  
    //**********************************************************************
    // Part II: Create some data by reading files
    //**********************************************************************
    int i;
    for (i = 1; i < argc; ++i)
    {
      // For testing
      if (strcmp(argv[i], "-testing") == 0)
        continue;
  
      // Load datanode (eg. many image formats, surface formats, etc.)
      mitk::StandaloneDataStorage::SetOfObjects::Pointer dataNodes =   mitk::IOUtil::Load(argv[i], *m_DataStorage);
  
      if (dataNodes->empty())
      {
        fprintf(stderr, "Could not open file %s \n\n", argv[i]);
        exit(2);
      }
  
      mitk::Image::Pointer image = dynamic_cast<mitk::Image *>(dataNodes->at  (0)->GetData());
      if ((m_FirstImage.IsNull()) && (image.IsNotNull()))
        m_FirstImage = image;
    }
  }
  ```

- 设置窗口函数 ***Step6::SetupWidgets()***
  ```C++
  void Step6::SetupWidgets()
  {
    //*************************************************************************
    // Part I: Create windows and pass the datastorage to it
    //*************************************************************************
  
    // Create toplevel widget with vertical layout
    QVBoxLayout *vlayout = new QVBoxLayout(this);
    vlayout->setMargin(0);
    vlayout->setSpacing(2);
  
    // Create viewParent widget with horizontal layout
    QWidget *viewParent = new QWidget(this);
    vlayout->addWidget(viewParent);
  
    QHBoxLayout *hlayout = new QHBoxLayout(viewParent);
    hlayout->setMargin(0);
    hlayout->setSpacing(2);
  
    //*************************************************************************
    // Part Ia: 3D view
    //*************************************************************************
  
    // Create a renderwindow
    QmitkRenderWindow *renderWindow = new QmitkRenderWindow(viewParent);
    hlayout->addWidget(renderWindow);
  
    // Tell the renderwindow which (part of) the tree to render
    renderWindow->GetRenderer()->SetDataStorage(m_DataStorage);
  
    // Use it as a 3D view
    renderWindow->GetRenderer()->SetMapperID(mitk::BaseRenderer::Standard3D);
  
    // Reposition the camera to include all visible actors
    renderWindow->GetRenderer()->GetVtkRenderer()->ResetCamera();
  
    //*************************************************************************
    // Part Ib: 2D view for slicing axially
    //*************************************************************************
  
    // Create QmitkSliceWidget, which is based on the class
    // QmitkRenderWindow, but additionally provides sliders
    QmitkSliceWidget *view2 = new QmitkSliceWidget(viewParent);
    hlayout->addWidget(view2);
  
    // Tell the QmitkSliceWidget which (part of) the tree to render.
    // By default, it slices the data axially
    view2->SetDataStorage(m_DataStorage);
    mitk::DataStorage::SetOfObjects::ConstPointer rs = m_DataStorage->GetAll();
    view2->SetData(rs->Begin(), mitk::SliceNavigationController::Axial);
  
    // We want to see the position of the slice in 2D and the
    // slice itself in 3D: add it to the tree!
    m_DataStorage->Add(view2->GetRenderer()->GetCurrentWorldPlaneGeometryNode());
  
    //*************************************************************************
    // Part Ic: 2D view for slicing sagitally
    //*************************************************************************
  
    // Create QmitkSliceWidget, which is based on the class
    // QmitkRenderWindow, but additionally provides sliders
    QmitkSliceWidget *view3 = new QmitkSliceWidget(viewParent);
    hlayout->addWidget(view3);
  
    // Tell the QmitkSliceWidget which (part of) the tree to render
    // and to slice sagitally
    view3->SetDataStorage(m_DataStorage);
    view3->SetData(rs->Begin(), mitk::SliceNavigationController::Sagittal);
  
    // We want to see the position of the slice in 2D and the
    // slice itself in 3D: add it to the tree!
    m_DataStorage->Add(view3->GetRenderer()->GetCurrentWorldPlaneGeometryNode());
  
    //*************************************************************************
    // Part II: handle updates: To avoid unnecessary updates, we have to
    //*************************************************************************
    // define when to update. The RenderingManager serves this purpose, and
    // each RenderWindow has to be registered to it.
    /* mitk::RenderingManager *renderingManager = mitk::RenderingManager::GetInstance();
     renderingManager->AddRenderWindow( renderWindow );
     renderingManager->AddRenderWindow( view2->GetRenderWindow() );
     renderingManager->AddRenderWindow( view3->GetRenderWindow() ); */
  }
  ```
- 区域增长函数
  ```C++
  void RegionGrowing(itk::Image<TPixel, VImageDimension> *itkImage, Step6*step6)
  {
    typedef itk::Image<TPixel, VImageDimension> ImageType;
  
    typedef float InternalPixelType;
    typedef itk::Image<InternalPixelType, VImageDimension>InternalImageType;
  
    mitk::BaseGeometry *geometry = step6->m_FirstImage->GetGeometry();
  
    // create itk::CurvatureFlowImageFilter for smoothing and set itkImageas input
    typedef itk::CurvatureFlowImageFilter<ImageType, InternalImageType>CurvatureFlowFilter;
    typename CurvatureFlowFilter::Pointer smoothingFilter =CurvatureFlowFilter::New();
  
    smoothingFilter->SetInput(itkImage);
    smoothingFilter->SetNumberOfIterations(4);
    smoothingFilter->SetTimeStep(0.0625);
  
    // create itk::ConnectedThresholdImageFilter and set filtered image asinput
    typedef itk::ConnectedThresholdImageFilter<InternalImageType,ImageType> RegionGrowingFilterType;
    typedef typename RegionGrowingFilterType::IndexType IndexType;
    typename RegionGrowingFilterType::Pointer regGrowFilter =RegionGrowingFilterType::New();
  
    regGrowFilter->SetInput(smoothingFilter->GetOutput());
    regGrowFilter->SetLower(step6->GetThresholdMin());
    regGrowFilter->SetUpper(step6->GetThresholdMax());
  
    // convert the points in the PointSet m_Seeds (in world-coordinates) to
    // "index" values, i.e. points in pixel coordinates, and add these asseeds
    // to the RegionGrower
    mitk::PointSet::PointsConstIterator pit, pend =step6->m_Seeds->GetPointSet()->GetPoints()->End();
    IndexType seedIndex;
    for (pit = step6->m_Seeds->GetPointSet()->GetPoints()->Begin(); pit !=pend; ++pit)
    {
      geometry->WorldToIndex(pit.Value(), seedIndex);
      regGrowFilter->AddSeed(seedIndex);
    }
  
    regGrowFilter->GetOutput()->Update();
    mitk::Image::Pointer mitkImage = mitk::Image::New();
    mitk::CastToMitkImage(regGrowFilter->GetOutput(), mitkImage);
  
    if (step6->m_ResultNode.IsNull())
    {
      step6->m_ResultNode = mitk::DataNode::New();
      step6->m_DataStorage->Add(step6->m_ResultNode);
    }
    step6->m_ResultNode->SetData(mitkImage);
    // set some additional properties
    step6->m_ResultNode->SetProperty("name", mitk::StringProperty::Ne("segmentation"));
    step6->m_ResultNode->SetProperty("binary", mitk::BoolProperty::Ne(true));
    step6->m_ResultNode->SetProperty("color", mitk::ColorProperty::New(1.0 0.0, 0.0));
    step6->m_ResultNode->SetProperty("volumerendering",mitk::BoolProperty::New(true));
    step6->m_ResultNode->SetProperty("layer", mitk::IntProperty::New(1));
    mitk::LevelWindowProperty::Pointer levWinProp =mitk::LevelWindowProperty::New();
    mitk::LevelWindow levelwindow;
    levelwindow.SetAuto(mitkImage);
    levWinProp->SetLevelWindow(levelwindow);
    step6->m_ResultNode->SetProperty("levelwindow", levWinProp);
  
    step6->m_ResultImage = static_cast<mitk::Image *(step6->m_ResultNode->GetData());
  } //RegionGrowing()
  ```
  
