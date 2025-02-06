import pandas as pd
import os

statisticsFilesNames = ['Stats-0.csv', 'Stats-1.csv', 'Stats-2.csv', 'Stats-3.csv', 'Stats-4.csv', 'Stats-5.csv', 'Stats-6.csv', 'Stats-7.csv', 'Stats-8.csv', 'Stats-9.csv']
mergedStatisticsFileName = 'Stats.csv'

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "kernel": [],
                             "length_scale": [],
                             "nu": [],
                             "alpha": [],
                             "periodicity": [],
                             "rmse": [],
                             "mape": [],
                             "r2": []})

for statisticsFileName in statisticsFilesNames:
  thisStats = pd.read_csv(statisticsFileName)
  #print(f'{thisStats}')
  thisStats = thisStats.drop(thisStats.columns[0], axis=1)
  #print(f'{thisStats}')

  dfStatistics = pd.concat([dfStatistics, thisStats], ignore_index=True)
  
if os.path.exists(mergedStatisticsFileName):
  os.remove(mergedStatisticsFileName)
  print(f'Removed existing statistics file: \'{mergedStatisticsFileName}\'.')
dfStatistics.to_csv(mergedStatisticsFileName)
print(f'Merged statistics to file: \'{mergedStatisticsFileName}\'.')
print(f'{dfStatistics}')
