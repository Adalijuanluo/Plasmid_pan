# Plasmid_pan
An **underdevelopment** pipeline to define the core genome of plasmids using prokka and roary. 

"We can consider including bakta to optimise the annotation, it would be useful for functional interpretation step"

## Author
EMBO project 2 team
## Input and Output
### Input 
Option 1: .txt file of a list of plasmid accession numbers for downloading from NCBI.

Option 2: Path of a directory that includes the .fasta files of plasmid genomes.  
   
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
* Option 1
````
plasmidpan --help
# plasmidpan -h
plasmidpan --list path/accession.txt --outpath outpath
# plasmidpan -l path/accession.txt -o outpath

````
* Option 2
````
plasmidpan --help
# plasmidpan -h
plasmidpan --input path_of_fasta --outpath outpath
# plasmidpan -i path_of_fasta -o outpath
````

