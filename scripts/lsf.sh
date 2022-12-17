#!/bin/sh

# 设置运行参数
GPU=${GPU:-V100}
GPUNUM=${GPUNUM:-1}
JOBNAME=${JOBNAME:-EAGLE}

# 写入文件
echo "#!/bin/sh" > $JOBNAME.sh
echo "#BSUB -gpu \"num=$GPUNUM:mode=exclusive_process\"" >> $JOBNAME.sh
echo "#BSUB -n $GPUNUM" >> $JOBNAME.sh
if [ $GPU == V100 ]; then
    echo "#BSUB -q gpu" >> $JOBNAME.sh
else
    echo "#BSUB -q gpu2" >> $JOBNAME.sh
fi
echo "#BSUB -o $JOBNAME.out" >> $JOBNAME.sh
echo "#BSUB -e $JOBNAME.err" >> $JOBNAME.sh
echo "#BSUB -J $JOBNAME" >> $JOBNAME.sh
echo "python basicsr/train.py $*" >> $JOBNAME.sh

# 运行
bsub < $JOBNAME.sh

# 删除文件
rm $JOBNAME.sh
