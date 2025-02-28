#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 32G
#SBATCH --time=40:00:00
#SBATCH --job-name=Grid2401-0.65

python 01_NN-Grid2401-0.65.py
