import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


combinedDataFile = 'DiffRMSER2.csv'
statisticsFile = 'StatisticsOfGPTrainingDiffKernels.csv'
predictionsFile = 'yPredictionsOfGPModelsDiffKernels_usingPrevOptParams.csv'

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
else:
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
    
  if not os.path.isfile(predictionsFile):
    print(f'Can not find and open \'{predictionsFile}\'. Exit.')
    exit()
  else:
    dfPredictions = pd.read_csv(predictionsFile)
    #print(f'{dfPredictions}')
    try:
      dfPredictions = dfPredictions.drop(columns=["Unnamed: 0"])
    except:
      print(f'Something went wrong with\'dfPredictions = dfPredictions.drop(columns=["Unnamed: 0"])\'.')
    else:
      #print(f'{dfPredictions}')
      pass
    

## plot diff vs RMSE && diff vs R2
if createCombinedDataFile:
  dfCombinedData = pd.DataFrame({"diff": [],
                                 "rmse": [],
                                 "r2": []})
  
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
    try:
      thisKernel = thisPredictionEntry["kernel"]
    except:
      print(f'Could not get \'thisKernel = thisPredictionEntry["kernel"]\' for\nthisPredictionEntry = {thisPredictionEntry}')
  
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
    try:
      kernelSubset = datasetSubset[datasetSubset["kernel"] == thisKernel]
    except:
      print(f'Could not get \'kernelSubset = datasetSubset[datasetSubset["kernel"] == thisKernel]\' for\nthisPredictionEntry = {thisPredictionEntry}')
    else:
      #print(f'{kernelSubset}')
      pass
    
    ## get RMSE and R2 from dfStatistics entry  
    try:
      thisRMSE = kernelSubset["rmse"]
    except:
      print(f'Could not get \'thisRMSE = kernelSubset["rmse"]\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {kernelSubset}')
    else:
      #print(f'{thisRMSE}')
      #print(f'{thisRMSE.to_numpy()}')
      #print(f'{float(thisRMSE.to_numpy())}')
      try:
        thisRMSE = float(thisRMSE.to_numpy())
      except:
        print(f'Could not cast \'thisRMSE = float(thisRMSE.to_numpy())\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {kernelSubset}')
      else:
        #print(f'{thisRMSE}')
        pass
      pass
    try:
      thisR2 = kernelSubset["r2"]
    except:
      print(f'Could not get \'thisR2 = kernelSubset["r2"]\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {kernelSubset}')
    else:
      #print(f'{thisR2}')
      try:
        thisR2 = float(thisR2.to_numpy())
      except:
        print(f'Could not cast \'thisRMSE = float(thisR2.to_numpy())\' for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {kernelSubset}')
      else:
        #print(f'{thisR2}')
        pass
      pass
  
    ## create ne df entry for dfCombinedData
    try:
      thisCombinedDataEntry = pd.DataFrame({"diff": [thisDiff], "rmse": [thisRMSE], "r2": [thisR2]})
    except:
      print(f'Could not create thisCombinedDataEntry for\nthisPredictionEntry = {thisPredictionEntry}\nthisStatisticsEntry = {kernelSubset}')
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

## linear regression for subset (based on previous plotting)
diffMax = 10
diffMin = -10
subsetDiff = dfCombinedData[dfCombinedData["diff"] <= diffMax]
#print(f'{len(subsetDiff)}')
subsetDiff = subsetDiff[subsetDiff["diff"] >= diffMin]
#print(f'{subsetDiff}')

rmseMax = 25
rmseMin = 0
subsetRMSE = dfCombinedData[dfCombinedData["rmse"] <= rmseMax]
#print(f'{len(subsetRMSE)}')
subsetRMSE = subsetRMSE[subsetRMSE["rmse"] >= rmseMin]
#print(f'{subsetRMSE}')

r2Max = 1.0
r2Min = 0.94
subsetR2 = dfCombinedData[dfCombinedData["r2"] <= r2Max]
#print(f'{len(subsetR2)}')
subsetR2 = subsetR2[subsetR2["r2"] >= r2Min]
#print(f'{subsetR2}')

subsetRMSER2 = subsetRMSE[subsetRMSE["r2"] <= r2Max]
subsetRMSER2 = subsetRMSER2[subsetRMSER2["r2"] >= r2Min]
#print(f'{subsetRMSER2}')


## plots
gs_kw = dict(width_ratios=[1, 1, 1, 3], height_ratios=[1, 1, 1])
fig, axd = plt.subplot_mosaic([['RMSEvsDiff', 'R2vsDiff', 'RMSEvsR2', 'RMSER2Filtered'], 
                               ['ZoomRMSEvsDiff', 'ZoomR2vsDiff', 'ZoomRMSEvsR2', 'RMSER2Filtered'], 
                               ['DiffFiltered', 'RMSEFiltered', 'R2Filtered', 'RMSER2Filtered']], 
                               gridspec_kw=gs_kw, figsize=(28.0, 14.0))
                               
