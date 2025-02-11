#! /bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 5G
#SBATCH --time=00:05:00
#SBATCH --job-name=eval_density

echo -e "density\n" | gmx energy -f prod.edr -o density
