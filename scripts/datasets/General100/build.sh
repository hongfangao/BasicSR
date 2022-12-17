# download
python scripts/datasets/General100/download.py

# unzip
unzip datasets/General100.zip -d datasets/General100/
rm datasets/General100.zip
mv datasets/General100/General100/ datasets/General100/original

# modcrop
echo 'Please open MATLAB in the current directory and execute the following statements in turn:'
echo 'cd scripts/datasets/General100/'
echo 'downsample'
