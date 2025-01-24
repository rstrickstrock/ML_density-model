from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import os
import glob
import numpy as np
import pickle

from matplotlib import pyplot as plt

resultDir = f'trainedModels'
optParamFile = 'optimized_parameters.csv'
###
predictionsFile = 'yPredictionsUsingPrevOptParams.csv'
combinedDataFile = 'DiffRMSER2.csv'
statisticsFile = 'Stats.csv'

cwd = os.getcwd()

createPredictionsFile = True
if os.path.isfile(predictionsFile):
  createPredictionsFile = False
  try:
    dfPredictions = pd.read_csv(predictionsFile)
  except:
    print(f'Can not open \'{predictionsFile}\'. Exit.')
    exit()
  else:
    try:
      dfPredictions = dfPredictions.drop(columns=["Unnamed: 0"])
    except:
      print(f'Something went wrong with\'dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])\'.')
    else:
      #print(f'{dfPredictions}')
      pass
else:
  ratioDirs = glob.glob(os.path.join(resultDir, '*'))

  optParams = pd.read_csv(optParamFile)
  #print(f'{optParams}')
  xOpt = optParams.drop('density', axis=1)
  #print(f'{xOpt}')
  yOpt = optParams['density']
  #print(f'{yOpt}')
  try:
    yOpt = float(yOpt.to_numpy())
  except:
    print(f'Could not float(yOpt.to_numpy())')

  dfPredictions = pd.DataFrame({"ratio":[],
                                "rndint":[],
                                "dataset":[],
                                "prediction":[],
                                "target":[],
                                "diff":[]})

  for ratioDir in ratioDirs:
    #print(f'{ratioDir}')
    try:
      thisRatio = float(os.path.basename(ratioDir))
    except:
      print(f'something went wrong with \'float(os.path.basename(ratioDir))\'. Exit.')
      exit()
    else:
      #print(f'{thisRatio}')
      pass

    os.chdir(ratioDir)
    modelFiles = glob.glob(os.path.join(os.getcwd(),'trained_model*'))
    #print(f'{modelFiles}')
    for modelFile in modelFiles:
      #print(f'{modelFile}')
      try:
        thisRndInt = int(os.path.basename(modelFile).split("_")[3].split(".")[0])
      except:
        print(f'Could not get RndInt for modelfile:\n{modelFile}')
      else:
        #print(f'{thisRndInt}')
        pass
  
      try:
        thisDataset = str(os.path.basename(modelFile).split("_")[1][5:])
      except:
        print(f'Could not get thisDataset for modelfile:\n{modelFile}')
      else:
        #print(f'{thisDataset}')
        pass
    
      with open(modelFile, "rb") as thisFile:
        try:
          thisModel = pickle.load(thisFile)
        except:
          print(f'Could not load modelfile:\n{modelFile}')

      try:
        thisPrediction = thisModel.predict(xOpt)
      except:
        print(f'Could not predict thisPrediction with modelfile:\n{modelFile}')
      else:
        thisPrediction = float(thisPrediction)
        #print(f'thisPrediction: {thisPrediction}')
  
      try:  
        thisDiff = yOpt - thisPrediction
      except:
        print(f'Could not calc thisDiff for modelfile:\n{modelFile}')
    
      try:
        newResultsEntry = pd.DataFrame({"ratio":[thisRatio],
                                        "rndint":[thisRndInt],
                                        "dataset":[thisDataset],
                                        "prediction":[thisPrediction],
                                        "target":[yOpt],
                                        "diff":[thisDiff]})
      except:
        print(f'something went wrong with creating the newResultsEntry for modelfile:\n{modelFile}')
      else:
        try:
          dfPredictions = pd.concat([dfPredictions, newResultsEntry], ignore_index=True)
        except:
          print(f'something went wrong when concating DFs for modefile:\n{modelFile}')
        else:
          pass

      #print(f'{dfPredictions}')
  
    os.chdir(cwd)
    #print(f'{dfPredictions}')

  if os.path.exists(predictionsFile):
    os.remove(predictionsFile)
    print(f'Removed existing statistics file: \'{predictionsFile}\'.')
  dfPredictions.to_csv(predictionsFile)
  print(f'Wrote statistics to file: \'{predictionsFile}\'.')
#print(f'{dfPredictions}')


createCombinedDataFile = True
if os.path.isfile(combinedDataFile):
  createCombinedDataFile = False
  try:
    dfCombinedData = pd.read_csv(combinedDataFile)
  except:
    print(f'Can not open \'{combinedDataFile}\'. Exit.')
    exit()
  else:
    try:
      dfCombinedData = dfCombinedData.drop(columns=["Unnamed: 0"])
    except:
      print(f'Something went wrong with\'dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])\'.')
    else:
      #print(f'{dfCombinedData}')
      pass

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

