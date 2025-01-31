import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob

metricX = "rmse"
#metricX = "mape"
metricY = "r2"
statisticsFile = 'Stats.csv'

if not metricX in ["rmse", "mape", "r2"]:
  print(f'Chosen metric 1 ({metricX}) is not in [rmse, mape, r2]. Please chose one of them. Exit.')
  exit()
if not metricY in ["rmse", "mape", "r2"]:
  print(f'Chosen metric 2 ({metricY}) is not in [rmse, mape, r2]. Please chose one of them. Exit.')
  exit()
  
if metricX is "rmse":
  xLabel = "RMSE"
elif metricX is "mape":
  xLabel = "MAPE"
else:
  xLabel = "R2"

if metricY is "rmse":
  yLabel = "RMSE"
elif metricY is "mape":
  yLabel = "MAPE"
else:
  yLabel = "R2"

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


minMetric1 = dfStatistics[f'{metricX}'].min()
minMetric1 = minMetric1 - 0.01*minMetric1
maxMetric1 = dfStatistics[f'{metricX}'].max()
maxMetric1 = maxMetric1 + 0.01*maxMetric1
minMetric2 = dfStatistics['r2'].min()
minMetric2 = minMetric2 - 0.001*minMetric2
maxMetric2 = dfStatistics['r2'].max()
maxMetric2 = maxMetric2 + 0.01*maxMetric2

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
print(f'Grid1296')
print(f'mean {xLabel}: {np.mean(subsetGrid1296[metricX].to_numpy())}')
print(f'stddev {xLabel}: {np.std(subsetGrid1296[metricX].to_numpy())}')
print(f'mean {yLabel}: {np.mean(subsetGrid1296[metricY].to_numpy())}')
print(f'stddev {yLabel}: {np.std(subsetGrid1296[metricY].to_numpy())}\n')
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
print(f'Grid2401')
print(f'mean {xLabel}: {np.mean(subsetGrid2401[metricX].to_numpy())}')
print(f'stddev {xLabel}: {np.std(subsetGrid2401[metricX].to_numpy())}')
print(f'mean {yLabel}: {np.mean(subsetGrid2401[metricY].to_numpy())}')
print(f'stddev {yLabel}: {np.std(subsetGrid2401[metricY].to_numpy())}\n')
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
print(f'Sobol1')
print(f'mean {xLabel}: {np.mean(subsetSobol1[metricX].to_numpy())}')
print(f'stddev {xLabel}: {np.std(subsetSobol1[metricX].to_numpy())}')
print(f'mean {yLabel}: {np.mean(subsetSobol1[metricY].to_numpy())}')
print(f'stddev {yLabel}: {np.std(subsetSobol1[metricY].to_numpy())}\n')
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]
print(f'Sobol2')
print(f'mean {xLabel}: {np.mean(subsetSobol2[metricX].to_numpy())}')
print(f'stddev {xLabel}: {np.std(subsetSobol2[metricX].to_numpy())}')
print(f'mean {yLabel}: {np.mean(subsetSobol2[metricY].to_numpy())}')
print(f'stddev {yLabel}: {np.std(subsetSobol2[metricY].to_numpy())}\n')

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
  thisAvgRMSE = np.mean(thisSubset[f'{metricX}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricX}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY}'].to_numpy())
  if not labeled:
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
  else:
    axd["Grid1296"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Grid1296.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  thisSubset = subsetGrid2401[subsetGrid2401["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricX}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricX}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY}'].to_numpy())
  if not labeled:
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
  else:
    axd["Grid2401"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Grid2401.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  thisSubset = subsetSobol1[subsetSobol1["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricX}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricX}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY}'].to_numpy())
  if not labeled:
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
  else:
    axd["Sobol1"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Sobol1.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  thisSubset = subsetSobol2[subsetSobol2["ratio"] == ratio]
  thisAvgRMSE = np.mean(thisSubset[f'{metricX}'].to_numpy())
  thisStdRMSE = np.std(thisSubset[f'{metricX}'].to_numpy())
  thisAvgR2 = np.mean(thisSubset[f'{metricY}'].to_numpy())
  thisStdR2 = np.std(thisSubset[f'{metricY}'].to_numpy())
  if not labeled:
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, label=f'{xLabel}', c="#069AF3", marker='o')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, label=f'{yLabel}', c="#F97306", marker='o')
  else:
    axd["Sobol2"].errorbar(1-ratio, thisAvgRMSE, yerr=thisStdRMSE, c="#069AF3", marker='o')
    axd2Sobol2.errorbar(1-ratio, thisAvgR2, yerr=thisStdR2, c="#F97306", marker='o')
    
  labeled = True
  
axd["Grid1296"].legend(bbox_to_anchor=(0.99,0.99))
axd["Grid1296"].set_xlabel("% of Dataset used for Training")
axd["Grid1296"].set_ylabel(f'{xLabel}', c="#069AF3")
axd["Grid1296"].set_title("Dataset used for Training: Grid1296", fontweight='bold')
axd["Grid1296"].set_ylim([minMetric1, maxMetric1])
axd["Grid1296"].tick_params(axis='y', color="#069AF3", which='both')
axd["Grid1296"].spines['left'].set_color("#069AF3")
axd2Grid1296.legend(bbox_to_anchor=(0.99,0.94))
axd2Grid1296.set_ylabel(f'{yLabel}', c="#F97306")
axd2Grid1296.set_ylim([minMetric2, maxMetric2])
axd2Grid1296.spines['left'].set_color("#069AF3")
axd2Grid1296.spines['right'].set_color("#F97306")
axd2Grid1296.tick_params(axis='y', color="#F97306", which='both')


axd["Grid2401"].legend(bbox_to_anchor=(0.18,0.99))
axd["Grid2401"].set_xlabel("% of Dataset used for Training")
axd["Grid2401"].set_ylabel(f'{xLabel}', c="#069AF3")
axd["Grid2401"].set_title("Dataset used for Training: Grid2401", fontweight='bold')
axd["Grid2401"].set_ylim([minMetric1, maxMetric1])
axd["Grid2401"].tick_params(axis='y', color="#069AF3", which='both')
axd["Grid2401"].spines['left'].set_color("#069AF3")
axd2Grid2401.legend(bbox_to_anchor=(0.18,0.94))
axd2Grid2401.set_ylabel(f'{yLabel}', c="#F97306")
axd2Grid2401.set_ylim([minMetric2, maxMetric2])
axd2Grid2401.spines['left'].set_color("#069AF3")
axd2Grid2401.spines['right'].set_color("#F97306")
axd2Grid2401.tick_params(axis='y', color="#F97306", which='both')

axd["Sobol1"].legend(bbox_to_anchor=(0.99,0.99))
axd["Sobol1"].set_xlabel("% of Dataset used for Training")
axd["Sobol1"].set_ylabel(f'{xLabel}', c="#069AF3")
axd["Sobol1"].set_title("Dataset used for Training: Sobol1", fontweight='bold')
axd["Sobol1"].set_ylim([minMetric1, maxMetric1])
axd["Sobol1"].tick_params(axis='y', color="#069AF3", which='both')
axd["Sobol1"].spines['left'].set_color("#069AF3")
axd2Sobol1.legend(bbox_to_anchor=(0.99,0.94))
axd2Sobol1.set_ylabel(f'{yLabel}', c="#F97306")
axd2Sobol1.set_ylim([minMetric2, maxMetric2])
axd2Sobol1.spines['left'].set_color("#069AF3")
axd2Sobol1.spines['right'].set_color("#F97306")
axd2Sobol1.tick_params(axis='y', color="#F97306", which='both')

axd["Sobol2"].legend(bbox_to_anchor=(0.99,0.99))
axd["Sobol2"].set_xlabel("% of Dataset used for Training")
axd["Sobol2"].set_ylabel(f'{xLabel}', c="#069AF3")
axd["Sobol2"].set_title("Dataset used for Training: Sobol2", fontweight='bold')
axd["Sobol2"].set_ylim([minMetric1, maxMetric1])
axd["Sobol2"].tick_params(axis='y', color="#069AF3", which='both')
axd["Sobol2"].spines['left'].set_color("#069AF3")
axd2Sobol2.legend(bbox_to_anchor=(0.99,0.94))
axd2Sobol2.set_ylabel(f'{yLabel}', c="#F97306")
axd2Sobol2.set_ylim([minMetric2, maxMetric2])
axd2Sobol2.spines['left'].set_color("#069AF3")
axd2Sobol2.spines['right'].set_color("#F97306")
axd2Sobol2.tick_params(axis='y', color="#F97306", which='both')

plt.tight_layout()
plt.show()



























