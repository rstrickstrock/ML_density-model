#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 10G
#SBATCH --time=01:00:00
#SBATCH --job-name=evalWOExtraData

python 11_evalTrainedModels_woExtraTestData.py
