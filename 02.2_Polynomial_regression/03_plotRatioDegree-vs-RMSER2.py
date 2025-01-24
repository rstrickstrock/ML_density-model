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
  fig, axd = plt.subplot_mosaic([['RMSE', 'R2', 'AvgByDegree']],  
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
    AvgRMSE.append(np.mean(thisSubsetDegree["rmse"].to_numpy()))
    AvgRMSEerr.append(np.std(thisSubsetDegree["rmse"].to_numpy()))
    AvgR2.append(np.mean(thisSubsetDegree["r2"].to_numpy()))
    AvgR2err.append(np.std(thisSubsetDegree["r2"].to_numpy()))
    thisX = []
    thisRMSE = []
    thisRMSEerr = []
    thisR2 = []
    thisR2err = []
    for ratio in thisSubsetDegree["ratio"].unique():
      thisX.append(1-ratio)
      thisSubsetDegreeRatio = thisSubsetDegree[thisSubsetDegree["ratio"] == ratio]
      thisRMSE.append(np.mean(thisSubsetDegreeRatio["rmse"].to_numpy()))
      thisRMSEerr.append(np.std(thisSubsetDegreeRatio["rmse"].to_numpy()))
      thisR2.append(np.mean(thisSubsetDegreeRatio["r2"].to_numpy()))
      thisR2err.append(np.std(thisSubsetDegreeRatio["r2"].to_numpy()))
    axd['RMSE'].errorbar(thisX, thisRMSE, yerr=thisRMSEerr, label=f'polyn. degree = {d}', marker=markers[d-1], color=colors[d-1], ls='-.')
    axd['R2'].errorbar(thisX, thisR2, yerr=thisR2err, label=f'polyn. degree = {d}', marker=markers[d-1], color=colors[d-1], ls='-.')
    
  axd["RMSE"].legend()
  axd["RMSE"].set_ylabel("RMSE", fontweight='bold')
  axd["RMSE"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["RMSE"].set_title("Avg. RMSE per Training-/Testdata split", fontweight='bold')
  #axd["RMSE"].set_ylim([minRMSE, maxRMSE])
  axd["R2"].legend()
  axd["R2"].set_xlabel("% of Dataset used for Training", fontweight='bold')
  axd["R2"].set_ylabel("R2", fontweight='bold')
  axd["R2"].set_title("Avg. R2 per Training-/Testdata split", fontweight='bold')
  axd["R2"].set_ylim([-1.0, 1.0])
  
  axd['AvgByDegree'].errorbar(DegreesForPlotting, AvgRMSE, yerr=AvgRMSEerr, label=f'Average RMSEs', marker='o', color='#069AF3', ls='-.')
  axd['AvgByDegree'].legend(bbox_to_anchor=(0.22,0.05), loc='center')
  axd["AvgByDegree"].set_ylabel("RMSE", c="#069AF3", fontweight='bold')
  axd["AvgByDegree"].set_xlabel("Polynomial Degree", fontweight='bold')
  axd["AvgByDegree"].set_title("Avg. RMSE/R2 per degree", fontweight='bold')
  axd["AvgByDegree"].set_xticks(DegreesForPlotting)
  axd["AvgByDegree"].tick_params(axis='y', color="#069AF3", which='both')
  axd["AvgByDegree"].spines['left'].set_color("#069AF3")
  axd2 = axd["AvgByDegree"].twinx()
  axd2.errorbar(DegreesForPlotting, AvgR2, yerr=AvgR2err, label=f'Average R2s', marker='o', color='#F97306', ls='-.')
  axd2.legend(bbox_to_anchor=(0.8,0.05), loc='center')
  axd2.set_ylabel("R2", c="#F97306", fontweight='bold')
  axd2.set_ylim([-1.0, 1.0])
  axd2.spines['left'].set_color("#069AF3")
  axd2.spines['right'].set_color("#F97306")
  axd2.tick_params(axis='y', color="#F97306", which='both')
  
  fig.suptitle(f'Dataset used for Training: {DatasetNames[deg]}', fontweight='bold')
  plt.tight_layout()
  #break
plt.show()
























