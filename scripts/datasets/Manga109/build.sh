# download
python scripts/datasets/Manga109/download.py

# unzip
unzip datasets/manga109.zip -d datasets/Manga109/
rm datasets/manga109.zip
mv datasets/Manga109/manga109/ datasets/Manga109/original

# modcrop
echo 'Please open MATLAB in the current directory and execute the following statements in turn:'
echo 'cd scripts/datasets/Manga109/'
echo 'downsample'
