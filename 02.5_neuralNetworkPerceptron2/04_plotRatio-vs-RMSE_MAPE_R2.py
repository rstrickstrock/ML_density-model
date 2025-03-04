import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob
import sys

try:
  saveOrShow = sys.argv[1]
except:
  saveOrShow = "show"
if saveOrShow == "save":
  pass
else:
  saveOrShow = "show"

statisticsFile = 'Stats.csv'
#metric1 = "rmse"
metric1 = "mape"
metric2 = "r2"
#metric2 = "mape"

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


if metric1 == "rmse":
  xLabel = "RMSE"
  minMETRIC1 = dfStatistics[f'{metric1}'].min()
  minMETRIC1 = minMETRIC1 - 0.01*minMETRIC1
  maxMETRIC1 = 100
elif metric1 == "mape":
  xLabel = "MAPE"
  minMETRIC1 = dfStatistics[f'{metric1}'].min()
  minMETRIC1 = minMETRIC1 - 0.01*minMETRIC1
  maxMETRIC1 = 0.10 
elif metric1 == "r2":
  xLabel = "R2"
  maxMETRIC1 = 1.05
  minMETRIC1 = 0.20
else:
  print(f'Please set \'metric1\' to "rmse", "r2" or "mape". (Is: {metric1}). Exit.')
  exit()
  
if metric2 == "rmse":
  yLabel = "RMSE"
  minMETRIC2 = dfStatistics[f'{metric2}'].min()
  minMETRIC2 = minMETRIC2 - 0.01*minMETRIC2
  maxMETRIC2 = 100
elif metric2 == "mape":
  yLabel = "MAPE"
  minMETRIC2 = dfStatistics[f'{metric2}'].min()
  minMETRIC2 = minMETRIC2 - 0.01*minMETRIC2
  maxMETRIC2 = 0.10
elif metric2 == "r2":
  yLabel = "R2"
  maxMETRIC2 = 1.05
  minMETRIC2 = 0.20
else:
  print(f'Please set \'metric2\' to "rmse", "r2" or "mape". (Is: {metric2}). Exit.')
  exit()

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]


## plots

datasetSubsets = [subsetGrid1296, subsetGrid2401, subsetSobol1, subsetSobol2]
#print(f'{datasetSubsets[0]}')
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']
markers = ['1', '2', '3', '4', 'x', '+']
DatasetNames = ['Grid1296', 'Grid2401', 'Sobol1', 'Sobol2']

gs_kw = dict(width_ratios=[1, 1], height_ratios=[1])
fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2']],  
                              gridspec_kw=gs_kw, figsize=(15.0, 5.0))

for nSubset in range(0, len(datasetSubsets)):
  #print(f'nSubset: {nSubset}')
  thisDataSubset = datasetSubsets[nSubset]
  #gs_kw = dict(width_ratios=[1, 1, 1], height_ratios=[1])
  #fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2', 'AvgByKernel']],
                                 #gridspec_kw=gs_kw, figsize=(15.0, 5.0))
  
  thisX = []
  thisRMSE = []
  thisRMSEerr = []
  thisR2 = []
  thisR2err = []
  for ratio in thisDataSubset["ratio"].unique():
    thisX.append(1-ratio)
    thisDataSubsetRatio = thisDataSubset[thisDataSubset["ratio"] == ratio]
    thisRMSE.append(np.mean(thisDataSubsetRatio[f'{metric1}'].to_numpy()))
    thisRMSEerr.append(np.std(thisDataSubsetRatio[f'{metric1}'].to_numpy()))
    thisR2.append(np.mean(thisDataSubsetRatio[f'{metric2}'].to_numpy()))
    thisR2err.append(np.std(thisDataSubsetRatio[f'{metric2}'].to_numpy()))
  axd['METRIC1'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'Dataset = {DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='-.')
  axd['METRIC2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'Dataset = {DatasetNames[nSubset]}', marker=markers[nSubset], color=colors[nSubset], ls='-.')
    
  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel}', fontweight='bold')
  axd["METRIC1"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1"].set_title(f'Avg. {xLabel} per Training-/Testdata split', fontweight='bold')
  #axd["METRIC1"].set_ylim([minMETRIC1, maxMETRIC1])
  axd["METRIC2"].legend()
  axd["METRIC2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2"].set_title(f'Avg. {yLabel} per Training-/Testdata split', fontweight='bold')
  #axd["METRIC2"].set_ylim([minMETRIC2, maxMETRIC2])
  
  #fig.suptitle(f'Dataset used for Training: {DatasetNames[nSubset]}', fontweight='bold')
  plt.tight_layout()
  #plt.savefig(f'TESTRatios_Kernels-vs-{xLabel}_{yLabel}_{DatasetNames[nSubset]}.png', dpi=300, format='png')
  #break

if saveOrShow == "show":
  plt.show()
elif saveOrShow == "save":
  plt.savefig(f'Ratios-vs-{xLabel}_{yLabel}.png', dpi=300, format='png')























