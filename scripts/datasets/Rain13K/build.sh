# download
python scripts/datasets/Rain13K/download.py

# unzip
unzip datasets/Rain13K/Rain13K_train_input.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_train_input.zip
unzip datasets/Rain13K/Rain13K_train_target.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_train_target.zip
unzip datasets/Rain13K/Rain13K_test_100_input.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_100_input.zip
unzip datasets/Rain13K/Rain13K_test_100_target.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_100_target.zip
unzip datasets/Rain13K/Rain13K_test_100L_input.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_100L_input.zip
unzip datasets/Rain13K/Rain13K_test_100L_target.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_100L_target.zip
unzip datasets/Rain13K/Rain13K_test_100H_input.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_100H_input.zip
unzip datasets/Rain13K/Rain13K_test_100H_target.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_100H_target.zip
unzip datasets/Rain13K/Rain13K_test_1200_input.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_1200_input.zip
unzip datasets/Rain13K/Rain13K_test_1200_target.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_1200_target.zip
unzip datasets/Rain13K/Rain13K_test_2800_input.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_2800_input.zip
unzip datasets/Rain13K/Rain13K_test_2800_target.zip -d datasets/Rain13K/
rm datasets/Rain13K/Rain13K_test_2800_target.zip

# mv
mkdir datasets/Rain13K/train
mv datasets/Rain13K/Rain13K_train_input datasets/Rain13K/train/input
mv datasets/Rain13K/Rain13K_train_target datasets/Rain13K/train/target
mkdir datasets/Rain13K/test
mkdir datasets/Rain13K/test/Test100
mv datasets/Rain13K/Rain13K_test_100_input datasets/Rain13K/test/Test100/input
mv datasets/Rain13K/Rain13K_test_100_target datasets/Rain13K/test/Test100/target
mkdir datasets/Rain13K/test/Rain100H
mv datasets/Rain13K/Rain13K_test_100H_input datasets/Rain13K/test/Rain100H/input
mv datasets/Rain13K/Rain13K_test_100H_target datasets/Rain13K/test/Rain100H/target
mkdir datasets/Rain13K/test/Rain100L
mv datasets/Rain13K/Rain13K_test_100L_input datasets/Rain13K/test/Rain100L/input
mv datasets/Rain13K/Rain13K_test_100L_target datasets/Rain13K/test/Rain100L/target
mkdir datasets/Rain13K/test/Test1200
mv datasets/Rain13K/Rain13K_test_1200_input datasets/Rain13K/test/Test1200/input
mv datasets/Rain13K/Rain13K_test_1200_target datasets/Rain13K/test/Test1200/target
mkdir datasets/Rain13K/test/Test2800
mv datasets/Rain13K/Rain13K_test_2800_input datasets/Rain13K/test/Test2800/input
mv datasets/Rain13K/Rain13K_test_2800_target datasets/Rain13K/test/Test2800/target
