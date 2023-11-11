import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class GRSS18_5dataset(CustomDataset):
    """STARE dataset.

    In segmentation map annotation for STARE, 0 stands for background, which is
    included in 2 categories. ``reduce_zero_label`` is fixed to False. The
    ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '.ah.png'.
    """
    # CLASSES = ('Unclassified','Healthy grass','Stressed grass','Artificial turf','Evergreen trees','Deciduous trees','Bare earth','Water','Residential buildings','Non-residential buildings','Roads','Sidewalks','Crosswalks','Major thoroughfares','Highways','Railways','Paved parking lots','Unpaved parking lots','cars','Trains','Stadium seats')
    CLASSES = ("Unlabeled","Building","Vehicle-Path","Foliage","Human-Path","Vehicle")
    '''
    0 – Unclassified
    1 – Healthy grass
    2 – Stressed grass
    3 – Artificial turf
    4 – Evergreen trees
    5 – Deciduous trees
    6 – Bare earth
    7 – Water
    8 – Residential buildings
    9 – Non-residential buildings
    10 – Roads
    11 – Sidewalks
    12 – Crosswalks
    13 – Major thoroughfares
    14 – Highways
    15 – Railways
    16 – Paved parking lots
    17 – Unpaved parking lots
    18 – Cars
    19 – Trains
    20 – Stadium seats
    '''

    #PALETTE = [[120, 120, 120], [6, 230, 230]]
    # PALETTE = [[0, 0, 0], [255, 255, 255]]
    PALETTE = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128],[120, 120, 120]]


    def __init__(self, **kwargs):
        super(GRSS18_5dataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)


