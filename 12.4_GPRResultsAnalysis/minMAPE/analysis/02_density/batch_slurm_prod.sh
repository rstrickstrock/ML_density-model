#!/bin/bash
#SBATCH --partition=hpc,hpc1,hpc3
#SBATCH --nodes=1
#SBATCH --mem 20G
#SBATCH --time=02:00:00
#SBATCH --job-name=evalDens

gmx grompp -f prod.mdp -c equilibrated.gro -t equilibrated.cpt -p topol.top -o prod.tpr

gmx mdrun -v -deffnm prod

