# download
python scripts/datasets/BSDS200/download.py

# unzip
unzip datasets/BSDS200.zip -d datasets/BSDS200/
rm datasets/BSDS200.zip
mv datasets/BSDS200/BSDS200/ datasets/BSDS200/original/

# modcrop
echo 'Please open MATLAB in the current directory and execute the following statements in turn:'
echo 'cd scripts/datasets/BSDS200/'
echo 'downsample'
