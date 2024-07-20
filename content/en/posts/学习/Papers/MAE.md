---
title: "MAE is all you need"
date: 2023-04-19T15:01:38+08:00
draft: false
categories:
    - 学习
    - work
    - paper
    - mae

libraries:
- katex

enableTocContent: true
---

## Mask Autoencoder 

MAE想法很简单，很有效，很牛逼，这里主要讨论一些实现细节，以官方代码为准

### ViT (models_mae.py
)

MAE的ViT和原版ViT还是有点区别，这里主要讲区别:

- 位置编码：

    原版的ViT使用了一个可学习的向量来表示位置

    MAE使用了固定的sin-cos编码，这里其实就比较能理解，毕竟为了复原图像，肯定需要知道每个Patch在哪里
