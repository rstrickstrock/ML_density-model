import pandas as pd
import glob
import os

pwd = os.getcwd()
statsFiles = glob.glob(os.path.join(pwd, "StatsPart-*"))
#print(f'{statsFiles}')

mergedStatisticsFileName = 'Stats.csv'

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "learning_rate": [],
                             "epoch": [],
                             "rmse": [],
                             "mape": [],
                             "r2": []})

for statisticsFile in statsFiles:
  #print(f'{statisticsFile}')
  thisStats = pd.read_csv(statisticsFile)
  #print(f'{thisStats}')
  thisStats = thisStats.drop(thisStats.columns[0], axis=1)
  #print(f'{thisStats}')

  dfStatistics = pd.concat([dfStatistics, thisStats], ignore_index=True)


dfStatisticsSorted = pd.DataFrame({"ratio": [],
                                   "rndint": [],
                                   "dataset": [],
                                   "learning_rate": [],
                                   "epoch": [],
                                   "rmse": [],
                                   "mape": [],
                                   "r2": []})
                                   
ratios = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
for ratio in ratios:
  #print(f'{ratio}')
  dfThisStatistics = dfStatistics[dfStatistics["ratio"] == ratio]
  #print(f'{dfThisStatistics}')
  dfStatisticsSorted = pd.concat([dfStatisticsSorted, dfThisStatistics], ignore_index=True)
  
if os.path.exists(mergedStatisticsFileName):
  os.remove(mergedStatisticsFileName)
  print(f'Removed existing statistics file: \'{mergedStatisticsFileName}\'.')
dfStatisticsSorted.to_csv(mergedStatisticsFileName)
print(f'Merged statistics to file: \'{mergedStatisticsFileName}\'.')
print(f'{dfStatisticsSorted}')