axd["RMSEvsDiff"].scatter(dfCombinedData["rmse"], dfCombinedData["diff"], label="RMSE vs Diff", c="#377eb8")
axd["RMSEvsDiff"].set(xlabel="RMSE", ylabel="Diff")
axd["RMSEvsDiff"].set_title("RMSE vs Diff", fontweight='bold')
axd["RMSEvsDiff"].plot([0, 0], [diffMin, diffMax], ls='-', color='red', label='Zoom Range')
axd["RMSEvsDiff"].legend()
axd["ZoomRMSEvsDiff"].scatter(subsetDiff["rmse"], subsetDiff["diff"], label="RMSE vs Diff", c="#377eb8")
axd["ZoomRMSEvsDiff"].legend()
axd["ZoomRMSEvsDiff"].set(xlabel="RMSE", ylabel="Diff")
axd["ZoomRMSEvsDiff"].set_title("Zoomed RMSE vs Diff", fontweight='bold')
axd["DiffFiltered"].scatter(subsetDiff["rmse"], subsetDiff["r2"], label=f'{diffMin} <= diff <= {diffMax}', c="#377eb8")
axd["DiffFiltered"].legend()
axd["DiffFiltered"].set(xlabel="RMSE", ylabel="R2")
axd["DiffFiltered"].set_title(f'RMSE vs R2 filtered by {diffMin}<=diff<={diffMax}', fontweight='bold')

axd["R2vsDiff"].scatter(dfCombinedData["r2"], dfCombinedData["diff"], label="R2 vs Diff", c="#4daf4a")
axd["R2vsDiff"].set(xlabel="R2", ylabel="Diff")
axd["R2vsDiff"].set_title("R2 vs Diff", fontweight='bold')
axd["R2vsDiff"].plot([0, 0], [diffMin, diffMax], ls='-', color='red', label='Zoom Range')
axd["R2vsDiff"].legend()
axd["ZoomR2vsDiff"].scatter(subsetDiff["r2"], subsetDiff["diff"], label="R2 vs Diff", c="#4daf4a")
axd["ZoomR2vsDiff"].legend()
axd["ZoomR2vsDiff"].set(xlabel="R2", ylabel="Diff")
axd["ZoomR2vsDiff"].set_title("Zoomed R2 vs Diff", fontweight='bold')
axd["ZoomR2vsDiff"].set_xlim([0, 1.0])
#axd["ZoomR2vsDiff"].set_ylim([diffMin, diffMax])
axd["RMSEFiltered"].scatter(subsetRMSE["r2"], subsetRMSE["diff"], label=f'{rmseMin} <= rmse <= {rmseMax}', c="#4daf4a")
axd["RMSEFiltered"].legend()
axd["RMSEFiltered"].set(xlabel="R2", ylabel="Diff")
axd["RMSEFiltered"].set_title(f'R2 vs Diff filtered by rmse<={rmseMax}', fontweight='bold')

axd["RMSEvsR2"].scatter(dfCombinedData["rmse"], dfCombinedData["r2"], label="RMSE vs R2", c="#852E02")
axd["RMSEvsR2"].set(xlabel="RMSE", ylabel="R2")
axd["RMSEvsR2"].set_title("RMSE vs R2", fontweight='bold')
thisXMin = 15
thisXMax = 50
thisYMin = 0.7
thisYMax = 1.0
axd["RMSEvsR2"].plot([rmseMin, rmseMax], [0, 0], ls='-', color='red', label='Zoom Range')
axd["RMSEvsR2"].legend()
axd["ZoomRMSEvsR2"].scatter(subsetRMSE["rmse"], subsetRMSE["r2"], label="RMSE vs R2", c="#852E02")
axd["ZoomRMSEvsR2"].legend()
axd["ZoomRMSEvsR2"].set(xlabel="RMSE", ylabel="R2")
axd["ZoomRMSEvsR2"].set_title("Zoomed RMSE vs R2", fontweight='bold')
axd["R2Filtered"].scatter(subsetR2["rmse"], subsetR2["diff"], label=f'{r2Min} <= r2 <= {r2Max}', c="#852E02")
axd["R2Filtered"].legend()
axd["R2Filtered"].set(xlabel="RMSE", ylabel="Diff")
axd["R2Filtered"].set_title(f'RMSE vs Diff filtered by {r2Min}<=r2<={r2Max}', fontweight='bold')

X = subsetRMSER2["rmse"]
Y = subsetRMSER2["r2"]
Z = subsetRMSER2["diff"]
cm = plt.cm.get_cmap('Accent')
#scatter = axd["RMSER2Filtered"].scatter(X, Y, c=Z.to_numpy(), cmap=cm, vmin=-max(np.sqrt(np.power(Z.min(),2)), np.sqrt(np.power(Z.max(), 2))), vmax=max(np.sqrt(np.power(Z.min(),2)), np.sqrt(np.power(Z.max(), 2))))
scatter = axd["RMSER2Filtered"].scatter(X, Y, c=Z.to_numpy(), cmap=cm, vmin=2*diffMin, vmax=diffMax)
axd["RMSER2Filtered"].set(xlabel="RMSE", ylabel="R2")
axd["RMSER2Filtered"].set_title(f'RMSE vs R2 filtered by {r2Min}<=r2<={r2Max} AND rmse<={rmseMax}, colorcoded by Diff ', fontweight='bold')
cbar = fig.colorbar(scatter, ax=axd["RMSER2Filtered"], orientation='vertical')
cbar.set_label("Diff")

plt.tight_layout()
plt.show()































