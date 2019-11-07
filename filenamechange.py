import os, glob
import sys

base_dir=sys.argv[1]
os.chdir(base_dir)
#os.chdir("/scicomp/home/nej1/LP/EU/from_Joao/genomes/mergetest")
#base_dir = "/scicomp/home/nej1/LP/all_genome_allele"
#os.chdir("/scicomp/home/nej1/LP/all_genome_allele")
for file in os.listdir("."): 
     if file.endswith("fasta"):
         #name=file.split("_")[1]
         name=file.split("_")[0]+".fasta"
        #name=file.split("_")[0]+"-"+file.split("_")[1]\
         #+"-"+file.split("_")[2]+".fasta"
         os.rename(file,name)
