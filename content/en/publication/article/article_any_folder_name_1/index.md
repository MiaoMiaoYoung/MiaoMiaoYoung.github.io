---
keywords: ['Segmentation','Pancreas']
authors: ['MiaoMiaoYang']
publication: "abc"
abstract: "The low resolution of thick CT/MR with large spacing will lead to misdiagnosis and bring a huge difficulty to the automatic organ or lesion segmentation. Especially in automatic pancreatic tumor segmentation, due to the limitation of equipment, the tumors only exist in a few slices, and the continuity between slices of 3D CT/MR image is poor. Besides, the features of tumors, such as the size, shape, location, intensity and so on, vary dramatically according to different cases. The fuzzy boundaries of small tumors also bring great uncertainty to the segmentation task. Aiming to solve those problems, we introduce the LLE-based interpolation neural network into the pancreatic tumor segmentation task, which mainly includes the following improvements: 1) We utilize local linear embedding (LLE) to model the relationship between adjacent slices and the interpolated slice. It adapts the spatial transformation of the organ between slices. 2) Neural network, combining with the LLE module, is designed to significantly enhance the image resolution, thus can generate more continuous and clearer images for each sequence. 3) Multiscale cascade strategy is adopted in the network to reduce the influence of drastic changes in tumor size on segmentation results. Experiments are carried out in MR images with 3.5mm thickness provided by Changhai hospital, and CT images on Medical Segmentation Decathlon pancreatic tumor challenge, respectively. The results show that our proposed model has a sensitivity of 96.55% and a dice coefficient of 62.8% (±25.8%) on the MR dataset, and a dice coefficient of 50.6% (±,30.9%) on the CT dataset."
links:
 - name: url
   link: https://doi.org/10.1007/s10489-021-02847-9
copyright: "Copyright (c) 2018 zzossig"
title: "Local Linear Embedding Based Interpolation Neural Network in Pancreatic Tumor Segmentation"
ENTRYTYPE: "article"
enableToc: True
enableWhoami: True
pinned: true
publishDate: "2021-11-26"
---