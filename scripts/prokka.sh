#!/bin/bash



if false; then
screen -S prokka
chmod +x prokka.sh
nohup ./prokka.sh downloaded.txt
fi

# path to conda activate
# Ada cluster
# source ~/conda/bin/activate
# conda activate prokka
# Liam laptop
source /Users/Liam/opt/miniconda3/bin/activate
conda activate "plaspan_env" 

outpath=$1
inpath=$2

#cd $outpath
ls $inpath > filelist.txt


cat filelist.txt | while read line; do name=${line%.fasta}; prokka --outdir "$outpath"/$name --force --kingdom Bacteria --prefix $name --locustag $name $inpath"/"$line --cpus 8 

done

# not needed is plaspan_env
# mamba activate roary

