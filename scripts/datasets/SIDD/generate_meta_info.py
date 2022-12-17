''' generate meta info '''
from os import path as osp

from falcon.utils import scandir
from PIL import Image


def generate_meta_info_sidd():
    """ Generate meta info for SIDD dataset. """
    gt_folder = 'datasets/SIDD/train/target/subs'
    meta_info_txt = 'core/data/meta_info/meta_info_SIDD_sub.txt'
    img_list = sorted(list(scandir(gt_folder)))
    with open(meta_info_txt, 'w') as f:
        for img_path in img_list:
            img = Image.open(osp.join(gt_folder, img_path))  # lazy load
            width, height = img.size
            mode = img.mode
            if mode == 'RGB':
                n_channel = 3
            elif mode == 'L':
                n_channel = 1
            else:
                raise ValueError(f'Unsupported mode {mode}.')
            info = f'{img_path} ({height},{width},{n_channel})'
            f.write(f'{info}\n')


if __name__ == '__main__':
    generate_meta_info_sidd()
