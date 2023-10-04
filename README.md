# Plasmid_pan
An **underdevelopment** pipeline to define the core and accessory genome of plasmids using prokka and roary. 

"We can consider including bakta to optimise the annotation, it would be useful for functional interpretation and pinpoint the R-M hotspots."

## Author
EMBO project 2 team
## Contents

- [Installation](#installation)
- [Input & Output](#input-and-output)
- [Usage](#usage)

## Installation
1. Mamba is recommended to install packages
   Install Mamba using miniforge https://github.com/conda-forge/miniforge#mambaforge
   
   For linux installation:
````
wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

bash Miniforge3.sh -b -p "${HOME}/conda"

source "${HOME}/conda/etc/profile.d/conda.sh"

conda activate
````
2. Create a new environment and install packages:
````
mamba create -n plaspan_env

mamba activate plaspan_env

mamba install roary

mamba install prokka
````
3. Download this repository:
````
git clone https://github.com/Adalijuanluo/Plasmid_pan.git
cd Plasmid_pan
````

## Input and Output
### Input 
Option 1: .txt file of a list of plasmid accession numbers for downloading from NCBI.

Option 2: Path of a directory that includes the .fasta files of plasmid genomes.  
   
### Output
1. A directory of plasmid genome annotation .gff files by prokka.
2. A directory of pangenome output
3. Tables and figures that summarise the hard, soft shell/core genes and accessory genes. 

## Usage
* Option 1
````
plasmidpan --help

plasmidpan --acclist /path/accession.txt --outpath /outpath

# plasmidpan -a /path/accession.txt -o /outpath

````
* Option 2
````
plasmidpan --input /path_of_fasta --outpath /outpath

# plasmidpan -i /path_of_fasta -o /outpath
````

