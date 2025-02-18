#! /bin/bash

Ratios=("0.05" "0.10" "0.15" "0.20" "0.25" "0.30" "0.35" "0.40" "0.45" "0.50" "0.55" "0.60" "0.65" "0.70" "0.75" "0.80" "0.85" "0.90" "0.95")
Datasets=("Grid1296" "Grid2401" "Sobol1" "Sobol2")

touch run-all.sh
chmod +x run-all.sh

for dataset in "${Datasets[@]}"
do
  #echo $dataset
  for ratio in "${Ratios[@]}"
  do
   #echo "  $ratio"
   sed "s/DIESERRATIO/$ratio/" <01_NN-$dataset-RATIO.py >01_NN-$dataset-$ratio.py
   sed "s/#SBATCH --job-name=DATASET-RATIO/#SBATCH --job-name=$dataset-$ratio/" <01_batch-DATASET-RATIO.sh >batchtmp
   sed "s/python 01_NN-DATASET-RATIO.py/python 01_NN-$dataset-$ratio.py/" <batchtmp >01_batch-$dataset-$ratio.sh
   rm batchtmp
   echo -e "sbatch 01_batch-$dataset-$ratio.sh" >>run-all.sh
  done
  #break
done

