# dataset settings
dataset_type = 'GRSS18_5dataset'
data_root = 'Your data path'
img_norm_cfg = dict(
    mean=[108.181244, 111.65996, 109.42959],std=[59.013214, 57.097572, 57.428936],to_rgb=True)
img_scale = (512,512)
crop_size = (512,512)
train_pipeline = [
    dict(type='LoadImageFromFile'),# 同时load npz文件
    # dict(type='LoadnpzFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='PhotoMetricDistortion'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type="addStage"),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    # 添加4个stage数据至img=img[0] img[1]=stage01
    dict(type='Collect', keys=['img', 'gt_semantic_seg'])
    # dict(type='Collect', keys=['img', 'gt_semantic_seg',"stage01","stage02","stage03","stage04"])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type="addStage"),
    # dict(type='DefaultFormatBundle'),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]

data = dict(
    samples_per_gpu=1, #batch_size
    workers_per_gpu=1, #nums gpu
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/train',
        ann_dir='ann_dir/train',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/val',
        ann_dir='ann_dir/val',  
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/val',
        ann_dir='ann_dir/val', 
        pipeline=test_pipeline)
)