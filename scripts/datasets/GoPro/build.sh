# download
python scripts/datasets/GoPro/download.py

# unzip
unzip datasets/GOPRO_Large.zip -d datasets/GoPro
rm datasets/GOPRO_Large.zip

# mv
mkdir datasets/GoPro/train/sharp
mkdir datasets/GoPro/train/blur
mkdir datasets/GoPro/train/blur_gamma
mkdir datasets/GoPro/test/sharp
mkdir datasets/GoPro/test/blur
mkdir datasets/GoPro/test/blur_gamma
python scripts/GoPro/regroup.py
mkdir datasets/GoPro/train/sharp/original
mv datasets/GoPro/train/sharp/*.png datasets/GoPro/train/sharp/original
mkdir datasets/GoPro/train/blur/original
mv datasets/GoPro/train/blur/*.png datasets/GoPro/train/blur/original
mkdir datasets/GoPro/train/blur_gamma/original
mv datasets/GoPro/train/blur_gamma/*.png datasets/GoPro/train/blur_gamma/original
mkdir datasets/GoPro/test/sharp/original
mv datasets/GoPro/test/sharp/*.png datasets/GoPro/test/sharp/original
mkdir datasets/GoPro/test/blur/original
mv datasets/GoPro/test/blur/*.png datasets/GoPro/test/blur/original
mkdir datasets/GoPro/test/blur_gamma/original
mv datasets/GoPro/test/blur_gamma/*.png datasets/GoPro/test/blur_gamma/original

# subs
python scripts/datasets/GoPro/extract_subimages.py

# create lmdb
python scripts/datasets/GoPro/create_lmdb.py