## plot diff vs RMSE && diff vs R2
if createCombinedDataFile:
  dfCombinedData = pd.DataFrame({"ratio":[],
                                 "rndint":[],
                                 "dataset":[],
                                 "rmse": [],
                                 "r2": [],
                                 "prediction":[],
                                 "target":[],
                                 "diff":[]})
  
  # get corresponding RMSEs/R2s from dfStatistics to every Diff from dfPredictions
  for i in range(0, len(dfPredictions)):
    #print(f'{dfPredictions.iloc[i]}')
    try:
      ## get entry from predictions
      thisPredictionEntry = dfPredictions.iloc[i]
    except:
      print(f'Could not do \'thisPredictionEntry = dfPredictions.iloc[i]\' for\ni = {i}. Exit!')
      exit()
    else:
      #print(f'{thisPredictionEntry}')
      pass
    try:
      ## get the diff (target - prediction) for this model
      thisDiff = thisPredictionEntry["diff"]
    except:
      print(f'Could not do \'thisDiff = thisPredictionEntry["diff"]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    else:
      #print(f'{thisDiff}')
      pass
    try:
      thisPrediction = thisPredictionEntry["prediction"]
    except:
      print(f'Could not do \'thisPrediction = thisPredictionEntry["prediction"]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    else:
      #print(f'{thisPrediction}')
      pass
  
    ## get model settings to find RMSE and R2 in dfStatistics
    try:
      thisRatio = thisPredictionEntry["ratio"]
    except:
      print(f'Could not get \'thisRatio = thisPredictionEntry["ratio"]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    try:
      thisRndInt = thisPredictionEntry["rndint"]
    except:
      print(f'Could not get \'thisRndInt = thisPredictionEntry["rndint"]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    try:
      thisDataset = thisPredictionEntry["dataset"]
    except:
      print(f'Could not get \'thisDataset = thisPredictionEntry["dataset"]\' for\nthisPredictionEntry = {thisPredictionEntry}')
  
    ## find the corresponding model entry in dfStatistics
    try:
      ratioSubset = dfStatistics[dfStatistics["ratio"] == thisRatio]
    except:
      print(f'Could not get \'ratioSubset = dfStatistics[dfStatistics["ratio"] == thisRatio]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    else:
      #print(f'{ratioSubset}')
      pass
    try:
      rndIntSubset = ratioSubset[ratioSubset["rndint"] == thisRndInt]
    except:
      print(f'Could not get \'rndIntSubset = ratioSubset[ratioSubset["rndint"] == thisRndInt]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    try:
      datasetSubset = rndIntSubset[rndIntSubset["dataset"] == thisDataset]
    except:
      print(f'Could not get \'datasetSubset = rndIntSubset[rndIntSubset["dataset"] == thisDataset]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    else:
      #print(f'{datasetSubset}')
      pass
    
    ## get RMSE and R2 from dfStatistics entry  
    try:
      thisRMSE = datasetSubset["rmse"]
    except:
      print(f'Could not get \'thisRMSE = datasetSubset["rmse"]\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {datasetSubset}')
    else:
      #print(f'{thisRMSE}')
      #print(f'{thisRMSE.to_numpy()}')
      #print(f'{float(thisRMSE.to_numpy())}')
      try:
        thisRMSE = float(thisRMSE.to_numpy())
      except:
        print(f'Could not cast \'thisRMSE = float(thisRMSE.to_numpy())\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {datasetSubset}')
      else:
        #print(f'{thisRMSE}')
        pass
      pass
    try:
      thisR2 = datasetSubset["r2"]
    except:
      print(f'Could not get \'thisR2 = datasetSubset["r2"]\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {datasetSubset}')
    else:
      #print(f'{thisR2}')
      try:
        thisR2 = float(thisR2.to_numpy())
      except:
        print(f'Could not cast \'thisRMSE = float(thisR2.to_numpy())\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {datasetSubset}')
      else:
        #print(f'{thisR2}')
        pass
      pass
  
    ## create ne df entry for dfCombinedData
    try:
      thisCombinedDataEntry = pd.DataFrame({"ratio":[thisRatio],
                                            "rndint":[thisRndInt],
                                            "dataset":[thisDataset],
                                            "rmse": [thisRMSE],
                                            "r2": [thisR2],
                                            "prediction":[thisPrediction],
                                            "target":[707.0],
                                            "diff":[thisDiff]})
    except:
      print(f'Could not create thisCombinedDataEntry for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {datasetSubset}')
    else:
      #print(f'{thisCombinedDataEntry}')
      pass
      
    ## concat dfCombinedData with the new entry
    try:  
      dfCombinedData = pd.concat([dfCombinedData, thisCombinedDataEntry], ignore_index=True)
    except:
      print(f'Could not concat dfCombinedData with thisCombinedDataEntry for\nthisPredictionEntry = {thisPredictionEntry}')

  if os.path.exists(combinedDataFile):
    ## this if condition should only be checked if combinedDataFile does NOT exist. 
    ## If this is true it does exist, while it doesnt?
    print(f'It should not be possible that this code is executed.')
    os.remove(combinedDataFile)
    print(f'Removed existing combined data file: \'{combinedDataFile}\'.')
  dfCombinedData.to_csv(combinedDataFile)
  print(f'Wrote combined data to file: \'{combinedDataFile}\'.')
#print(f'{dfCombinedData}')

## min RMSE
idxMinRMSE = dfCombinedData['rmse'].idxmin()
#print(f'{idxMinRMSE}')
minRMSE = dfCombinedData['rmse'].min()
#print(f'{minRMSE}')
minRMSERow = dfCombinedData.iloc[idxMinRMSE]
#print(f'Min RMSE Entry:\n{minRMSERow}\n')

## max R2
idxMaxR2 = dfCombinedData['r2'].idxmax()
#print(f'{idxMaxR2}')
maxR2 = dfCombinedData['r2'].max()
#print(f'{maxR2}')
maxR2Row = dfCombinedData.iloc[idxMaxR2]
#print(f'Max R2 Entry:\n{maxR2Row}\n')

## diff closest to 0
thisDiff_old = 100000000
#print(f'{np.power(dfCombinedData.iloc[1]["diff"], 2)}')
for i in range(0, len(dfCombinedData)):
  thisDiff = min(thisDiff_old, np.power(dfCombinedData.iloc[i]["diff"], 2))
  if thisDiff < thisDiff_old:
    dfEntry = dfCombinedData.iloc[i]
    thisDiff_old = thisDiff
#print(f'Entry with diff closest to 0:\n{dfEntry}\n')

## filter based on following constraints
subsetGrid1296 = dfCombinedData[dfCombinedData["dataset"] == "Grid1296"]
subsetGrid2401 = dfCombinedData[dfCombinedData["dataset"] == "Grid2401"]
subsetSobol1 = dfCombinedData[dfCombinedData["dataset"] == "Sobol1"]
subsetSobol2 = dfCombinedData[dfCombinedData["dataset"] == "Sobol2"]

## plots
gs_kw = dict(width_ratios=[1, 1, 1], height_ratios=[1])
fig, axd = plt.subplot_mosaic([['RMSEvsR2', 'RMSEvsDiff', 'R2vsDiff']], 
                               gridspec_kw=gs_kw, figsize=(21.0, 7.0))

axd["RMSEvsR2"].scatter(subsetGrid1296["rmse"], subsetGrid1296["r2"], label="Dataset: Grid1296", c="#332288")
axd["RMSEvsR2"].scatter(subsetGrid2401["rmse"], subsetGrid2401["r2"], label="Dataset: Grid2401", c="#88CCEE")
axd["RMSEvsR2"].scatter(subsetSobol1["rmse"], subsetSobol1["r2"], label="Dataset: Sobol1", c="#DDCC77")
axd["RMSEvsR2"].scatter(subsetSobol2["rmse"], subsetSobol2["r2"], label="Dataset: Sobol2", c="#117733")
axd["RMSEvsR2"].set(xlabel="RMSE", ylabel="R2")
axd["RMSEvsR2"].set_title("RMSE vs R2", fontweight='bold')
axd["RMSEvsR2"].legend()

axd["RMSEvsDiff"].scatter(subsetGrid1296["rmse"], subsetGrid1296["diff"], label="Dataset: Grid1296", c="#332288")
axd["RMSEvsDiff"].scatter(subsetGrid2401["rmse"], subsetGrid2401["diff"], label="Dataset: Grid2401", c="#88CCEE")
axd["RMSEvsDiff"].scatter(subsetSobol1["rmse"], subsetSobol1["diff"], label="Dataset: Sobol1", c="#DDCC77")
axd["RMSEvsDiff"].scatter(subsetSobol2["rmse"], subsetSobol2["diff"], label="Dataset: Sobol2", c="#117733")
axd["RMSEvsDiff"].set(xlabel="RMSE", ylabel="Diff")
axd["RMSEvsDiff"].set_title("RMSE vs Diff (target - pred(opt_params))", fontweight='bold')
axd["RMSEvsDiff"].legend()

axd["R2vsDiff"].scatter(subsetGrid1296["r2"], subsetGrid1296["diff"], label="Dataset: Grid1296", c="#332288")
axd["R2vsDiff"].scatter(subsetGrid2401["r2"], subsetGrid2401["diff"], label="Dataset: Grid2401", c="#88CCEE")
axd["R2vsDiff"].scatter(subsetSobol1["r2"], subsetSobol1["diff"], label="Dataset: Sobol1", c="#DDCC77")
axd["R2vsDiff"].scatter(subsetSobol2["r2"], subsetSobol2["diff"], label="Dataset: Sobol2", c="#117733")
axd["R2vsDiff"].set(xlabel="R2", ylabel="Diff")
axd["R2vsDiff"].set_title("R2 vs Diff (target - pred(opt_params))", fontweight='bold')
axd["R2vsDiff"].legend()
plt.tight_layout()
plt.show()































