---
title: "Work Note"
date: 2022-07-12T11:16:18+08:00
draft: false
categories:
    - 教程
tags:
    - python
    - code    
---


## Mathjax

{{< mathjax >}}



## 平滑一组数据 (Smooth)

```python
from scipy.ndimage import gaussian_filter1d
import numpy as np
gaussian_filter1d([1.0, 2.0, 3.0, 4.0, 5.0], 1)
gaussian_filter1d([1.0, 2.0, 3.0, 4.0, 5.0], 4)
import matplotlib.pyplot as plt
np.random.seed(280490)
x = np.random.randn(101).cumsum()
y3 = gaussian_filter1d(x, 3)
y6 = gaussian_filter1d(x, 6)
plt.plot(x, 'k', label='original data')
plt.plot(y3, '--', label='filtered, sigma=3')
plt.plot(y6, ':', label='filtered, sigma=6')
plt.legend()
plt.grid()
plt.show()
```

## CUDA 乱杀

###

实验环境不知道为啥又崩溃了，导入torch的时候显示没有gpu

```python
import torch
# /opt/conda/lib/python3.7/site-packages/torch/cuda/__init__.py:83: UserWarning: CUDA initialization: CUDA driver initialization failed, you might not have a CUDA gpu. (Triggered internally at  /opt/conda/conda-bld/pytorch_1656352464346/work/c10/cuda/CUDAFunctions.cpp:109.)
#   return torch._C._cuda_getDeviceCount() > 0
```

试了好久没有办法，最后从之前的images新建了container发现还是一样的问题，然后觉得应该是images损坏了，开始下载对应新的images

```bash
# host 主机是cuda10.1 nvcc Cuda compilation tools, release 7.5, V7.5.17，这里就选择了最接近的
sudo docker pull pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel
```

但是下载之后问题又来了...

> https://developer.nvidia.com/zh-cn/blog/updating-the-cuda-linux-gpg-repository-key/
> 
> 为了最好地确保 RPM 和 Debian 软件包存储库的安全性和可靠性， NVIDIA 从 2022 年 4 月 27 日开始更新并轮换apt、dnf/yum和zypper软件包管理器使用的签名密钥。

导致Dockerfile自动构建镜像的时候没有办法通过密钥...

```bash
# 将以下命令中的$distro/$arch替换为适合您的操作系统的值；例如：
# debian10/x86_64
# debian11/x86_64
# ubuntu1604/x86_64
# ubuntu1804 / cross linux sbsa
# ubuntu1804 / ppc64el
# Ubuntu 1804 / sbsa
# ubuntu1804/x86_64
# ubuntu2004 / cross linux sbsa
# Ubuntu 2004 / sbsa
# ubuntu2004/x86_64
# Ubuntu 2204 / sbsa
# ubuntu2204/x86_64
# wsl-ubuntu/x86_64

wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
```

但是酱紫还是不行...

```bash
apt-get update
# E: Conflicting values set for option Signed-By regarding source https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /: /usr/share/keyrings/cuda-archive-keyring.gpg !=
# E: The list of sources could not be read.
```

> https://forums.developer.nvidia.com/t/the-repository-https-developer-download-nvidia-com-compute-cuda-repos-ubuntu1804-x86-64-release-is-not-signed/193764/13


既然酱紫，就把对应的库删了吧

```bash
$ cat /etc/apt/sources.list.d/cuda.list 
# deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /
$ rm /etc/apt/sources.list.d/cuda.list
$ apt update
# Get:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease [1575 B]
# Hit:2 http://archive.ubuntu.com/ubuntu bionic InRelease                                                                                                  
# Hit:3 http://security.ubuntu.com/ubuntu bionic-security InRelease                                                              
# Ign:4 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease
# Get:5 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Packages [709 kB]
# Hit:6 http://archive.ubuntu.com/ubuntu bionic-updates InRelease               
# Hit:7 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release
# Hit:8 http://archive.ubuntu.com/ubuntu bionic-backports InRelease                               
# Err:9 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release.gpg
#   The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F60F4B3D7FA2AF80
# Fetched 709 kB in 2s (397 kB/s)
# Reading package lists... Done
# Building dependency tree       
# Reading state information... Done
# 25 packages can be upgraded. Run 'apt list --upgradable' to see them.
# W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F60F4B3D7FA2AF80
# W: Failed to fetch https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/Release.gpg  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F60F4B3D7FA2AF80
# W: Some index files failed to download. They have been ignored, or old ones used instead.
$ cat /etc/apt/sources.list.d/nvidia-ml.list 
# deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /
$ rm /etc/apt/sources.list.d/nvidia-ml.list
$ apt update
# Hit:1 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease
# Hit:2 http://security.ubuntu.com/ubuntu bionic-security InRelease                                                                
# Hit:3 http://archive.ubuntu.com/ubuntu bionic InRelease                                                
# Hit:4 http://archive.ubuntu.com/ubuntu bionic-updates InRelease
# Hit:5 http://archive.ubuntu.com/ubuntu bionic-backports InRelease
# Reading package lists... Done
# Building dependency tree       
# Reading state information... Done
# 25 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

解决！

### RuntimeError: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED

torch.cuda.is_available()健在的情况下

有可能...就是没显存了

在nvidia-smi上监控一下显存的使用情况，有可能程序自动会多卡，有一张显存占用就不行的情况


## 项目结构

- 项目名称 [e.g. Geometry-based Segmentation]

    - 数据集名称 [e.g. MSD_Liver]

        - data

            数据集数据，最好统一格式: image / label ...


        - code

            - 版本号 [e.g. v1]

        - contrast [对比实验]

            - 对比实验名称



