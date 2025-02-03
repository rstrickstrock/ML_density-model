import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import glob


statisticsFile = 'Stats.csv'
metric1 = "rmse"
#metric1 = "mape"
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


if metric1 is "rmse":
  xLabel = "RMSE"
  minMETRIC1 = dfStatistics[f'{metric1}'].min()
  minMETRIC1 = minMETRIC1 - 0.01*minMETRIC1
  maxMETRIC1 = 100
elif metric1 is "mape":
  xLabel = "MAPE"
  minMETRIC1 = dfStatistics[f'{metric1}'].min()
  minMETRIC1 = minMETRIC1 - 0.01*minMETRIC1
  maxMETRIC1 = 0.13 
elif metric1 is "r2":
  xLabel = "R2"
  maxMETRIC1 = 1.05
  minMETRIC1 = 0.0
else:
  print(f'Please set \'metric1\' to "rmse", "r2" or "mape". (Is: {metric1}). Exit.')
  exit()
  
if metric2 is "rmse":
  yLabel = "RMSE"
  minMETRIC2 = dfStatistics[f'{metric2}'].min()
  minMETRIC2 = minMETRIC2 - 0.01*minMETRIC2
  maxMETRIC2 = 100
elif metric2 is "mape":
  yLabel = "MAPE"
  minMETRIC2 = dfStatistics[f'{metric2}'].min()
  minMETRIC2 = minMETRIC2 - 0.01*minMETRIC2
  maxMETRIC2 = 0.13
elif metric2 is "r2":
  yLabel = "R2"
  maxMETRIC2 = 1.05
  minMETRIC2 = 0.0
else:
  print(f'Please set \'metric2\' to "rmse", "r2" or "mape". (Is: {metric2}). Exit.')
  exit()

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
#print(f'Grid1296')
#print(f'mean RMSE: {np.mean(subsetGrid1296["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetGrid1296["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetGrid1296["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetGrid1296["r2"].to_numpy())}\n')
#print(f'mean RMSE: {np.mean(subsetGrid1296["rmse"].to_numpy())}')
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
#print(f'Grid2401')
#print(f'mean RMSE: {np.mean(subsetGrid2401["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetGrid2401["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetGrid2401["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetGrid2401["r2"].to_numpy())}\n')
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
#print(f'Sobol1')
#print(f'mean RMSE: {np.mean(subsetSobol1["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetSobol1["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetSobol1["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetSobol1["r2"].to_numpy())}\n')
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]
#print(f'Sobol2')
#print(f'mean RMSE: {np.mean(subsetSobol2["rmse"].to_numpy())}')
#print(f'stddev RMSE: {np.std(subsetSobol2["rmse"].to_numpy())}')
#print(f'mean R2: {np.mean(subsetSobol2["r2"].to_numpy())}')
#print(f'stddev R2: {np.std(subsetSobol2["r2"].to_numpy())}\n')
if False:
  print(f'Grid1296')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.mean(subsetGrid1296[subsetGrid1296["degree"] == d]["r2"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetGrid1296[subsetGrid1296["degree"] == d]["r2"].to_numpy()), 4)} \\\\'
    )
  print('')
  print(f'Grid2401')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.mean(subsetGrid2401[subsetGrid2401["degree"] == d]["r2"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetGrid2401[subsetGrid2401["degree"] == d]["r2"].to_numpy()), 4)} \\\\'
    )
  print('')
  print(f'Sobol1')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.mean(subsetSobol1[subsetSobol1["degree"] == d]["r2"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetSobol1[subsetSobol1["degree"] == d]["r2"].to_numpy()), 4)} \\\\'
    )
  print('')
  print(f'Sobol2')
  for d in range(1, 11):  # Loop through degrees 1 to 10
    print(
        f'& {d} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["degree"] == d]["rmse"].to_numpy()), 4)} & '
        f'{np.round(np.mean(subsetSobol2[subsetSobol2["degree"] == d]["r2"].to_numpy()), 4)} & '
        f'{np.round(np.std(subsetSobol2[subsetSobol2["degree"] == d]["r2"].to_numpy()), 4)} \\\\'
    )
  print('')


