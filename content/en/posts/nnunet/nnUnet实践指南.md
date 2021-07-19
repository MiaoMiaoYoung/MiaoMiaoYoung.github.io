---
title: "nnunet实践指南"
date: 2021-07-19T21:57:22+08:00
draft: False
image: images/posts/nnunet.jpg
categories:
    - work
    - code
tags:
    - 代码复现
    - 医学图像
    - 分割
    - nnunet

enableTocContent: true
---

## 数据集处理

> 官方要求在这里：https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_conversion.md

现有的数据集是按照如下目录进行排列的，其中器官标签organ文件夹和肿瘤标签文件夹tumor中的标签文件都是0-1标签文件。

```bash
data
├─image
│      image-1.nrrd
|      ......
│      image-n.nrrd
│
├─organ
│      image-1.nrrd
|      ......
│      image-n.nrrd
│
└─tumor
       image-1.nrrd
       ......
       image-n.nrrd
```

现在需要把他们转化为Decathlon数据集中的格式并创建dataset.json文件记录数据集信息：

### 数据集文件

1. 标签文件
   
    需要把之前的标签汇总到一个文件中，通过不同的值来标注不同的部分。如：0-背景；1-器官；2-肿瘤。存放标签文件的文件夹最好命名为：labelTr

    ```python
    for file in tqdm(files):
        organ_path = os.path.join(organ_dire, file)
        tumor_path = os.path.join(tumor_dire, file)
        label_path = os.path.join(label_dire, file)

        organ, param = get_medical_image(organ_path)
        tumor, _ = get_medical_image(tumor_path)

        assert organ.shape == tumor.shape

        label = np.zeros(shape=organ.shape)
        label[organ == 1] = 1
        label[tumor == 1] = 2

        save_medical_image(label, label_path, param)
    ```

2. 图像文件

    图像文件夹需要拆分训练集和测试集，分别命名为（最好）：

    训练集：imageTr；测试集：imageTs

3. 文件命名

    需要修改每一个文件的命名，格式为：Organ_XXX.nii.gz

    Organ为器官名称，如:Pancreas

    XXX表示三位不同的标识数字、

    图像格式最好是.nii.gz

    ```python 
    for index,file in tqdm(enumerate(files),total=len(files)):
        image_path = os.path.join(image_dire, file)
        label_path = os.path.join(label_dire, file)

        image,param = get_medical_image(image_path)
        label,_ = get_medical_image(label_path)

        save_medical_image(image, os.path.join(image_dire,'pancreas_{0:03d}.nii.gz'.format(index+1)),param)
        save_medical_image(label, os.path.join(label_dire,'pancreas_{0:03d}.nii.gz'.format(index+1)),param)
    ```

-------------------------------------

整理完成的数据集文件夹应该是（dataset.json文件后续生成）：

```bash
├─imagesTr
│      pancreas_001.nii.gz
|      ...
│      pancreas_899.nii.gz
│
├─imagesTs
│      pancreas_900.nii.gz
|      ...
│      pancreas_999.nii.gz
│
└─labelsTr
        pancreas_001.nii.gz
        ...
        pancreas_899.nii.gz
```

### dataset.json

数据集通过dataset.json文件来展示数据集信息，其中包含以下内容，以Task07_Pancreas为例：

```json
{ 
    "name": "Pancreas", 
    "description": "Pancreas and cancer segmentation",
    "reference": "Memorial Sloan Kettering Cancer Center ",
    "licence":"CC-BY-SA 4.0",
    "relase":"1.0 04/05/2018",
    "tensorImageSize": "3D",
    "modality": { 
        "0": "CT"
     }, 
    "labels": { 
        "0": "background", 
        "1": "pancreas", 
        "2": "cancer"
    }, 
    "numTraining": 281, 
    "numTest": 139,
    "training":[{"image":"./imagesTr/pancreas_290.nii.gz","label":"./labelsTr/pancreas_290.nii.gz"},],
    "test":["./imagesTs/pancreas_044.nii.gz",]
}
```

所以，需要对自己的数据集也生成上述的dataset.json配置文件：

