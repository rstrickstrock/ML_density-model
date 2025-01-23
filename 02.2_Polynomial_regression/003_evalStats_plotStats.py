import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob


statisticsFile = 'Stats.csv'

if not os.path.isfile(statisticsFile):
  print(f'Can not find and open \'{statisticsFile}\'. Exit.')
  exit()
else:
  dfStatistics = pd.read_csv(statisticsFile)
  #print(f'{dfStatistics}')
  try:
    dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])
  except:
    print(f'Something went wrong with\'dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])\'.')
  else:
    #print(f'{dfStatistics}')
    pass


minRMSE = dfStatistics['rmse'].min()
minRMSE = minRMSE - 0.01*minRMSE
maxRMSE = dfStatistics['rmse'].max()
maxRMSE = maxRMSE + 0.01*maxRMSE
minR2 = dfStatistics['r2'].min()
minR2 = minR2 - 0.001*minR2
maxR2 = dfStatistics['r2'].max()
maxR2 = maxR2 + 0.01*maxR2

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
print(f'Grid1296')
print(f'mean RMSE: {np.mean(subsetGrid1296["rmse"].to_numpy())}')
print(f'stddev RMSE: {np.std(subsetGrid1296["rmse"].to_numpy())}')
print(f'mean R2: {np.mean(subsetGrid1296["r2"].to_numpy())}')
print(f'stddev R2: {np.std(subsetGrid1296["r2"].to_numpy())}\n')
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
print(f'Grid2401')
print(f'mean RMSE: {np.mean(subsetGrid2401["rmse"].to_numpy())}')
print(f'stddev RMSE: {np.std(subsetGrid2401["rmse"].to_numpy())}')
print(f'mean R2: {np.mean(subsetGrid2401["r2"].to_numpy())}')
print(f'stddev R2: {np.std(subsetGrid2401["r2"].to_numpy())}\n')
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
print(f'Sobol1')
print(f'mean RMSE: {np.mean(subsetSobol1["rmse"].to_numpy())}')
print(f'stddev RMSE: {np.std(subsetSobol1["rmse"].to_numpy())}')
print(f'mean R2: {np.mean(subsetSobol1["r2"].to_numpy())}')
print(f'stddev R2: {np.std(subsetSobol1["r2"].to_numpy())}\n')
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]
print(f'Sobol2')
print(f'mean RMSE: {np.mean(subsetSobol2["rmse"].to_numpy())}')
print(f'stddev RMSE: {np.std(subsetSobol2["rmse"].to_numpy())}')
print(f'mean R2: {np.mean(subsetSobol2["r2"].to_numpy())}')
print(f'stddev R2: {np.std(subsetSobol2["r2"].to_numpy())}\n')

