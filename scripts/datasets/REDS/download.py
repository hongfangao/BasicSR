''' download '''
import os

from falcon.utils import aligo

if __name__ == '__main__':
    os.makedirs('datasets/REDS/', exist_ok=True)
    # train
    aligo.download('datasets/REDS/train_blur_bicubic.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/train_blur_comp.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/train_blur_jpeg.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/train_blur.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/train_sharp_bicubic.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/train_sharp.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/val_blur_bicubic.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/val_blur_comp.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/val_blur_jpeg.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/val_blur.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/val_sharp_bicubic.zip', 'datasets/REDS/')
    aligo.download('datasets/REDS/val_sharp.zip', 'datasets/REDS/')
