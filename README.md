# Plasmid_pan
A pipeline to define the core genome of plasmids 

## Author
EMBO project 2 team
## Input and Output
### Input 
.txt file of a list of plasmid accession numbers for downloading from NCBI 

or 

Path of a directory that includes the .fasta files of plasmid genomes.  
   
### Output
1. A directory of plasmid genome annotation .gff files by prokka.
2. A directory of pangenome output
3. Tables and figures that summarise the hard, soft shell/core genes and accessory genes. 

## Installation
1. Update or Install Miniconda and add the bioconda channel:
   - conda update -n base -c defaults conda
   
     or 
   
   - Install miniconda3  -> https://docs.conda.io/en/latest/miniconda.html
   - Add bioconda -> http://www.ddocent.com//bioconda/
2. Create miniconda3 environment:
````
conda create -n plasmid_pan 
conda activate plasmid_pan
conda install -y -c conda-forge -c bioconda -c defaults prokka
conda install -y -c bioconda roary
````
3. Download this repository:
````
git clone https://github.com/Adalijuanluo/Plasmid_pan.git
cd Plasmid_pan
````
## Usage
* Output 1
````
plasmidpan -h
plasmidpan -l path/accession.txt -o outpath
````
* Output 2
````
plasmidpan -i path_of_fasta -o outpath
````

