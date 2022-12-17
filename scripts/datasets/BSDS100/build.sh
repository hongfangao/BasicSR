# download
python scripts/datasets/BSDS100/download.py

# unzip
unzip datasets/BSDS100.zip -d datasets/BSDS100/
rm datasets/BSDS100.zip
mv datasets/BSDS100/BSDS100/ datasets/BSDS100/original/

# modcrop
echo 'Please open MATLAB in the current directory and execute the following statements in turn:'
echo 'cd scripts/datasets/BSDS100/'
echo 'downsample'
