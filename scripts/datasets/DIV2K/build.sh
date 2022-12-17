# download
python scripts/datasets/DIV2K/download.py

# unzip
unzip datasets/DIV2K/DIV2K_train_HR.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_HR.zip
unzip datasets/DIV2K/DIV2K_train_LR_bicubic_X2.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_bicubic_X2.zip
unzip datasets/DIV2K/DIV2K_train_LR_unknown_X2.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_unknown_X2.zip
unzip datasets/DIV2K/DIV2K_train_LR_bicubic_X3.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_bicubic_X3.zip
unzip datasets/DIV2K/DIV2K_train_LR_unknown_X3.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_unknown_X3.zip
unzip datasets/DIV2K/DIV2K_train_LR_bicubic_X4.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_bicubic_X4.zip
unzip datasets/DIV2K/DIV2K_train_LR_unknown_X4.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_unknown_X4.zip
unzip datasets/DIV2K/DIV2K_train_LR_x8.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_x8.zip
unzip datasets/DIV2K/DIV2K_valid_HR.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_HR.zip
unzip datasets/DIV2K/DIV2K_valid_LR_bicubic_X2.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_bicubic_X2.zip
unzip datasets/DIV2K/DIV2K_valid_LR_unknown_X2.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_unknown_X2.zip
unzip datasets/DIV2K/DIV2K_valid_LR_bicubic_X3.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_bicubic_X3.zip
unzip datasets/DIV2K/DIV2K_valid_LR_unknown_X3.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_unknown_X3.zip
unzip datasets/DIV2K/DIV2K_valid_LR_bicubic_X4.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_bicubic_X4.zip
unzip datasets/DIV2K/DIV2K_valid_LR_unknown_X4.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_unknown_X4.zip
unzip datasets/DIV2K/DIV2K_valid_LR_x8.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_x8.zip
# real
unzip datasets/DIV2K/DIV2K_train_LR_difficult.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_difficult.zip
unzip datasets/DIV2K/DIV2K_valid_LR_difficult.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_difficult.zip
unzip datasets/DIV2K/DIV2K_train_LR_wild.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_wild.zip
unzip datasets/DIV2K/DIV2K_valid_LR_wild.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_wild.zip
unzip datasets/DIV2K/DIV2K_train_LR_mild.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_train_LR_mild.zip
unzip datasets/DIV2K/DIV2K_valid_LR_mild.zip -d datasets/DIV2K/
rm datasets/DIV2K/DIV2K_valid_LR_mild.zip

