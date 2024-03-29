_base_ = [
    '../_base_/models/pspnet_unet_s5-d16.py', '../_base_/datasets/Vaihingen.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_20k.py'
]
model = dict(decode_head=dict(num_classes=6),test_cfg=dict(crop_size=(256, 256), stride=(170, 170)))
evaluation = dict(metric='mDice')
