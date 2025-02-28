#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 32G
#SBATCH --time=40:00:00
#SBATCH --job-name=Sobol2-0.95

python 01_NN-Sobol2-0.95.py
