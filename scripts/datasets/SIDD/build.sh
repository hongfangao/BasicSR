# download
python scripts/datasets/SIDD/download.py

# unzip
unzip datasets/SIDD/SIDD_Medium_Srgb.zip
rm datasets/SIDD/SIDD_Medium_Srgb.zip

# mv
mkdir datasets/SIDD/train
mkdir datasets/SIDD/train/input
mkdir datasets/SIDD/train/input/original
mkdir datasets/SIDD/train/target
mkdir datasets/SIDD/train/target/original
python scripts/datasets/SIDD/regroup.py
rm datasets/SIDD/SIDD_Medium_Srgb -r
mkdir datasets/SIDD/valid
mkdir datasets/SIDD/valid/input
mkdir datasets/SIDD/valid/input/original
mkdir datasets/SIDD/valid/target
mkdir datasets/SIDD/valid/target/original

# valid
echo 'Please open MATLAB in the current directory and execute the following statements in turn:'
echo 'cd scripts/datasets/SIDD/'
echo 'valid'

# crop
python scripts/datasets/SIDD/extract_subimages.py

# lmdb
python scripts/datasets/SIDD/create_lmdb.py

# info
python scripts/datasets/SIDD/generate_meta_info.py
