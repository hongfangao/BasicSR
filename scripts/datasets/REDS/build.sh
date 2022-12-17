# download
python scripts/datasets/REDS/download.py

# unzip
unzip datasets/REDS/train_blur_bicubic.zip -d datasets/REDS/
rm datasets/REDS/train_blur_bicubic.zip
unzip datasets/REDS/train_blur_comp.zip -d datasets/REDS/
rm datasets/REDS/train_blur_comp.zip
unzip datasets/REDS/train_blur_jpeg.zip -d datasets/REDS/
rm datasets/REDS/train_blur_jpeg.zip
unzip datasets/REDS/train_blur.zip -d datasets/REDS/
rm datasets/REDS/train_blur.zip
unzip datasets/REDS/train_sharp_bicubic.zip -d datasets/REDS/
rm datasets/REDS/train_sharp_bicubic.zip
unzip datasets/REDS/train_sharp.zip -d datasets/REDS/
rm datasets/REDS/train_sharp.zip
unzip datasets/REDS/val_blur_bicubic.zip -d datasets/REDS/
rm datasets/REDS/val_blur_bicubic.zip
unzip datasets/REDS/val_blur_comp.zip -d datasets/REDS/
rm datasets/REDS/val_blur_comp.zip
unzip datasets/REDS/val_blur_jpeg.zip -d datasets/REDS/
rm datasets/REDS/val_blur_jpeg.zip
unzip datasets/REDS/val_blur.zip -d datasets/REDS/
rm datasets/REDS/val_blur.zip
unzip datasets/REDS/val_sharp_bicubic.zip -d datasets/REDS/
rm datasets/REDS/val_sharp_bicubic.zip
unzip datasets/REDS/val_sharp.zip -d datasets/REDS/
rm datasets/REDS/val_sharp.zip

# mv
mv datasets/REDS/train/train_blur/ datasets/REDS/train/blur
mv datasets/REDS/val/val_blur/ datasets/REDS/val/blur
mv datasets/REDS/train/train_blur_bicubic/ datasets/REDS/train/blur_bicubic
mv datasets/REDS/val/val_blur_bicubic/ datasets/REDS/val/blur_bicubic
mv datasets/REDS/train/train_blur_comp/ datasets/REDS/train/blur_comp
mv datasets/REDS/val/val_blur_comp/ datasets/REDS/val/blur_comp
mv datasets/REDS/train/train_blur_jpeg/ datasets/REDS/train/blur_jpeg
mv datasets/REDS/val/val_blur_jpeg/ datasets/REDS/val/blur_jpeg
mv datasets/REDS/train/train_sharp/ datasets/REDS/train/sharp
mv datasets/REDS/val/val_sharp/ datasets/REDS/val/sharp
mv datasets/REDS/train/train_sharp_bicubic/ datasets/REDS/train/sharp_bicubic
mv datasets/REDS/val/val_sharp_bicubic/ datasets/REDS/val/sharp_bicubic
