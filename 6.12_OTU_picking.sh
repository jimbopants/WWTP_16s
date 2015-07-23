#!/bin/bash

#MSUB -N 6.12_OTU_picking

#MSUB -A d20725

#MSUB -m abe
#MSUB -q normal

#MSUB -l nodes=1:ppn=10

#MSUB -l walltime=48:00:00

# Activate the macqiime source
source ./activate.sh

cd ./6.12.15/
pick_open_reference_otus.py -i ../seqs.fna -o ./open_ref_otus/ -r ./gg_97_otus.fasta -a -O 10



