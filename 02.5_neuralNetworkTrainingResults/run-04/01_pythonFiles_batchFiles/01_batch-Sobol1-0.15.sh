#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 32G
#SBATCH --time=40:00:00
#SBATCH --job-name=Sobol1-0.15

python 01_NN-Sobol1-0.15.py
