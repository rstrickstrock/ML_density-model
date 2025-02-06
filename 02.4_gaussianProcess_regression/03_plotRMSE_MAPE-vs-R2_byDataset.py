import matplotlib.pyplot as plt
import pandas as pd

import os
import glob


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
  maxMETRIC1 = 0.13 
elif metric1 == "r2":
  xLabel = "R2"
  maxMETRIC1 = 1.05
  minMETRIC1 = 0.0
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
  maxMETRIC2 = 0.13
elif metric2 == "r2":
  yLabel = "R2"
  maxMETRIC2 = 1.05
  minMETRIC2 = 0.0
else:
  print(f'Please set \'metric2\' to "rmse", "r2" or "mape". (Is: {metric2}). Exit.')
  exit()


subsetGrid1296 = dfStatistics[dfStatistics["dataset"] == "Grid1296"]
subsetGrid2401 = dfStatistics[dfStatistics["dataset"] == "Grid2401"]
subsetSobol1 = dfStatistics[dfStatistics["dataset"] == "Sobol1"]
subsetSobol2 = dfStatistics[dfStatistics["dataset"] == "Sobol2"]

## plots
gs_kw = dict(width_ratios=[2, 1, 1], height_ratios=[1, 1])
fig, axd = plt.subplot_mosaic([['AllInOne', 'Grid1296', 'Sobol1'], 
                               ['AllInOne', 'Grid2401', 'Sobol2']], 
                               gridspec_kw=gs_kw, figsize=(18.0, 9.0))

axd["AllInOne"].scatter(subsetGrid1296[f'{metric1}'], subsetGrid1296[f'{metric2}'], label="Grid1296", c="#332288", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetGrid2401[f'{metric1}'], subsetGrid2401[f'{metric2}'], label="Grid2401", c="#88CCEE", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol1[f'{metric1}'], subsetSobol1[f'{metric2}'], label="Sobol1", c="#DDCC77", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].scatter(subsetSobol2[f'{metric1}'], subsetSobol2[f'{metric2}'], label="Sobol2", c="#117733", marker='o')#, edgecolor="#44AA99")
axd["AllInOne"].legend()
axd["AllInOne"].set(xlabel=f'{xLabel}', ylabel=f'{yLabel}')
axd["AllInOne"].set_title("All In One", fontweight='bold')
axd["AllInOne"].set_xlim([minMETRIC1, maxMETRIC1])
axd["AllInOne"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Grid1296"].scatter(subsetGrid1296[f'{metric1}'], subsetGrid1296[f'{metric2}'], label="Grid1296", c="#332288", marker='o')#, edgecolor="#44AA99")
axd["Grid1296"].legend()
axd["Grid1296"].set(xlabel=f'{xLabel}', ylabel=f'{yLabel}')
axd["Grid1296"].set_title("Grid1296", fontweight='bold')
axd["Grid1296"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Grid1296"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Grid2401"].scatter(subsetGrid2401[f'{metric1}'], subsetGrid2401[f'{metric2}'], label="Grid2401", c="#88CCEE", marker='o')#, edgecolor="#44AA99")
axd["Grid2401"].legend()
axd["Grid2401"].set(xlabel=f'{xLabel}', ylabel=f'{yLabel}')
axd["Grid2401"].set_title("Grid2401", fontweight='bold')
axd["Grid2401"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Grid2401"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Sobol1"].scatter(subsetSobol1[f'{metric1}'], subsetSobol1[f'{metric2}'], label="Sobol1", c="#DDCC77", marker='o')#, edgecolor="#44AA99")
axd["Sobol1"].legend()
axd["Sobol1"].set(xlabel=f'{xLabel}', ylabel=f'{yLabel}')
axd["Sobol1"].set_title("Sobol1", fontweight='bold')
axd["Sobol1"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Sobol1"].set_ylim([minMETRIC2, maxMETRIC2])

axd["Sobol2"].scatter(subsetSobol2[f'{metric1}'], subsetSobol2[f'{metric2}'], label="Sobol2", c="#117733", marker='o')#, edgecolor="#44AA99")
axd["Sobol2"].legend()
axd["Sobol2"].set(xlabel=f'{xLabel}', ylabel=f'{yLabel}')
axd["Sobol2"].set_title("Sobol2", fontweight='bold')
axd["Sobol2"].set_xlim([minMETRIC1, maxMETRIC1])
axd["Sobol2"].set_ylim([minMETRIC2, maxMETRIC2])

plt.tight_layout()
#plt.show()

plt.savefig(f'{xLabel}-vs-{yLabel}.png', dpi=300, format='png')



























