# Assume that DIV2K has been downloaded.

# download
python scripts/datasets/DF2K/download.py

# unzip
tar -xvf datasets/Flickr2K.tar -C datasets
rm datasets/Flickr2K.tar

# copy
mv datasets/Flickr2K/ datasets/DF2K
mkdir datasets/DF2K/train
mkdir datasets/DF2K/train/HR
mv datasets/DF2K/Flickr2K_HR datasets/DF2K/train/HR/original
mkdir datasets/DF2K/train/LR
mkdir datasets/DF2K/train/LR/bicubic
mkdir datasets/DF2K/train/LR/bicubic/X2
mv datasets/DF2K/Flickr2K_LR_bicubic/X2 datasets/DF2K/train/LR/bicubic/X2/original
mkdir datasets/DF2K/train/LR/bicubic/X3
mv datasets/DF2K/Flickr2K_LR_bicubic/X3 datasets/DF2K/train/LR/bicubic/X3/original
mkdir datasets/DF2K/train/LR/bicubic/X4
mv datasets/DF2K/Flickr2K_LR_bicubic/X4 datasets/DF2K/train/LR/bicubic/X4/original
rm datasets/DF2K/Flickr2K_LR_bicubic -r
mkdir datasets/DF2K/train/LR/unknown
mkdir datasets/DF2K/train/LR/unknown/X2
mv datasets/DF2K/Flickr2K_LR_unknown/X2 datasets/DF2K/train/LR/unknown/X2/original
mkdir datasets/DF2K/train/LR/unknown/X3
mv datasets/DF2K/Flickr2K_LR_unknown/X3 datasets/DF2K/train/LR/unknown/X3/original
mkdir datasets/DF2K/train/LR/unknown/X4
mv datasets/DF2K/Flickr2K_LR_unknown/X4 datasets/DF2K/train/LR/unknown/X4/original
rm datasets/DF2K/Flickr2K_LR_unknown -r
cp datasets/DIV2K/train/HR/original/*.png datasets/DF2K/train/HR/original/
cp datasets/DIV2K/train/LR/bicubic/X2/original/*.png datasets/DF2K/train/LR/bicubic/X2/original
cp datasets/DIV2K/train/LR/bicubic/X3/original/*.png datasets/DF2K/train/LR/bicubic/X3/original
cp datasets/DIV2K/train/LR/bicubic/X4/original/*.png datasets/DF2K/train/LR/bicubic/X4/original
cp datasets/DIV2K/train/LR/unknown/X2/original/*.png datasets/DF2K/train/LR/unknown/X2/original
cp datasets/DIV2K/train/LR/unknown/X3/original/*.png datasets/DF2K/train/LR/unknown/X3/original
cp datasets/DIV2K/train/LR/unknown/X4/original/*.png datasets/DF2K/train/LR/unknown/X4/original

# extract_subimages
python scripts/datasets/DF2K/extract_subimages.py

# create lmdb
python scripts/datasets/DF2K/create_lmdb.py

# generate meta info
python scripts/datasets/DF2K/generate_meta_info.py
