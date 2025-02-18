#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 32G
#SBATCH --time=72:00:00
#SBATCH --job-name=S1-0.05

python 01_NN-Sobol1-0.05.py
