import sys
from basicsr.train import train_pipeline
import os.path as osp

if __name__ == "__main__":
    # sys.argv += "-opt options/train/SRResNet_SRGAN/train_MSRGAN_x4.yml --debug".split()
    sys.argv += "-opt options/train/waegan/train_WAEGAN_x4.yml --debug".split()
    train_pipeline(osp.abspath(osp.join(__file__,osp.pardir)))