import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt

statisticsFile = 'StatisticsOfGPTraining.csv'
if not os.path.isfile(statisticsFile):
  print(f'Can not find and open \'{statisticsFile}\'. Exit.')
  exit()
else:
  dfStatistics = pd.read_csv(statisticsFile)
  try:
    dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])
  except:
    print(f'Something went wrong with\'dfStatistics = dfStatistics.drop(columns=["Unnamed: 0"])\'.')
  else:
    #print(f'{dfStatistics}')
    pass


def calc_stats(dataFrame):
  time = dataFrame["time [hrs]"].to_numpy()
  #print(f'{time}')
  avgTime = np.mean(time)
  #print(f'{avgTime}')
  sdTime = np.std(time)
  #print(f'{sdTime}')
  
  rmse = dataFrame["rmse"].to_numpy()
  #print(f'{rmse}')
  avgRMSE = np.mean(rmse)
  #print(f'{avgRMSE}')
  sdRMSE = np.std(rmse)
  #print(f'{sdRMSE}')
  
  r2 = dataFrame["r2"].to_numpy()
  #print(f'{r2}')
  avgR2 = np.mean(r2)
  #print(f'{avgR2}')
  sdR2 = np.std(r2)
  #print(f'{sdR2}')
  
  return avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2


def plot_incl_stats(df, dfAvg, xAxis, yAxis, avgXAxis, avgYAxis, sdYAxis):
  try:
    xAxis = str(xAxis)
  except:
    print(f'ERROR: xAxis must be a string. Exit.')
    exit()
  try:
    yAxis = str(yAxis)
  except:
    print(f'ERROR: yAxis mus be a string. Exit.')
    exit()
  try:
    avgXAxis = str(avgXAxis)
  except:
    print(f'ERROR: avgXAxis must be a string. Exit.')
    exit()
  try:
    avgYAxis = str(avgYAxis)
  except:
    print(f'ERROR: avgYAxis mus be a string. Exit.')
    exit()
  try:
    sdYAxis = str(sdYAxis)
  except:
    print(f'ERROR: sdYAxis mus be a string. Exit.')
    exit()
      

  gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1, 2])
  fig, axd = plt.subplot_mosaic([['Grid1296', 'Sobol1'],
                                 ['Grid2401', 'Sobol2'],
                                 ['Averages', 'Averages']],
                                gridspec_kw=gs_kw, figsize=(10.0, 7.0), layout="constrained")
  ## plot all data
  legendGrid1296 = True
  legendGrid2401 = True
  legendSobol1 = True
  legendSobol2 = True
  for i in range(0, len(df)):
    thisLabel = None
    thisRow = df.iloc[i]
    #print(f'{thisRow[xAxis]}')
    if thisRow["dataset"] == "Grid1296":
      thisMarker = 'o'
      thisColor = '#377eb7' #blue
      thisDataSet = "Grid1296"
      if legendGrid1296:
        thisLabel = "Grid1296"
        legendGrid1296 = False
        #thisTitle = "Trainingdataset: Grid1296"
    elif thisRow["dataset"] == "Grid2401":
      thisMarker = 's'
      thisColor = '#ff7f00' #orange
      thisDataSet = "Grid2401"
      if legendGrid2401:
        thisLabel = "Grid2401"
        legendGrid2401 = False
        #thisTitle = "Trainingdataset: Grid2401"
    elif thisRow["dataset"] == "Sobol1":
      thisMarker = 'd'
      thisColor = '#4daf4a' #green
      thisDataSet = "Sobol1"
      if legendSobol1:
        thisLabel = "Sobol1"
        legendSobol1 = False
        #thisTitle = "Trainingdataset: Sobol1"
    elif thisRow["dataset"] == "Sobol2":
      thisMarker = 'X'
      thisColor = '#f781bf' #pink
      thisDataSet = "Sobol2"
      if legendSobol2:
        thisLabel = "Sobol2"
        legendSobol2 = False
        #thisTitle = "Trainingdataset: Sobol2"
    
    if thisLabel is not None:
      axd[thisDataSet].plot(thisRow[xAxis], thisRow[yAxis], color=thisColor, marker=thisMarker, label=thisLabel)
      #axd[thisDataSet].set_title(thisTitle)
    else:
      axd[thisDataSet].plot(thisRow[xAxis], thisRow[yAxis], color=thisColor, marker=thisMarker)
    #break
    
  ## plot averages + std dev
  legendGrid1296 = True
  legendGrid2401 = True
  legendSobol1 = True
  legendSobol2 = True
  for i in range(0, len(dfAvg)):
    thisLabel = None
    thisRow = dfAvg.iloc[i]
    if thisRow["dataset"] == "Grid1296":
      thisMarker = 'o'
      thisColor = '#984ea3' #purple
      thisMultPlotColor = '#377eb7' #blue
      thisDataSet = "Grid1296"
      if legendGrid1296:
        thisLabel = "Avg. + Std.Dev."
        thisMultPlotLabel = "Grid1296"
        legendGrid1296 = False
    elif thisRow["dataset"] == "Grid2401":
      thisMarker = 's'
      thisColor = '#984ea3' #purple
      thisMultPlotColor = '#ff7f00' #orange
      thisDataSet = "Grid2401" 
      if legendGrid2401:
        thisLabel = "Avg. + Std.Dev."
        thisMultPlotLabel = "Grid2401"
        legendGrid2401 = False
    elif thisRow["dataset"] == "Sobol1":
      thisMarker = 'd'
      thisColor = '#984ea3' #purple
      thisMultPlotColor = '#4daf4a' #green
      thisDataSet = "Sobol1" 
      if legendSobol1:
        thisLabel = "Avg. + Std.Dev."
        thisMultPlotLabel = "Sobol1"
        legendSobol1 = False 
    elif thisRow["dataset"] == "Sobol2":
      thisMarker = 'X'
      thisColor = '#984ea3' #purple
      thisMultPlotColor = '#f781bf' #pink
      thisDataSet = "Sobol2"
      if legendSobol2:
        thisLabel = "Avg. + Std.Dev."
        thisMultPlotLabel = "Sobol2"
        legendSobol2 = False
      
    if thisLabel is not None:
      axd[thisDataSet].errorbar(thisRow[avgXAxis], thisRow[avgYAxis], yerr=thisRow[sdYAxis], color=thisColor, marker=thisMarker, label=thisLabel)
      axd["Averages"].errorbar(thisRow[avgXAxis], thisRow[avgYAxis], yerr=thisRow[sdYAxis], color=thisMultPlotColor, marker=thisMarker, label=thisMultPlotLabel)
    else:
      axd[thisDataSet].errorbar(thisRow[avgXAxis], thisRow[avgYAxis], yerr=thisRow[sdYAxis], color=thisColor, marker=thisMarker)
      axd["Averages"].errorbar(thisRow[avgXAxis], thisRow[avgYAxis], yerr=thisRow[sdYAxis], color=thisMultPlotColor, marker=thisMarker)
  
  axd["Averages"].set_title("Compare Averages")
  for mosaicName in ["Grid1296", "Grid2401", "Sobol1", "Sobol2", "Averages"]:
    axd[mosaicName].legend()
    axd[mosaicName].set(xlabel=xAxis, ylabel=yAxis)
  #  ax.set(xlabel=xAxis, ylabel=yAxis)  
  #for ax in axd.flat:
    #ax.label_outer()  
  #  ax.legend()
  plt.show()



