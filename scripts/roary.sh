#!/bin/bash

# Ada cluster
#source ~/conda/bin/activate
#conda activate roary
# Liam laptop
source /Users/Liam/opt/miniconda3/bin/activate
conda activate plaspan_env

input=$1
outpath=$2
echo "Input gff: "$input
echo "The pangenome will be saved at: "$outpath


ls $input/*/*.gff

roary -p 12 -e -v -s -i 80 -cd 80 -f $outpath"_i80_c80" $input/*/*.gff
