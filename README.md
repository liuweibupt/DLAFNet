# DLAFNet: Direct LiDAR-Aerial Fusion Network for Semantic Segmentation of 2D Aerial Image and 3D LiDAR Point Cloud

## Abstract
Semantic segmentation of high-resolution remote sensing images (RSIs) is developing rapidly. For the semantic segmentation of 2D images, various architectures based on convolutional neural networks have emerged. Nowadays, the accuracy of segmentation has been continuously improved with the introduction of transformer-based models such as SegFormer and Swin Transformer. The methods of semantic segmentation of 3D LiDAR point cloud data, e.g. PointNet and Kernel Point Convolution (KPConv), also develop rapidly due to the emergence of 3D convolution. Multispectral image (MSI) can provide rich spectral information for semantic segmentation, while 3D LiDAR point cloud data can provide depth information. Thus, the semantic segmentation accuracy could be improved by fusing multispectral images and 3D LiDAR point cloud data. The traditional aerial image and LiDAR data fusion uses the DSM or other information obtained from the LiDAR point cloud and fuses the RSIs by adding depth channels. In this paper, we propose a method titled Direct LiDAR-Aerial Fusion Network (DLAFNet) which directly uses the multispectral image and LiDAR point cloud data for semantic Segmentation tasks. In particular, since the sparse features extracted from the KPConv branch are not as essential as features from MSI, we design LiDAR Assisted Attention Module (L-AAM). Our experiments on the modified GRSS18 dataset prove that our method is proper and obtains the best results by comparing with its components and other methods.      

<div align="center">
  <img src="resources/DLAFNet.png"/> 
</div>

## Data

The original data is available from [2018 IEEE GRSS Data Fusion Challenge – Fusion of Multispectral LiDAR and Hyperspectral Data | Hyperspectral Image Analysis Lab (uh.edu)](https://hyperspectral.ee.uh.edu/?page_id=1075). The processed 2D GRSS18 data can be found in [here](https://pan.baidu.com/s/1scYaRvgtW1fGXzZaG2aGyg?pwd=cwpo )(password for BaiduNetdisk: cwpo)  

You can download the transformed data and put it under your path, and change the path of the dataset in the dataset configuration file `\DLAFNet\configs\_base_\datasets\GRSS18_5.py` to the path you have set yourself.    

You can refer to the [KPConv](https://github.com/HuguesTHOMAS/KPConv) for 3D branching data processing, and get the features of different stages and process them through the pseudo-code of the paper, and save them as corresponding files for your convenience. We also provide the test data, you can get them from [here](https://pan.baidu.com/s/1aY4lLqXbkWFRzIHudWRyfQ?pwd=b4bs ) and refer to it to construct your own train data.

## Results

| Data      | Model      | OA(%) | mIoU(%) |
| --------- | ---------- | ----- | ------- |
| MSI       | FCN        | 75.03 | 28.23   |
| MSI       | DANet      | 78.08 | 28.66   |
| MSI       | PSPNet     | 78.45 | 30.97   |
| MSI       | Deeplab v3 | 78.45 | 26.37   |
| MSI       | SegFormer  | 78.67 | 30.83   |
| LiDAR     | PointNet   | 71.40 | 15.83   |  
| LiDAR     | PointNet++ | 75.32 | 18.06   | 
| LiDAR     | KPConv     | 76.97 | 22.57   |
| MSI-LiDAR | EDFT       | 79.25 | 31.15   | 
| MSI-LiDAR | DLAFNet    | 79.88 | 31.94   |

DLAFNet best mIoU results for models able to be found from [here](https://pan.baidu.com/s/1O1qGekBoDRPg4sLoSE7FMw?pwd=pvuk ). 

## Installation

Please refer to [get_started.md](docs/get_started.md) for installation


## Training

```shell 
# Single-gpu training 
python tools\train.py configs\dlafnet\dlafnet_mit_b0_512_80k_GRSS18_5.py 
```

## Acknowledgement

We acknowledged the IEEE Geoscience and Remote Sensing Society Image Analysis and Data Fusion Technical Committee and the Hyperspectral Image Analysis Lab at the University of Houston for the GRSS18 dataset. We also acknowledged paper [EDFT](https://www.mdpi.com/2072-4292/14/5/1294) and forked its [code](https://github.com/h1063135843/EDFT). We are also grateful for the use of [KPConv](https://github.com/HuguesTHOMAS/KPConv). 

## Citation

```
@INPROCEEDINGS{10282837,
  author={Liu, Wei and Wang, He and Qiao, Yicheng and Liang, Bin and Yang, Junli and Zhang, Haopeng}, 
  booktitle={IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium},  
  title={Dlafnet: A Direct Fusion Method of 2D Aerial Image and 3D Lidar Point Cloud for Semantic Segmentation}, 
  year={2023},
  volume={},
  number={},
  pages={5922-5925},
  doi={10.1109/IGARSS52108.2023.10282837}}
```


