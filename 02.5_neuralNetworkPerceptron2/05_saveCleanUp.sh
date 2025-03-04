mkdir 01_pythonFiles_batchFiles 01_slurmFiles 01_StatsParts
mv Stats.csv MAPE-vs-R2.png Ratios-vs-MAPE_R2.png run-*
mv StatsPart-* 01_StatsParts/
mv slurm-392* 01_slurmFiles/
mv 01_batch-Grid* 01_batch-Sobol* 01_pythonFiles_batchFiles/
mv 01_NN-Grid1296-0.* 01_NN-Grid2401-0.* 01_NN-Sobol1-0.* 01_NN-Sobol2-0.* 01_pythonFiles_batchFiles/
mv 01_pythonFiles_batchFiles/ 01_slurmFiles/ 01_StatsParts/ run-*
rm 01_run-all.sh
mv run-* ../02.5_neuralNetworkTrainingResults/
