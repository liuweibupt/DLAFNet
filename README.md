# DLAFNet: Direct LiDAR-Aerial Fusion Network for Semantic Segmentation of 2D Multispectral Aerial Image and 3D LiDAR Point Cloud

## Abstract
Abstract—Semantic segmentation of high-resolution remote sensing images (RSIs) is developing rapidly. For the semantic segmentation of 2D images, various architectures based on convolutional neural networks have emerged. Nowadays, the accuracy of segmentation has been continuously improved with the introduction of transformer-based models such as SegFormer and Swin Transformer. The methods of semantic segmentation of 3D LiDAR point cloud data, e.g. PointNet and Kernel Point Convolution (KPConv), also develop rapidly due to the emergence of 3D convolution. Multispectral image (MSI) can provide rich spectral information for semantic segmentation, while 3D LiDAR point cloud data can provide depth information. Thus, the semantic segmentation accuracy could be improved by fusing multispectral images and 3D LiDAR point cloud data. The traditional aerial image and LiDAR data fusion uses the DSM or other information obtained from the LiDAR point cloud and fuses the RSIs by adding depth channels. In this paper, we propose a method titled Direct LiDAR-Aerial Fusion Network (DLAFNet) which directly uses the multispectral image and LiDAR point cloud data for semantic Segmentation tasks. In particular, since the sparse features extracted from the KPConv branch are not as essential as features from MSI, we design LiDAR Assisted Attention Module (L-AAM). Our experiments on the modified GRSS18 dataset prove that our method is proper and obtains the best results by comparing with its components and other methods.

The code will be released after the review.

## Data

We acknowledged the IEEE Geoscience and Remote Sensing Society Image Analysis and Data Fusion Technical Committee and the Hyperspectral Image Analysis Lab at the University of Houston for the GRSS18 dataset. 

The original data is available from [2018 IEEE GRSS Data Fusion Challenge – Fusion of Multispectral LiDAR and Hyperspectral Data | Hyperspectral Image Analysis Lab (uh.edu)](https://hyperspectral.ee.uh.edu/?page_id=1075). The processed 2D GRSS data can be fouond in [here](https://pan.baidu.com/s/1scYaRvgtW1fGXzZaG2aGyg?pwd=cwpo )(password for BaiduNetdisk: cwpo)

Put your data on  `DLAFNetCode\DLAFNet\configs\_base_\datasets\GRSS18_5.py`.



## Installation

Please refer to [get_started.md](docs/get_started.md) for installation



## Training

```shell
# Single-gpu training
python tools\train.py configs\dlafnet\dlafnet_mit_b0_512_80k_GRSS18_5.py
```