### MIN RMSE    
idxMinRMSE = dfStatistics['rmse'].idxmin()
#print(f'{idxMinRMSE}')
minRMSE = dfStatistics['rmse'].min()
#print(f'{minRMSE}')
minRMSERow = dfStatistics.iloc[idxMinRMSE]
#print(f'Min RMSE Entry:\n{minRMSERow}\n')

### MAX R2
idxMaxR2 = dfStatistics['r2'].idxmax()
#print(f'{idxMaxR2}')
maxR2 = dfStatistics['r2'].max()
#print(f'{maxR2}')
maxR2Row = dfStatistics.iloc[idxMaxR2]
#print(f'Max R2 Entry:\n{maxR2Row}\n')

### loop over ratios
ratios = dfStatistics['ratio'].to_numpy()
listOfRatios = []
for ratio in ratios:
  #print(f'{ratio}')
  if ratio not in listOfRatios:
    listOfRatios.append(ratio)
#print(f'{listOfRatios}')

dfAverages = pd.DataFrame({"ratio": [],
                           "dataset": [],
                           "avg. time [hrs]": [],
                           "sd. time [hrs]": [],
                           "avg. rmse": [],
                           "sd. rmse": [],
                           "avg. r2": [],
                           "sd. r2": []})
#print(f'{dfAverages}')
for ratio in listOfRatios:
  ## get all data for this ratio
  dfRatio = dfStatistics[dfStatistics["ratio"] == ratio]
  #print(f'{dfRatio}')
  
  ## sort data by datasets
  dfGrid1296 = dfRatio[dfRatio["dataset"] == "Grid1296"]
  #print(f'{dfGrid1296}')
  dfGrid2401 = dfRatio[dfRatio["dataset"] == "Grid2401"]
  #print(f'{dfGrid2401}')
  dfSobol1 = dfRatio[dfRatio["dataset"] == "Sobol1"]
  #print(f'{dfSobol1}')
  dfSobol2 = dfRatio[dfRatio["dataset"] == "Sobol2"]
  #print(f'{dfSobol2}')
  
  ## calculate means for every dataset
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid1296)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid1296"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid2401)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid2401"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol1)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol1"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol2)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol2"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #print(f'{dfAverages}')
  #break
#print(f'{dfAverages}')
  
### MIN AVG RMSE    
idxMinAvgRMSE = dfAverages['avg. rmse'].idxmin()
#print(f'{idxMinAvgRMSE}')
minAvgRMSE = dfAverages['avg. rmse'].min()
#print(f'{minAvgRMSE}')
minAvgRMSERow = dfAverages.iloc[idxMinAvgRMSE]
#print(f'Min avg. RMSE Entry:\n{minAvgRMSERow}\n')

### MAX R2
idxMaxAvgR2 = dfAverages['avg. r2'].idxmax()
#print(f'{idxMaxAvgR2}')
maxAvgR2 = dfAverages['avg. r2'].max()
#print(f'{maxAvgR2}')
maxAvgR2Row = dfAverages.iloc[idxMaxAvgR2]
#print(f'Max R2 Entry:\n{maxAvgR2Row}\n')  


## plot ratio vs time
plot_incl_stats(dfStatistics, dfAverages, "ratio", "time [hrs]", "ratio", "avg. time [hrs]", "sd. time [hrs]")
  
## plot ratio vs rmse
#plot_incl_stats(dfStatistics, dfAverages, "ratio", "rmse", "ratio", "avg. rmse", "sd. rmse")  
  
## plot ratio vs r2

#plot_incl_stats(dfStatistics, dfAverages, "ratio", "r2", "ratio", "avg. r2", "sd. r2")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
