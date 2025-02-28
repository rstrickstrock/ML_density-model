import pandas as pd
import glob
import os

pwd = os.getcwd()
trainedModelsDirs = glob.glob(os.path.join(pwd, "trainedModels/*"))
#print(f'{trainedModelsDirs}')

mergedStatisticsFileName = 'Stats.csv'

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "learning_rate": [],
                             "epoch": [],
                             "mape": [],
                             "r2": []})

thisLearningRate = 0.001
for trainedModelsDir in trainedModelsDirs:
  modelNames = glob.glob(os.path.join(trainedModelsDir,"*"))
  #print(f'{modelNames}')
  for modelName in modelNames:
    thisModelname = os.path.basename(modelName)
    #print(f'{thisModelname}')
    thisRatio = float(thisModelname.split("-")[1])
    #print(f'thisRatio: {thisRatio}')
    thisRndInt = int(thisModelname.split("-")[2])
    #print(f'thisRndInt: {thisRndInt}')
    thisDataSet = str(thisModelname.split("_")[0].split("-")[3])
    #print(f'thisDataSet: {thisDataSet}')
    thisEpoch = int(thisModelname.split("_")[1])
    #print(f'thisEpoch: {thisEpoch}')
    thisMAPE = float(thisModelname.split("_")[2])
    #print(f'thisMAPE: {thisMAPE}')
    thisR2 = float(thisModelname.split("_")[3].split(".pth")[0])
    #print(f'thisR2: {thisR2}')
    dfThisStatistics = pd.DataFrame({"ratio": [thisRatio],
                                     "rndint": [thisRndInt],
                                     "dataset": [thisDataSet],
                                     "learning_rate": [thisLearningRate],
                                     "epoch": [thisEpoch],
                                     "mape": [thisMAPE],
                                     "r2": [thisR2]})
    dfStatistics = pd.concat([dfStatistics, dfThisStatistics], ignore_index=True)

#print(f'{dfStatistics}')


dfStatisticsSorted = pd.DataFrame({"ratio": [],
                                   "rndint": [],
                                   "dataset": [],
                                   "learning_rate": [],
                                   "epoch": [],
                                   "mape": [],
                                   "r2": []})
                                   
ratios = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
for ratio in ratios:
  #print(f'{ratio}')
  dfThisStatistics = dfStatistics[dfStatistics["ratio"] == float(ratio)]
  #print(f'{dfThisStatistics}')
  dfStatisticsSorted = pd.concat([dfStatisticsSorted, dfThisStatistics], ignore_index=True)
  
if os.path.exists(mergedStatisticsFileName):
  os.remove(mergedStatisticsFileName)
  print(f'Removed existing statistics file: \'{mergedStatisticsFileName}\'.')
dfStatisticsSorted.to_csv(mergedStatisticsFileName)
print(f'Merged statistics to file: \'{mergedStatisticsFileName}\'.')
print(f'{dfStatisticsSorted}')
