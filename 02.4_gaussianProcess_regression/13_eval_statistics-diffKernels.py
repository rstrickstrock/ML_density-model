import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt

statisticsFile = 'StatisticsOfGPTrainingDiffKernels.csv'
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


def plot_incl_stats(df, dfAvg, xAxis, yAxis, avgYAxis, sdYAxis, setYLim=False):
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
    avgYAxis = str(avgYAxis)
  except:
    print(f'ERROR: avgYAxis must be a string. Exit.')
    exit()
  try:
    sdYAxis = str(sdYAxis)
  except:
    print(f'ERROR: sdYAxis must be a string. Exit.')
    exit()

  # Define a color map for the kernel-category
  color_map = {"RBF": "#377eb8",    #blue
               "Matern": "#a65628", #brown
               "RQ": "#4daf4a",     #green
               "ESS": "#984ea3"}    #purple
  # Define offsets for subcategories
  offset_map = {"RBF": -0.3, "Matern": -0.1, "RQ": 0.1, "ESS":0.3} 
  
#  fig, ax = plt.subplots()
  gs_kw = dict(width_ratios=[1, 1], height_ratios=[1, 1, 2])
  fig, axd = plt.subplot_mosaic([['Grid1296', 'Sobol1'],
                                 ['Grid2401', 'Sobol2'],
                                 ['Averages', 'Averages']],
                                gridspec_kw=gs_kw, figsize=(22.0, 12.0))#, layout="constrained")
  # get x-Axis categories
  x_categories = df[xAxis].unique()
  x_positions_base = {cat: i for i, cat in enumerate(x_categories)}

  # plot points
  yMin = min(0, df[yAxis].min())
  yMax = int(df[yAxis].max()*100)/100

  for thisDataSet in df["dataset"].unique():
    #print(f'thisDataSet: {thisDataSet}')
    subset = df[df["dataset"] == thisDataSet]
    for thisKernel in subset["kernel"].unique():
      #print(f'\tKernel: {thisKernel}')
      kernelSubset = subset[subset["kernel"] == thisKernel]
      x_positions = [x_positions_base[t] + offset_map[thisKernel] for t in kernelSubset[xAxis]]
      axd[thisDataSet].scatter(x_positions, kernelSubset[yAxis], label=thisKernel, color=color_map[thisKernel])
      #axd[thisDataSet].legend()
      #axd[thisDataSet].set(xlabel=xAxis, ylabel=yAxis)
      #axd[thisDataSet].set_xticks(range(len(x_categories)))
      #axd[thisDataSet].set_xticklabels(x_categories, fontsize=10)
      #break
      
  # plot averages
  thisColor = "#f781bf" # pink for averages
  thisMarker = 'X' 
  for thisDataSet in dfAvg["dataset"].unique():
    thisLabel = True
    #print(f'thisDataSet: {thisDataSet}')
    subset = dfAvg[dfAvg["dataset"] == thisDataSet]
    for thisKernel in subset["kernel"].unique():
      #print(f'\tKernel: {thisKernel}')
      kernelSubset = subset[subset["kernel"] == thisKernel]
      x_positions = [x_positions_base[t] + offset_map[thisKernel] for t in kernelSubset[xAxis]]
      if thisLabel is True:
        thisLabel = "Averages"
      axd[thisDataSet].errorbar(x_positions, kernelSubset[avgYAxis], yerr=kernelSubset[sdYAxis], color=thisColor, marker=thisMarker, ls='', label=thisLabel)
      thisLabel = None
      if thisDataSet == "Grid1296":
        thisMultplotMarker = 'v'
        thisMultPlotLabel = f'Grid1296 + {thisKernel}'
      elif thisDataSet == "Grid2401":
        thisMultplotMarker = '^'
        thisMultPlotLabel = f'Grid2401 + {thisKernel}'
      elif thisDataSet == "Sobol1":
        thisMultplotMarker = 's'
        thisMultPlotLabel = f'Sobol1 + {thisKernel}'
      elif thisDataSet == "Sobol2":
        thisMultplotMarker = 'D'
        thisMultPlotLabel = f'Sobol1 + {thisKernel}'
      axd["Averages"].errorbar(x_positions, kernelSubset[avgYAxis], yerr=kernelSubset[sdYAxis], color=color_map[thisKernel], marker=thisMultplotMarker, label=thisMultPlotLabel)
      #break
      
  for thisDataSet in np.append(df["dataset"].unique(), 'Averages'):
    axd[thisDataSet].legend()
    axd[thisDataSet].set(xlabel=xAxis, ylabel=yAxis)
    axd[thisDataSet].set_xticks(range(len(x_categories)))
    axd[thisDataSet].set_xticklabels(x_categories, fontsize=10)
    if setYLim == True:
      axd[thisDataSet].set_ylim([yMin, yMax*1.1])
      axd[thisDataSet].set_yticks(np.linspace(yMin, yMax, 5))
    axd[thisDataSet].set_title(f'Trainingdataset: {thisDataSet}', fontweight='bold')
    if thisDataSet == "Averages":
      axd[thisDataSet].set_title(thisDataSet, fontweight='bold')

  # Adjust layout and show plot
  plt.tight_layout()
  plt.show()


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
                           "kernel": [],
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
  dfGrid1296RBF = dfGrid1296[dfGrid1296["kernel"] == "RBF"]
  dfGrid1296Matern = dfGrid1296[dfGrid1296["kernel"] == "Matern"]
  dfGrid1296RQ = dfGrid1296[dfGrid1296["kernel"] == "RQ"]
  dfGrid1296ESS = dfGrid1296[dfGrid1296["kernel"] == "ESS"]
  #print(f'{dfGrid1296RBF}')
  
  dfGrid2401 = dfRatio[dfRatio["dataset"] == "Grid2401"]
  #print(f'{dfGrid2401}')
  dfGrid2401RBF = dfGrid2401[dfGrid2401["kernel"] == "RBF"]
  dfGrid2401Matern = dfGrid2401[dfGrid2401["kernel"] == "Matern"]
  dfGrid2401RQ = dfGrid2401[dfGrid2401["kernel"] == "RQ"]
  dfGrid2401ESS = dfGrid2401[dfGrid2401["kernel"] == "ESS"]
  #print(f'{dfGrid2401RBF}')
  
  dfSobol1 = dfRatio[dfRatio["dataset"] == "Sobol1"]
  #print(f'{dfSobol1}')
  dfSobol1RBF = dfSobol1[dfSobol1["kernel"] == "RBF"]
  dfSobol1Matern = dfSobol1[dfSobol1["kernel"] == "Matern"]
  dfSobol1RQ = dfSobol1[dfSobol1["kernel"] == "RQ"]
  dfSobol1ESS = dfSobol1[dfSobol1["kernel"] == "ESS"]
  #print(f'{dfSobol1RBF}')
  
  dfSobol2 = dfRatio[dfRatio["dataset"] == "Sobol2"]
  #print(f'{dfSobol2}')
  dfSobol2RBF = dfSobol2[dfSobol2["kernel"] == "RBF"]
  dfSobol2Matern = dfSobol2[dfSobol2["kernel"] == "Matern"]
  dfSobol2RQ = dfSobol2[dfSobol2["kernel"] == "RQ"]
  dfSobol2ESS = dfSobol2[dfSobol2["kernel"] == "ESS"]
  #print(f'{dfSobol2RBF}')
  
  ## calculate means for every dataset
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid1296RBF)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid1296"], "kernel": ["RBF"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid1296Matern)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid1296"], "kernel": ["Matern"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid1296RQ)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid1296"], "kernel": ["RQ"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid1296ESS)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid1296"], "kernel": ["ESS"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid2401RBF)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid2401"], "kernel": ["RBF"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid2401Matern)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid2401"], "kernel": ["Matern"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid2401RQ)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid2401"], "kernel": ["RQ"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfGrid2401ESS)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Grid2401"], "kernel": ["ESS"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol1RBF)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol1"], "kernel": ["RBF"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol1Matern)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol1"], "kernel": ["Matern"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol1RQ)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol1"], "kernel": ["RQ"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol1ESS)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol1"], "kernel": ["ESS"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol2RBF)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol2"], "kernel": ["RBF"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol2Matern)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol2"], "kernel": ["Matern"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol2RQ)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol2"], "kernel": ["RQ"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  avgTime, sdTime, avgRMSE, sdRMSE, avgR2, sdR2 = calc_stats(dfSobol2ESS)
  newDfEntry = pd.DataFrame({"ratio": [ratio], "dataset": ["Sobol2"], "kernel": ["ESS"], "avg. time [hrs]": [avgTime], "sd. time [hrs]": [sdTime], "avg. rmse": [avgRMSE], "sd. rmse": [sdRMSE], "avg. r2": [avgR2], "sd. r2": [sdR2]})
  dfAverages = pd.concat([dfAverages, newDfEntry], ignore_index=True)
  #print(f'{dfAverages}')
  #break
