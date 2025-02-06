import pandas as pd

import os


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
  
  
## min MAPE
dfThisStatistics = dfStatistics
minMapeIDXs = []
for i in range(0, 10):
  idxMinMAPE = dfThisStatistics['mape'].idxmin()
  #print(f'{idxMinMAPE}')
  #minMAPE = dfThisStatistics['mape'].min()
  #print(f'{minMAPE}')
  #minMAPERow = dfThisStatistics.iloc[idxMinMAPE]
  #print(f'Min MAPE Entry:\n{minMAPERow}\n')
  minMapeIDXs.append(idxMinMAPE)
  dfThisStatistics = dfThisStatistics.drop([idxMinMAPE])

print(f'{minMapeIDXs}')

## max R2
dfThisStatistics = dfStatistics
maxR2IDXs = []
for i in range(0, 10):
  idxMaxR2 = dfThisStatistics['r2'].idxmax()
  #print(f'{idxMaxR2}')
  #maxR2 = dfThisStatistics['r2'].max()
  #print(f'{maxR2}')
  #maxR2Row = dfThisStatistics.iloc[idxMaxR2]
  #print(f'Max R2 Entry:\n{maxR2Row}\n')
  maxR2IDXs.append(idxMaxR2)
  dfThisStatistics = dfThisStatistics.drop([idxMaxR2])

#print(f'{maxR2IDXs}')
print(f'Min MAPE Models:')
for thisID in minMapeIDXs:
  print(f'MAPE: {dfStatistics.iloc[thisID]["mape"]}  \tR2: {dfStatistics.iloc[thisID]["r2"]}')
  print(f'  Dataset: {dfStatistics.iloc[thisID]["dataset"]}, Kernel: {dfStatistics.iloc[thisID]["kernel"]}, Ratio: {dfStatistics.iloc[thisID]["ratio"]}, RndInt: {dfStatistics.iloc[thisID]["rndint"]}')
  print(f'')
  if thisID in maxR2IDXs:
    print(f'{thisID}')
    
print(f'\nMax R2 Models:')
for thisID in maxR2IDXs:
  print(f'R2: {dfStatistics.iloc[thisID]["r2"]}    \tMAPE: {dfStatistics.iloc[thisID]["mape"]}')
  print(f'  Dataset: {dfStatistics.iloc[thisID]["dataset"]}, Kernel: {dfStatistics.iloc[thisID]["kernel"]}, Ratio: {dfStatistics.iloc[thisID]["ratio"]}, RndInt: {dfStatistics.iloc[thisID]["rndint"]}')
  print(f'')