# # move
mkdir datasets/DIV2K/train
mkdir datasets/DIV2K/train/HR/
mkdir datasets/DIV2K/train/LR/
mv datasets/DIV2K/DIV2K_train_HR datasets/DIV2K/train/HR/original/
mkdir datasets/DIV2K/train/LR/bicubic/
mkdir datasets/DIV2K/train/LR/bicubic/X2/
mv datasets/DIV2K/DIV2K_train_LR_bicubic/X2 datasets/DIV2K/train/LR/bicubic/X2/original
mkdir datasets/DIV2K/train/LR/bicubic/X3/
mv datasets/DIV2K/DIV2K_train_LR_bicubic/X3 datasets/DIV2K/train/LR/bicubic/X3/original
mkdir datasets/DIV2K/train/LR/bicubic/X4/
mv datasets/DIV2K/DIV2K_train_LR_bicubic/X4 datasets/DIV2K/train/LR/bicubic/X4/original
rm datasets/DIV2K/DIV2K_train_LR_bicubic -r
mkdir datasets/DIV2K/train/LR/bicubic/X8/
mv datasets/DIV2K/DIV2K_train_LR_x8 datasets/DIV2K/train/LR/bicubic/X8/original
mkdir datasets/DIV2K/train/LR/unknown/
mkdir datasets/DIV2K/train/LR/unknown/X2/
mv datasets/DIV2K/DIV2K_train_LR_unknown/X2/ datasets/DIV2K/train/LR/unknown/X2/original
mkdir datasets/DIV2K/train/LR/unknown/X3/
mv datasets/DIV2K/DIV2K_train_LR_unknown/X3/ datasets/DIV2K/train/LR/unknown/X3/original
mkdir datasets/DIV2K/train/LR/unknown/X4/
mv datasets/DIV2K/DIV2K_train_LR_unknown/X4/ datasets/DIV2K/train/LR/unknown/X4/original
rm datasets/DIV2K/DIV2K_train_LR_unknown -r
mkdir datasets/DIV2K/train/LR/difficult/
mkdir datasets/DIV2K/train/LR/difficult/X4/
mv datasets/DIV2K/DIV2K_train_LR_difficult/ datasets/DIV2K/train/LR/difficult/X4/original
mkdir datasets/DIV2K/train/LR/wild/
mkdir datasets/DIV2K/train/LR/wild/X4/
mv datasets/DIV2K/DIV2K_train_LR_wild/ datasets/DIV2K/train/LR/wild/X4/original
mkdir datasets/DIV2K/train/LR/mild/
mkdir datasets/DIV2K/train/LR/mild/X4/
mv datasets/DIV2K/DIV2K_train_LR_mild/ datasets/DIV2K/train/LR/mild/X4/original
mkdir datasets/DIV2K/valid
mkdir datasets/DIV2K/valid/HR/
mkdir datasets/DIV2K/valid/LR/
mv datasets/DIV2K/DIV2K_valid_HR datasets/DIV2K/valid/HR/original
mkdir datasets/DIV2K/valid/LR/bicubic/
mkdir datasets/DIV2K/valid/LR/bicubic/X2/
mv datasets/DIV2K/DIV2K_valid_LR_bicubic/X2 datasets/DIV2K/valid/LR/bicubic/X2/original
mkdir datasets/DIV2K/valid/LR/bicubic/X3/
mv datasets/DIV2K/DIV2K_valid_LR_bicubic/X3 datasets/DIV2K/valid/LR/bicubic/X3/original
mkdir datasets/DIV2K/valid/LR/bicubic/X4/
mv datasets/DIV2K/DIV2K_valid_LR_bicubic/X4 datasets/DIV2K/valid/LR/bicubic/X4/original
mkdir datasets/DIV2K/valid/LR/bicubic/X8/
mv datasets/DIV2K/DIV2K_valid_LR_x8 datasets/DIV2K/valid/LR/bicubic/X8/original
rm datasets/DIV2K/DIV2K_valid_LR_bicubic -r
mkdir datasets/DIV2K/valid/LR/unknown/
mkdir datasets/DIV2K/valid/LR/unknown/X2/
mv datasets/DIV2K/DIV2K_valid_LR_unknown/X2 datasets/DIV2K/valid/LR/unknown/X2/original
mkdir datasets/DIV2K/valid/LR/unknown/X3/
mv datasets/DIV2K/DIV2K_valid_LR_unknown/X3 datasets/DIV2K/valid/LR/unknown/X3/original
mkdir datasets/DIV2K/valid/LR/unknown/X4/
mv datasets/DIV2K/DIV2K_valid_LR_unknown/X4 datasets/DIV2K/valid/LR/unknown/X4/original
rm datasets/DIV2K/DIV2K_valid_LR_unknown -r
mkdir datasets/DIV2K/valid/LR/difficult/
mkdir datasets/DIV2K/valid/LR/difficult/X4/
mv datasets/DIV2K/DIV2K_valid_LR_difficult/ datasets/DIV2K/valid/LR/difficult/X4/original
mkdir datasets/DIV2K/valid/LR/wild/
mkdir datasets/DIV2K/valid/LR/wild/X4/
mv datasets/DIV2K/DIV2K_valid_LR_wild/ datasets/DIV2K/valid/LR/wild/X4/original
mkdir datasets/DIV2K/valid/LR/mild/
mkdir datasets/DIV2K/valid/LR/mild/X4/
mv datasets/DIV2K/DIV2K_valid_LR_mild/ datasets/DIV2K/valid/LR/mild/X4/original

# extract_subimages
python scripts/datasets/DIV2K/extract_subimages.py

# # create lmdb
python scripts/datasets/DIV2K/create_lmdb.py

# # generate meta info
python scripts/datasets/DIV2K/generate_meta_info.py