#print(f'{dfAverages}')


### MIN RMSE    
idxMinRMSE = dfStatistics['rmse'].idxmin()
#print(f'{idxMinRMSE}')
minRMSE = dfStatistics['rmse'].min()
#print(f'{minRMSE}')
minRMSERow = dfStatistics.iloc[idxMinRMSE]
print(f'Min RMSE Entry:\n{minRMSERow}\n')

### MAX R2
idxMaxR2 = dfStatistics['r2'].idxmax()
#print(f'{idxMaxR2}')
maxR2 = dfStatistics['r2'].max()
#print(f'{maxR2}')
maxR2Row = dfStatistics.iloc[idxMaxR2]
print(f'Max R2 Entry:\n{maxR2Row}\n')

 
### MIN AVG RMSE    
idxMinAvgRMSE = dfAverages['avg. rmse'].idxmin()
#print(f'{idxMinAvgRMSE}')
minAvgRMSE = dfAverages['avg. rmse'].min()
#print(f'{minAvgRMSE}')
minAvgRMSERow = dfAverages.iloc[idxMinAvgRMSE]
print(f'Min avg. RMSE Entry:\n{minAvgRMSERow}\n')

### MAX R2
idxMaxAvgR2 = dfAverages['avg. r2'].idxmax()
#print(f'{idxMaxAvgR2}')
maxAvgR2 = dfAverages['avg. r2'].max()
#print(f'{maxAvgR2}')
maxAvgR2Row = dfAverages.iloc[idxMaxAvgR2]
print(f'Max R2 Entry:\n{maxAvgR2Row}\n')  


## plot ratio vs time
#plot_incl_stats(dfStatistics, dfAverages, "ratio", "time [hrs]", "avg. time [hrs]", "sd. time [hrs]", setYLim=True)
  
## plot ratio vs rmse
#plot_incl_stats(dfStatistics, dfAverages, "ratio", "rmse", "avg. rmse", "sd. rmse")  
  
## plot ratio vs r2
plot_incl_stats(dfStatistics, dfAverages, "ratio", "r2", "avg. r2", "sd. r2")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