## plots
degs = [5, 5, 6, 6]
datasetSubsets = [subsetGrid1296, subsetGrid2401, subsetSobol1, subsetSobol2]
#print(f'{datasetSubsets[0]}')
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']
markers = ['1', '2', '3', '4', 'x', '+']
DatasetNames = ['Grid1296', 'Grid2401', 'Sobol1', 'Sobol2']
for deg in range(0, len(degs)):
  #print(f'deg: {deg}')
  thisDataSubset = datasetSubsets[deg]
  gs_kw = dict(width_ratios=[1, 1, 1], height_ratios=[1])
  fig, axd = plt.subplot_mosaic([['METRIC1', 'METRIC2', 'AvgByDegree']],  
                                 gridspec_kw=gs_kw, figsize=(15.0, 5.0))

  DegreesForPlotting = []
  AvgRMSE = []
  AvgRMSEerr = []
  AvgR2 = []
  AvgR2err = []
  for d in range(1, degs[deg]+1):
    thisSubsetDegree = thisDataSubset[thisDataSubset["degree"] == d]
    #print(f'{thisSubsetDegree}')
    DegreesForPlotting.append(d)
    AvgRMSE.append(np.mean(thisSubsetDegree[f'{metric1}'].to_numpy()))
    AvgRMSEerr.append(np.std(thisSubsetDegree[f'{metric1}'].to_numpy()))
    AvgR2.append(np.mean(thisSubsetDegree[f'{metric2}'].to_numpy()))
    AvgR2err.append(np.std(thisSubsetDegree[f'{metric2}'].to_numpy()))
    thisX = []
    thisRMSE = []
    thisRMSEerr = []
    thisR2 = []
    thisR2err = []
    for ratio in thisSubsetDegree["ratio"].unique():
      thisX.append(1-ratio)
      thisSubsetDegreeRatio = thisSubsetDegree[thisSubsetDegree["ratio"] == ratio]
      thisRMSE.append(np.mean(thisSubsetDegreeRatio[f'{metric1}'].to_numpy()))
      thisRMSEerr.append(np.std(thisSubsetDegreeRatio[f'{metric1}'].to_numpy()))
      thisR2.append(np.mean(thisSubsetDegreeRatio[f'{metric2}'].to_numpy()))
      thisR2err.append(np.std(thisSubsetDegreeRatio[f'{metric2}'].to_numpy()))
    axd['METRIC1'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'polyn. degree = {d}', marker=markers[d-1], color=colors[d-1], ls='-.')
    axd['METRIC2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'polyn. degree = {d}', marker=markers[d-1], color=colors[d-1], ls='-.')
    
  axd["METRIC1"].legend()
  axd["METRIC1"].set_ylabel(f'{xLabel}', fontweight='bold')
  axd["METRIC1"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC1"].set_title(f'Avg. {xLabel} per Training-/Testdata split', fontweight='bold')
  #axd["METRIC1"].set_ylim([minRMSE, maxRMSE])
  axd["METRIC2"].legend()
  axd["METRIC2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["METRIC2"].set_ylabel(f'{yLabel}', fontweight='bold')
  axd["METRIC2"].set_title(f'Avg. {yLabel} per Training-/Testdata split', fontweight='bold')
  axd["METRIC2"].set_ylim([-1.0, 1.0])
  
  axd['AvgByDegree'].errorbar(DegreesForPlotting, AvgRMSE, yerr=AvgRMSEerr, label=f'Average RMSEs', marker='o', color='#069AF3', ls='-.')
  axd['AvgByDegree'].legend(bbox_to_anchor=(0.22,0.05), loc='center')
  axd["AvgByDegree"].set_ylabel(f'{xLabel}', c="#069AF3", fontweight='bold')
  axd["AvgByDegree"].set_xlabel("Polynomial Degree", fontweight='bold')
  axd["AvgByDegree"].set_title(f'Avg. {xLabel}/{yLabel} per degree', fontweight='bold')
  axd["AvgByDegree"].set_xticks(DegreesForPlotting)
  axd["AvgByDegree"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByDegree"].spines['left'].set_color("#069AF3")
  axd2 = axd["AvgByDegree"].twinx()
  axd2.errorbar(DegreesForPlotting, AvgR2, yerr=AvgR2err, label=f'Average R2s', marker='o', color='#F97306', ls='-.')
  axd2.legend(bbox_to_anchor=(0.8,0.05), loc='center')
  axd2.set_ylabel(f'{yLabel}', c="#F97306", fontweight='bold')
  axd2.set_ylim([-1.0, 1.0])
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  
  fig.suptitle(f'Dataset used for Training: {DatasetNames[deg]}', fontweight='bold')
  plt.tight_layout()
  #break
plt.show()
