```python
template = {
    "name": "Pancreas",
    "description": "Pancreas and cancer segmentation",
    "reference": "Memorial Sloan Kettering Cancer Center ",
    "licence": "CC-BY-SA 4.0",
    "relase": "1.0 04/05/2018",
    "tensorImageSize": "3D",
    "modality": {
        "0": "MR"
    },
    "labels": {
        "0": "background",
        "1": "pancreas",
        "2": "cancer"
    },
    "numTraining": 0,
    "numTest": 0,
    "training": [],
    "test": []
}

## training image
training_image_dire = './data/imagesTr/'
training_label_dire = './data/labelsTr/'
training_files = get_files_name(dire=training_image_dire)
for file in tqdm(training_files):
    template['training'].append(
        {
            "image": training_image_dire + file,
            "label": training_label_dire + file
        }
    )

## test image
test_image_dire = './data/imagesTs/'
test_files = get_files_name(dire=test_image_dire)
for file in tqdm(test_files):
    template['test'].append(test_image_dire + file)

## num
template['numTraining'] = len(training_files)
template['numTest'] = len(test_files)

save_json(template, './data/dataset.json')
```

**注意：** 模板中的"modality"等信息需要自己手动更改

### 完成

最后，将母文件夹改名为：TaskXX_Organ，如：Task07_Pancreas

## nnUNet配置

### 下载安装nnUNet

> https://github.com/MIC-DKFZ/nnUNet

按照要求下载代码并进行安装：

```python
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
pip install -e .
```

### 设置路径

一般和nnUNet文件夹平级，创建以下几个文件夹：

- nnUNet_raw_data_base：原始文件夹
  - nnUNet_raw_data: 存放原始数据
  - nnUNet_cropped_data: 用于存放预处理的数据
- nnUNet_preprocessed：预处理文件夹
- nnUNet_trained_models：模型的结果

所以文件夹结构如下：

```bash
Folder
|-- nnUNet
|   |--[Code]
|   
|-- nnUNet_preprocessed
|
|-- nnUNet_raw_data_base
|   |
|   |-- nnUNet_cropped_data
|   |
|   `-- nnUNet_raw_data
|
`-- nnUNet_trained_models

```

然后添加到系统路径中：

```bash
vim ~/.bashrc
export nnUNet_raw_data_base="/MiaoMiaoYang/nnUNet/nnUNet_raw_data_base"
export nnUNet_preprocessed="/MiaoMiaoYang/nnUNet/nnUNet_preprocessed"
export RESULTS_FOLDER="/MiaoMiaoYang/nnUNet/nnUNet_trained_models"
source ~/.bashrc # 使修改生效
```

## 转换数据集

> https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_conversion.md#how-to-use-decathlon-datasets

```bash
nnUNet_convert_decathlon_task -i FOLDER_TO_TASK_AS_DOWNLOADED_FROM_MSD -p NUM_PROCESSES
```

其中：

- FOLDER_TO_TASK_AS_DOWNLOADED_FROM_MSD：为下载后Decathlon数据集的路径，如：Task05_Prostate，并且它的id是两位数的
- NUM_PROCESSES：预处理的进程

```bash
nnUNet_convert_decathlon_task -i /MiaoMiaoYang/data/Task99_Pancreas -p 8
```

数据集转换之后，该文件夹为：

