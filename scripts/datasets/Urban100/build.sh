# download
python scripts/datasets/Urban100/download.py

# unzip
unzip datasets/urban100.zip -d datasets/Urban100/
rm datasets/urban100.zip
mv datasets/Urban100/urban100/ datasets/Urban100/original

# modcrop
echo 'Please open MATLAB in the current directory and execute the following statements in turn:'
echo 'cd scripts/datasets/Urban100/'
echo 'downsample'
