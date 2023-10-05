#!/bin/bash



if false; then
screen -S prokka
chmod +x prokka.sh
nohup ./prokka.sh downloaded.txt
fi

source ~/conda/bin/activate
mamba activate prokka

outpath=$1
inpath=$2

cd $outpath
ls $inpath > filelist.txt



cat filelist.txt | while read line; do name=${line%.fasta}; prokka --outdir $name --force --kingdom Bacteria --prefix $name --locustag $name $inpath"/"$line --cpus 8 

done

mamba activate roary