```bash
Folder
|-- nnUNet
|   |--[Code]
|   
|-- nnUNet_preprocessed
|
|-- nnUNet_raw_data_base
|   |
|   |-- nnUNet_cropped_data
|   |
|   `-- nnUNet_raw_data
|       |
|       `-- Task099_Pancreas
|           |
|           |-- dataset.json
|           |
|           |-- imagesTr
|           |   |-- pancreas_001_0000.nii.gz
|           |   |-- ........................
|           |   `-- pancreas_899_0000.nii.gz
|           |
|           |-- imagesTs
|           |   |-- pancreas_900_0000.nii.gz
|           |   |-- ........................
|           |   `-- pancreas_999_0000.nii.gz
|           |
|           `-- labelsTr
|               |-- pancreas_001.nii.gz
|               |-- ...................
|               `-- pancreas_899.nii.gz
|
`-- nnUNet_trained_models
```

## 数据进行预处理

```bash
nnUNet_plan_and_preprocess -t XXX --verify_dataset_integrity
```

- 数据必须得放置在正确的文件夹：

    nnUNet_raw_data_base/nnUNet_raw_data/TaskXXX_MYTASK

- XXX标识了需要进行预处理的id

    ```bash
    nnUNet_plan_and_preprocess -t 099 --verify_dataset_integrity
    ```

预处理后的文件会放在文件夹nnUNet_preprocessed下：

```bash
Folder
|-- nnUNet
|   |--[Code]
|   
|-- nnUNet_preprocessed
|   |
|   `-- Task099_Pancreas
|       |
|       |-- dataset.json
|       |
|       |-- dataset_properties.pkl
|       |
|       |-- gt_segmentations
|       |
|       |   |-- pancreas_001.nii.gz
|       |   |-- ...................
|       |   `-- pancreas_899.nii.gz
|       |
|       |-- nnUNetData_plans_v2.1_2D_stage0
|       |   |-- pancreas_001.npz
|       |   |-- pancreas_001.pkl
|       |   |-- ................
|       |   |-- ................
|       |   |-- pancreas_899.npz
|       |   `-- pancreas_899.pkl
|       |
|       |-- nnUNetData_plans_v2.1_stage0
|       |   |-- pancreas_001.npz
|       |   |-- pancreas_001.pkl
|       |   |-- ................
|       |   |-- ................
|       |   |-- pancreas_899.npz
|       |   `-- pancreas_899.pkl
|       |
|       |-- nnUNetData_plans_v2.1_stage1
|       |   |-- pancreas_001.npz
|       |   |-- pancreas_001.pkl
|       |   |-- ................
|       |   |-- ................
|       |   |-- pancreas_899.npz
|       |   `-- pancreas_899.pkl
|       |
|       |-- nnUNetPlansv2.1_plans_2D.pkl
|       |
|       `-- nnUNetPlansv2.1_plans_3D.pkl
|
|-- nnUNet_raw_data_base
|   |
|   |-- nnUNet_cropped_data
|   |   |
|   |   `-- Task099_Pancreas
|   |       |
|   |       |-- dataset.json
|   |       |
|   |       |-- dataset_properties.pkl
|   |       |
|   |       |-- gt_segmentations
|   |       |   |
|   |       |   |-- pancreas_001.nii.gz
|   |       |   |-- ...................
|   |       |   `-- pancreas_024.nii.gz
|   |       |
|   |       |-- pancreas_001.npz
|   |       |-- pancreas_001.pkl
|   |       |-- ................
|   |       |-- ................
|   |       |-- pancreas_899.npz
|   |       `-- pancreas_899.pkl
|   |
|   `-- nnUNet_raw_data
|       |
|       |-- Task099_Pancreas
|       |   |
|       |   |-- dataset.json
|       |   |
|       |   |-- imagesTr
|       |   |   |
|       |   |   |-- pancreas_001_0000.nii.gz
|       |   |   |-- ........................
|       |   |   `-- pancreas_899_0000.nii.gz
|       |   |   
|       |   |-- imagesTs
|       |   |   |
|       |   |   |-- pancreas_900_0000.nii.gz
|       |   |   |-- ........................
|       |   |   `-- pancreas_999_0000.nii.gz
|       |   |
|       |   `-- labelsTr
|       |       |
|       |       |-- pancreas_001.nii.gz
|       |       |-- ...................
|       |       `-- pancreas_899.nii.gz

`-- nnUNet_trained_models
    `-- nnUNet
```

## 训练

> 参考：https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/training_example_Hippocampus.md

```bash
nnUNet_train CONFIGURATION TRAINER_CLASS_NAME TASK_NAME_OR_ID FOLD  --npz (additional options)
```

### 2D U-Net

```bash
nnUNet_train 2d nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz
```

### 3D full resolution U-Net

```bash
nnUNet_train 3d_fullres nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz
```

### 3D U-Net cascade

```bash
nnUNet_train 3d_lowres nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz

#############################

nnUNet_train 3d_lowres nnUNetTrainerV2 Task099_Pancreas 0 --npz
```

- FOLD：表示了第几折的交叉验证

```bash
nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes TaskXXX_MYTASK FOLD --npz
```