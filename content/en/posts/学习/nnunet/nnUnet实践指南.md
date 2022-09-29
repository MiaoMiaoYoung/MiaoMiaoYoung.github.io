---
title: "nnunet实践指南"
date: 2021-07-19T21:57:22+08:00
draft: False
image: images/posts/nnunet.jpg
categories:
    - 学习
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
    src_image_dire = '../../data/22.06.28/image'
    src_label_dire = '../../data/22.06.28/label'
    files = get_files_name(dire=src_image_dire)

    dst_imageTr_dire = './data/imagesTr'
    dst_imageTs_dire = './data/imagesTs'
    dst_label_dire = './data/labelsTr'
    os.makedirs(dst_imageTr_dire, exist_ok=True)
    os.makedirs(dst_imageTs_dire, exist_ok=True)
    os.makedirs(dst_label_dire, exist_ok=True)

    for index, file in tqdm(enumerate(files), total=len(files)):
        image_path = os.path.join(src_image_dire, file)
        label_path = os.path.join(src_label_dire, file)

        image, param = get_medical_image(image_path)
        label, _ = get_medical_image(label_path)

        save_medical_image(image, os.path.join(dst_imageTr_dire if index < 60 else dst_imageTs_dire,
                                               'LAA_{0:03d}.nii.gz'.format(index + 1)), param)
        save_medical_image(label, os.path.join(dst_label_dire, 'LAA_{0:03d}.nii.gz'.format(index + 1)), param)
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

```
usage: nnUNet_train [-h] [-val] [-c] [-p P] [--use_compressed_data] [--deterministic] [--npz] [--find_lr] [--valbest] [--fp32] [--val_folder VAL_FOLDER] [--disable_saving]
                    [--disable_postprocessing_on_folds] [--val_disable_overwrite] [--disable_next_stage_pred] [-pretrained_weights PRETRAINED_WEIGHTS]
                    network network_trainer task fold

positional arguments:
  network
  network_trainer
  task                  can be task name or task id
  fold                  0, 1, ..., 5 or 'all'

optional arguments:
  -h, --help            show this help message and exit
  -val, --validation_only
                        use this if you want to only run the validation
  -c, --continue_training
                        use this if you want to continue a training
  -p P                  plans identifier. Only change this if you created a custom experiment planner
  --use_compressed_data
                        If you set use_compressed_data, the training cases will not be decompressed. Reading compressed data is much more CPU and RAM intensive and should only be used if you
                        know what you are doing
  --deterministic       Makes training deterministic, but reduces training speed substantially. I (Fabian) think this is not necessary. Deterministic training will make you overfit to some
                        random seed. Don't use that.
  --npz                 if set then nnUNet will export npz files of predicted segmentations in the validation as well. This is needed to run the ensembling step so unless you are developing
                        nnUNet you should enable this
  --find_lr             not used here, just for fun
  --valbest             hands off. This is not intended to be used
  --fp32                disable mixed precision training and run old school fp32
  --val_folder VAL_FOLDER
                        name of the validation folder. No need to use this for most people
  --disable_saving      If set nnU-Net will not save any parameter files (except a temporary checkpoint that will be removed at the end of the training). Useful for development when you are
                        only interested in the results and want to save some disk space
  --disable_postprocessing_on_folds
                        Running postprocessing on each fold only makes sense when developing with nnU-Net and closely observing the model performance on specific configurations. You do not
                        need it when applying nnU-Net because the postprocessing for this will be determined only once all five folds have been trained and nnUNet_find_best_configuration is
                        called. Usually running postprocessing on each fold is computationally cheap, but some users have reported issues with very large images. If your images are large
                        (>600x600x600 voxels) you should consider setting this flag.
  --val_disable_overwrite
                        Validation does not overwrite existing segmentations
  --disable_next_stage_pred
                        do not predict next stage
  -pretrained_weights PRETRAINED_WEIGHTS
                        path to nnU-Net checkpoint file to be used as pretrained model (use .model file, for example model_final_checkpoint.model). Will only be used when actually training.
                        Optional. Beta. Use with caution.
```

选择相对应的模型进行训练:

### 2D U-Net

```bash
nnUNet_train 2d nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz
```

### 3D full resolution U-Net

```bash
nnUNet_train 3d_fullres nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz
```

### 3D U-Net cascade

级联Unet需要两阶段运行

- Stage 1

    ```bash
    nnUNet_train 3d_lowres nnUNetTrainerV2 TaskXXX_MYTASK FOLD --npz
    ```

- Stage 2

    ```bash
    nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes TaskXXX_MYTASK FOLD --npz
    ```

第一阶段训练完后，RESULT_FOLDER的结果应该如下：

