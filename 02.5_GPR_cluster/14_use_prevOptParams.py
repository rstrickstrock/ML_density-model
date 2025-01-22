### imports ###
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process.kernels import RationalQuadratic as RQ
from sklearn.gaussian_process.kernels import ExpSineSquared as ESS
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd

import pickle
import os
import glob


resultDir = f'diffKernels_trained_GPModels'
optParamFile = 'optimized_parameters.csv'

ratioDirs = glob.glob(os.path.join(resultDir, '*'))
cwd = os.getcwd()

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

dfResults = pd.DataFrame({"ratio":[],
                         "rndint":[],
                         "dataset":[],
                         "kernel":[],
                         "prediction":[],
                         "std dev.":[],
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
      thisRndInt = int(os.path.basename(modelFile).split("_")[3])
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
    
    try:
      thisKernel = str(os.path.basename(modelFile).split("_")[4].split(".")[0])
    except:
      print(f'Could not get thisKernel for modelfile:\n{modelFile}')
    else:
      #print(f'{thisKernel}')
      pass
    
    with open(modelFile, "rb") as thisFile:
      try:
        thisModel = pickle.load(thisFile)
      except:
        print(f'Could not load modelfile:\n{modelFile}')
    
    try:
      thisPrediction, thisStd = thisModel.predict(xOpt, return_std=True)
    except:
      print(f'Could not predict thisPrediction, thisStd with modelfile:\n{modelFile}')
    else:
      thisPrediction = float(thisPrediction)
      thisStd = float(thisStd)
      #print(f'thisPrediction: {thisPrediction}')
      #print(f'thisStd: {thisStd}')

    try:  
      thisDiff = yOpt - thisPrediction
    except:
      print(f'Could not calc thisDiff for modelfile:\n{modelFile}')
    
    try:
      newResultsEntry = pd.DataFrame({"ratio":[thisRatio],
                                      "rndint":[thisRndInt],
                                      "dataset":[thisDataset],
                                      "kernel":[thisKernel],
                                      "prediction":[thisPrediction],
                                      "std dev.":[thisStd],
                                      "target":[yOpt],
                                      "diff":[thisDiff]})
    except:
      print(f'something went wrong with creating the newResultsEntry for modelfile:\n{modelFile}')
    else:
      try:
        dfResults = pd.concat([dfResults, newResultsEntry], ignore_index=True)
      except:
        print(f'something went wrong when concating DFs for modefile:\n{modelFile}')
      else:
        pass

    #print(f'{dfResults}')
  
  os.chdir(cwd)
  #print(f'{dfResults}')

statisticsFileName = 'yPredictionsOfGPModelsDiffKernels.csv'
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfResults.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfResults}')