## plots
gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['Grid1296', 'Sobol1'], 
                               ['Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(14.0, 14.0))

axd2Grid1296 = axd["Grid1296"].twinx()
axd2Grid2401 = axd["Grid2401"].twinx()
axd2Sobol1 = axd["Sobol1"].twinx()
axd2Sobol2 = axd["Sobol2"].twinx()

labeled = False
for ratio in subsetGrid1296["ratio"].unique():
  thisSubset = subsetGrid1296[subsetGrid1296["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset["rmse"].to_numpy())
  thisStdRMSE = np.std(thisSubset["rmse"].to_numpy())
  thisAvgR2 = np.mean(thisSubset["r2"].to_numpy())
  thisStdR2 = np.std(thisSubset["r2"].to_numpy())
  if not labeled:
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label="RMSE", c="#069AF3", marker='o')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label="R2", c="#F97306", marker='o')
  else:
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  thisSubset = subsetGrid2401[subsetGrid2401["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset["rmse"].to_numpy())
  thisStdRMSE = np.std(thisSubset["rmse"].to_numpy())
  thisAvgR2 = np.mean(thisSubset["r2"].to_numpy())
  thisStdR2 = np.std(thisSubset["r2"].to_numpy())
  if not labeled:
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label="RMSE", c="#069AF3", marker='o')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label="R2", c="#F97306", marker='o')
  else:
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  thisSubset = subsetSobol1[subsetSobol1["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset["rmse"].to_numpy())
  thisStdRMSE = np.std(thisSubset["rmse"].to_numpy())
  thisAvgR2 = np.mean(thisSubset["r2"].to_numpy())
  thisStdR2 = np.std(thisSubset["r2"].to_numpy())
  if not labeled:
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label="RMSE", c="#069AF3", marker='o')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label="R2", c="#F97306", marker='o')
  else:
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  thisSubset = subsetSobol2[subsetSobol2["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset["rmse"].to_numpy())
  thisStdRMSE = np.std(thisSubset["rmse"].to_numpy())
  thisAvgR2 = np.mean(thisSubset["r2"].to_numpy())
  thisStdR2 = np.std(thisSubset["r2"].to_numpy())
  if not labeled:
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label="RMSE", c="#069AF3", marker='o')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label="R2", c="#F97306", marker='o')
  else:
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  labeled = True
  
axd["Grid1296"].legend(bbox_to_anchor=(0.99,0.99))
axd["Grid1296"].set_xlabel("% of Dataset used for Training")
axd["Grid1296"].set_ylabel("RMSE", c="#069AF3")
axd["Grid1296"].set_title("Dataset used for Training: Grid1296", fontweight='bold')
axd["Grid1296"].set_ylim([minRMSE, maxRMSE])
axd["Grid1296"].tick_params(axis='y', color="#069AF3", which='both')
axd["Grid1296"].spines['left'].set_color("#069AF3")
axd2Grid1296.legend(bbox_to_anchor=(0.99,0.94))
axd2Grid1296.set_ylabel("R2", c="#F97306")
axd2Grid1296.set_ylim([minR2, maxR2])
axd2Grid1296.spines['left'].set_color("#069AF3")
axd2Grid1296.spines['right'].set_color("#F97306")
axd2Grid1296.tick_params(axis='y', color="#F97306", which='both')


axd["Grid2401"].legend(bbox_to_anchor=(0.18,0.99))
axd["Grid2401"].set_xlabel("% of Dataset used for Training")
axd["Grid2401"].set_ylabel("RMSE", c="#069AF3")
axd["Grid2401"].set_title("Dataset used for Training: Grid2401", fontweight='bold')
axd["Grid2401"].set_ylim([minRMSE, maxRMSE])
axd["Grid2401"].tick_params(axis='y', color="#069AF3", which='both')
axd["Grid2401"].spines['left'].set_color("#069AF3")
axd2Grid2401.legend(bbox_to_anchor=(0.18,0.94))
axd2Grid2401.set_ylabel("R2", c="#F97306")
axd2Grid2401.set_ylim([minR2, maxR2])
axd2Grid2401.spines['left'].set_color("#069AF3")
axd2Grid2401.spines['right'].set_color("#F97306")
axd2Grid2401.tick_params(axis='y', color="#F97306", which='both')

axd["Sobol1"].legend(bbox_to_anchor=(0.99,0.99))
axd["Sobol1"].set_xlabel("% of Dataset used for Training")
axd["Sobol1"].set_ylabel("RMSE", c="#069AF3")
axd["Sobol1"].set_title("Dataset used for Training: Sobol1", fontweight='bold')
axd["Sobol1"].set_ylim([minRMSE, maxRMSE])
axd["Sobol1"].tick_params(axis='y', color="#069AF3", which='both')
axd["Sobol1"].spines['left'].set_color("#069AF3")
axd2Sobol1.legend(bbox_to_anchor=(0.99,0.94))
axd2Sobol1.set_ylabel("R2", c="#F97306")
axd2Sobol1.set_ylim([minR2, maxR2])
axd2Sobol1.spines['left'].set_color("#069AF3")
axd2Sobol1.spines['right'].set_color("#F97306")
axd2Sobol1.tick_params(axis='y', color="#F97306", which='both')

axd["Sobol2"].legend(bbox_to_anchor=(0.99,0.99))
axd["Sobol2"].set_xlabel("% of Dataset used for Training")
axd["Sobol2"].set_ylabel("RMSE", c="#069AF3")
axd["Sobol2"].set_title("Dataset used for Training: Sobol2", fontweight='bold')
axd["Sobol2"].set_ylim([minRMSE, maxRMSE])
axd["Sobol2"].tick_params(axis='y', color="#069AF3", which='both')
axd["Sobol2"].spines['left'].set_color("#069AF3")
axd2Sobol2.legend(bbox_to_anchor=(0.99,0.94))
axd2Sobol2.set_ylabel("R2", c="#F97306")
axd2Sobol2.set_ylim([minR2, maxR2])
axd2Sobol2.spines['left'].set_color("#069AF3")
axd2Sobol2.spines['right'].set_color("#F97306")
axd2Sobol2.tick_params(axis='y', color="#F97306", which='both')

plt.tight_layout()
plt.show()



