```
(RESULTS_FOLDER) nnUNet_trained_models
└── nnUNet
    └── 3d_lowres
        └── Task099_Organ
            └── nnUNetTrainerV2__nnUNetPlansv2.1
                ├── fold_0
                │   ├── debug.json
                │   ├── model_best.model
                │   ├── model_best.model.pkl
                │   ├── model_final_checkpoint.model
                │   ├── model_final_checkpoint.model.pkl
                │   ├── model_latest.model
                │   ├── model_latest.model.pkl
                │   ├── postprocessing.json
                │   ├── progress.png
                │   ├── training_log_2022_9_28_20_52_08.txt
                │   ├── training_log_2022_9_28_21_13_23.txt
                │   ├── training_log_2022_9_29_10_05_59.txt
                │   ├── validation_raw
                │   │   ├── Organ_004.nii.gz
                │   │   ├── Organ_009.nii.gz
                │   │   ├── Organ_014.nii.gz
                │   │   ├── Organ_017.nii.gz
                │   │   ├── summary.json
                │   │   └── validation_args.json
                │   └── validation_raw_postprocessed
                │       ├── Organ_004.nii.gz
                │       ├── Organ_009.nii.gz
                │       ├── Organ_014.nii.gz
                │       ├── Organ_017.nii.gz
                │       └── summary.json
                ├── fold_1
                |   └── ...
                ├── fold_2
                |   └── ...
                ├── fold_3
                |   └── ...
                ├── fold_4
                |   └── ...
                ├── gt_niftis
                │   ├── Organ_001.nii.gz
                │   ├── Organ_002.nii.gz
                │   ├── Organ_003.nii.gz
                │   ├── Organ_004.nii.gz
                │   ├── Organ_005.nii.gz
                │   ├── Organ_006.nii.gz
                │   ├── Organ_007.nii.gz
                │   ├── Organ_008.nii.gz
                │   ├── Organ_009.nii.gz
                │   ├── Organ_010.nii.gz
                │   ├── Organ_011.nii.gz
                │   ├── Organ_012.nii.gz
                │   ├── Organ_013.nii.gz
                │   ├── Organ_014.nii.gz
                │   ├── Organ_015.nii.gz
                │   ├── Organ_016.nii.gz
                │   ├── Organ_017.nii.gz
                │   ├── Organ_018.nii.gz
                │   ├── Organ_019.nii.gz
                │   └── Organ_020.nii.gz
                ├── plans.pkl
                └── pred_next_stage
                    ├── Organ_001_segFromPrevStage.npz
                    ├── Organ_002_segFromPrevStage.npz
                    ├── Organ_003_segFromPrevStage.npz
                    ├── Organ_004_segFromPrevStage.npz
                    ├── Organ_005_segFromPrevStage.npz
                    ├── Organ_006_segFromPrevStage.npz
                    ├── Organ_007_segFromPrevStage.npz
                    ├── Organ_008_segFromPrevStage.npz
                    ├── Organ_009_segFromPrevStage.npz
                    ├── Organ_010_segFromPrevStage.npz
                    ├── Organ_011_segFromPrevStage.npz
                    ├── Organ_012_segFromPrevStage.npz
                    ├── Organ_013_segFromPrevStage.npz
                    ├── Organ_014_segFromPrevStage.npz
                    ├── Organ_015_segFromPrevStage.npz
                    ├── Organ_016_segFromPrevStage.npz
                    ├── Organ_017_segFromPrevStage.npz
                    ├── Organ_018_segFromPrevStage.npz
                    ├── Organ_019_segFromPrevStage.npz
                    └── Organ_020_segFromPrevStage.npz
```

> 可能会出现没有 validation_raw 文件夹的情况，这个时候重新预测一遍就好了, nnUNet_train 搭配 -val 参数就可以只进行验证 （但是必须要有model_final_checkpoint.model 、 model_final_checkpoint.model.pkl 文件）


## 测试

```bash
nnUNet_predict -i nnUNet_raw_data_base/nnUNet_raw_data/Task005_Prostate/imagesTs/ -o OUTPUT_DIRECTORY -t Task005_Prostate -m 3d_fullres -f 0
```

- '-i': 输入图像路径，需要经过数据的预处理
- '-o': 生成label的输出文件夹
- '-t': 任务标号，可全称，如:Task005_Prostate
- '-m': 模型种类
- '-f': [可选]，制定交叉验证的折进行预测

-----------------------------------------------------------

## 修改nnUNet损失函数

> https://github.com/MIC-DKFZ/nnUNet/tree/master/documentation/extending_nnunet.md

- 在"nnUNet\nnunet\training\loss_functions"添加新的损失函数


"nnUNet\nnunet\training\network_training"中保留了许多的训练策略，比如 "nnUNetTrainerV2CascadeFullRes"

其中的继承关系：nnUNetTrainerV2CascadeFullRes → nnUNetTrainerV2 → nnUNetTrainer

可以看到，这个里面使用的损失函数是："from nnunet.training.loss_functions.dice_loss import DC_and_CE_loss"


