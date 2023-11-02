#!/usr/bin/env python3
from time import sleep as sl

import sys
from os import environ
from Bio import SeqIO
import os
from os.path import commonprefix
import shutil
import argparse
import datetime
import time
import subprocess



def main(args):
    """
    run three components :
    1 fasta files downloading
    2 annotation using prokka
    3 pangenome definition using Roary

    :param args: command line input arguments in argparse object
    :return: output of gff, prokka
    """
    run_pangenomepip(args)


def download_sh(acclist, outpath):
    openfile = open(acclist, "r").read().splitlines()
    bashfile = outpath + "/download_fasta.sh"
    outf = open(bashfile, "w")
    outf.write("#!/bin/bash" + "\n" + "\n" + "\n" + "path=$1"+ "\n" + "mkdir $path" + "\n" + "cd $path"  + "\n" + "\n" )

    for line in openfile:
        a = "wget -O "
        b = '.fasta "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id='
        c = '&db=nuccore&report=fasta"'
        if line != "":
            out = a + line + b + line + c
            outf.write(out + "\n")
    outfasta = outpath + "/_fasta"
    # download_cmd = f"cd {outpath}"
    # subprocess.Popen(download_cmd, shell=True).wait()
    download_cmd = f"bash {bashfile}"
    print(f"bash {bashfile}")
    # subprocess.Popen(download_cmd, shell=True).wait()


    return bashfile, outfasta

def download(bashfile, outfasta):
    # print(bashfile)
    try:
        subprocess.run(["bash", bashfile, outfasta], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    return
def run_prokka(input_genomes_dir,output_prokka_dir):
    prokka_cmd = f"bash ../prokka.sh {output_prokka_dir} {input_genomes_dir}"
    subprocess.Popen(prokka_cmd, shell=True).wait()
    # try:
    #     subprocess.run(["bash", "prokka.sh", output_prokka_dir, input_genomes_dir], check=True, shell=False)
    # except subprocess.CalledProcessError as e:
    #     print(f"Error: {e}")

    return

def run_roary(output_prokka_dir, output_roary_dir):
    print(output_prokka_dir)
    print(output_roary_dir)
    roary_cmd=f"bash ../roary.sh {output_prokka_dir} {output_roary_dir}"
    subprocess.Popen(roary_cmd, shell=True).wait()

    return

def run_pangenomepip(args):
    start_time = time.time()
    ## get inputs from args
    script_path = sys.path[0]
    acclist = args.acclist
    outpath = args.outpath
    # if os.path.exists(outpath):
    #     pass
    # else:
    #     os.mkdir(outpath)
    output_prokka_dir = outpath + "/" + args.prefix + "_prokka"
    output_roary_dir = outpath + "/" + args.prefix + "_roary"
    os.makedirs(output_prokka_dir, exist_ok=True)
    # os.makedirs(output_roary_dir, exist_ok=True)
    if acclist:
        bashfile, fastadir = download_sh(acclist, outpath)
        download(bashfile, fastadir)
        run_prokka(fastadir,output_prokka_dir)
        run_roary(output_prokka_dir, output_roary_dir)

    if args.input:
        fastadir = args.input
        run_prokka(fastadir, output_prokka_dir)
        run_roary(output_prokka_dir, output_roary_dir)

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-a", "--acclist",
                        help=".txt file of a list of plasmid accession numbers for downloading from NCBI, e.g., "
                             "acclist.txt")
    parser.add_argument("-i", "--input",help="Path of a directory that includes the .fasta files of plasmid genomes, e.g., /home/fasta")
    parser.add_argument("-o", "--outpath",help="Output directory, e.g., /home/output")
    parser.add_argument("-p", "--prefix", help="prefix of outdir, e.g., PTU0", default="")
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    main(args)