#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 10G
#SBATCH --time=15:00:00
#SBATCH --job-name=testNN

python 01_testNNP.py
