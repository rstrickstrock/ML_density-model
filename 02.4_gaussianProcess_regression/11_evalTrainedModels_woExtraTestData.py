### imports ###
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process.kernels import RationalQuadratic as RQ
from sklearn.gaussian_process.kernels import ExpSineSquared as ESS

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
import numpy as np
import os
import glob

import pickle

## grid sampling 1296
data1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
data1296 = data1296.drop(data1296.columns[0], axis=1)
X_1296 = data1296.drop('density', axis=1)
Y_1296 = data1296['density']

## grid sampling 2401
data2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
data2401 = data2401.drop(data2401.columns[0], axis=1)
X_2401 = data2401.drop('density', axis=1)
Y_2401 = data2401['density']

## sobol2 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']

## sobol2 sampling
data_sobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
data_sobol2 = data_sobol2.drop(data_sobol2.columns[0], axis=1)
X_sobol2 = data_sobol2.drop('density', axis=1)
Y_sobol2 = data_sobol2['density']

statisticsFileName = 'Stats_woExtraTestData.csv'

pwd = os.getcwd()
### create current working directory ###
cwd = os.path.join(pwd, "trainedModels")
#print(f'{cwd}')
os.chdir(cwd)

absRatios = glob.glob(os.path.join(os.getcwd(), "*"))

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "kernel": [],
                             "rmse": [],
                             "mape": [],
                             "r2": []})

for ratio in absRatios:
  #Ratios.append(os.path.basename(ratio))
  modelFiles = glob.glob(os.path.join(os.getcwd(), ratio, "*"))
  #print(f'{Models}')
  for modelfile in modelFiles:
    #print(f'{modelfile}')
    thisDatasetName = os.path.basename(modelfile).split("_")[1][5:]
    #print(f'{thisDatasetName}')
    thisRatio = float(os.path.basename(modelfile).split("_")[2])
    #print(f'{thisRatio}')
    thisRndInt = int(os.path.basename(modelfile).split("_")[3])
    #print(f'{thisRndInt}')
    thisKernel = os.path.basename(modelfile).split("_")[4].split(".")[0]
    #print(f'{thisKernel}')
    
    if thisDatasetName == "Grid1296":
      X_train, X_test, Y_train, Y_test = train_test_split(X_1296, Y_1296, test_size=thisRatio, random_state=thisRndInt)
    elif thisDatasetName == "Grid2401":
      X_train, X_test, Y_train, Y_test = train_test_split(X_2401, Y_2401, test_size=thisRatio, random_state=thisRndInt)
    elif thisDatasetName == "Sobol1":
      X_train, X_test, Y_train, Y_test = train_test_split(X_sobol1, Y_sobol1, test_size=thisRatio, random_state=thisRndInt)
    elif thisDatasetName == "Sobol2":
      X_train, X_test, Y_train, Y_test = train_test_split(X_sobol2, Y_sobol2, test_size=thisRatio, random_state=thisRndInt)
    
    thisFile = open(modelfile, 'rb')
    thisModel = pickle.load(thisFile)
    
    prediction = thisModel.predict(X_test)
    rmse = np.sqrt(mean_squared_error(Y_test, prediction))
    mape = skmape(Y_test, prediction)
    r2 = r2_score(Y_test, prediction)
    
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [thisRndInt],
                            "dataset": [thisDatasetName],
                            "kernel": [thisKernel],
                            "rmse": [rmse],
                            "mape": [mape],
                            "r2": [r2]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    #break
  #break
os.chdir(pwd)
#print(f'{os.getcwd()}')
#print(f'{dfStatistics}')
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStatistics}')
























