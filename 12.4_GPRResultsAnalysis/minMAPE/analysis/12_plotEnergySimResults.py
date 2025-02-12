import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pwd = "/home/rstric2s/current_sim/Paper_Octane-3_NN-predictor/opt_with_GPR-Model/minMAPE"
thisDir = os.path.basename(pwd)

statisticsFileName = os.path.join(pwd, "StatsEnergies.csv")
avgRMSEFileName = os.path.join(pwd, "AvgRMSEEnergies.csv")

dfStats = pd.read_csv(statisticsFileName)
dfStats = dfStats.drop(dfStats.columns[0], axis=1)
#print(f'{dfStats}')
dfAvgRMSEs = pd.read_csv(avgRMSEFileName)
dfAvgRMSEs = dfAvgRMSEs.drop(dfAvgRMSEs.columns[0], axis=1)
#print(f'{dfAvgRMSEs}')

targets = dfStats["target"].to_numpy()
#print(f'{targets}')
sortIDX = targets.argsort()
#print(f'{sortIDX}')
sortedTargets = []
for idx in sortIDX:
  sortedTargets.append(targets[idx])
#print(f'{sortedTargets}')

plt.plot(sortedTargets, '-x', label="targets")
#plt.show()

for i in range(0, 10): #hardcoded :(
  thisEnergies = dfStats[f'{thisDir}-{i}'].to_numpy()
  thisSortedEnergies = []
  for idx in sortIDX:
    thisSortedEnergies.append(thisEnergies[idx])
  
  thisAvgRMSE = np.round(float(dfAvgRMSEs["Avg. RMSE"][i]), 4)
  plt.plot(thisSortedEnergies, '-.', label=f'{thisDir}-{i}, avg. RMSE: {thisAvgRMSE}')

plt.legend()  
#plt.show()
plt.savefig(f'optedEnergies-vs-Targets_{thisDir}.png', dpi=300, format='png')
