import matplotlib.pyplot as plt
import pandas as pd

import os
import glob


statisticsFile = 'Stats.csv'
#metrictype = "rmse"
metrictype = "mape"

if metrictype is "rmse":
  xLabel = "RMSE"
elif metrictype is "mape":
  xLabel = "MAPE"
else:
  print(f'Please set \'metrictype\' to "rmse" or "mape". (Is: {metrictype}). Exit.')
  exit()
  
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

#print(f'{dfStatistics}')
minMETRIC = dfStatistics[f'{metrictype}'].min()
minMETRIC = minMETRIC - 0.01*minMETRIC
maxMETRIC = dfStatistics[f'{metrictype}'].max()
maxMETRIC = maxMETRIC + 0.01*maxMETRIC
minR2 = dfStatistics['r2'].min()
minR2 = minR2 - 0.001*minR2
maxR2 = dfStatistics['r2'].max()
maxR2 = maxR2 + 0.01*maxR2

subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]

## plots
gs_kw = dict(width_ratios=[2, 1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['AllInOne', 'Grid1296', 'Sobol1'], 
                               ['AllInOne', 'Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(18.0, 9.0))

axd["AllInOne"].scatter(subsetGrid1296[f'{metrictype}'], subsetGrid1296["r2"], label="Grid1296", c="#332288", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid2401[f'{metrictype}'], subsetGrid2401["r2"], label="Grid2401", c="#88CCEE", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol1[f'{metrictype}'], subsetSobol1["r2"], label="Sobol1", c="#DDCC77", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol2[f'{metrictype}'], subsetSobol2["r2"], label="Sobol2", c="#117733", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].legend()
axd["AllInOne"].set(xlabel=f'{xLabel}', ylabel="R2")
axd["AllInOne"].set_title("All In One", fontweight='bold')
axd["AllInOne"].set_xlim([minMETRIC, maxMETRIC])
axd["AllInOne"].set_ylim([minR2, maxR2])

axd["Grid1296"].scatter(subsetGrid1296[f'{metrictype}'], subsetGrid1296["r2"], label="Grid1296", c="#332288", marker='o')#, edgecolor="#44AA99")
axd["Grid1296"].legend()
axd["Grid1296"].set(xlabel=f'{xLabel}', ylabel="R2")
axd["Grid1296"].set_title("Grid1296", fontweight='bold')
axd["Grid1296"].set_xlim([minMETRIC, maxMETRIC])
axd["Grid1296"].set_ylim([minR2, maxR2])

axd["Grid2401"].scatter(subsetGrid2401[f'{metrictype}'], subsetGrid2401["r2"], label="Grid2401", c="#88CCEE", marker='o')#, edgecolor="#44AA99")
axd["Grid2401"].legend()
axd["Grid2401"].set(xlabel=f'{xLabel}', ylabel="R2")
axd["Grid2401"].set_title("Grid2401", fontweight='bold')
axd["Grid2401"].set_xlim([minMETRIC, maxMETRIC])
axd["Grid2401"].set_ylim([minR2, maxR2])

axd["Sobol1"].scatter(subsetSobol1[f'{metrictype}'], subsetSobol1["r2"], label="Sobol1", c="#DDCC77", marker='o')#, edgecolor="#44AA99")
axd["Sobol1"].legend()
axd["Sobol1"].set(xlabel=f'{xLabel}', ylabel="R2")
axd["Sobol1"].set_title("Sobol1", fontweight='bold')
axd["Sobol1"].set_xlim([minMETRIC, maxMETRIC])
axd["Sobol1"].set_ylim([minR2, maxR2])

axd["Sobol2"].scatter(subsetSobol2[f'{metrictype}'], subsetSobol2["r2"], label="Sobol2", c="#117733", marker='o')#, edgecolor="#44AA99")
axd["Sobol2"].legend()
axd["Sobol2"].set(xlabel=f'{xLabel}', ylabel="R2")
axd["Sobol2"].set_title("Sobol2", fontweight='bold')
axd["Sobol2"].set_xlim([minMETRIC, maxMETRIC])
axd["Sobol2"].set_ylim([minR2, maxR2])

plt.tight_layout()
plt.show()

#plt.savefig(f'{xLabel}vsR2.png', dpi=300, format='png')



























