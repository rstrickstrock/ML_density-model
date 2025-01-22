import pandas as pd
import pickle
import os
import glob

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.metrics import mean_squared_error, r2_score

resultDir = "trained_GPModels"
optimizedParametersFile = "optimized_parameters.csv"

ratioDirs = glob.glob(os.path.join(resultDir, '*'))
#print(f'{ratioDirs}')

dfOptParams = pd.read_csv(optimizedParametersFile)
#print(f'{dfOptParams}')
xOpt = dfOptParams.drop('density', axis=1)
yOpt = dfOptParams['density']
#print(f'{xOpt}')
#print(f'{yOpt}')

for ratioDir in ratioDirs:
  trainedModels = glob.glob(os.path.join(ratioDir,'trained_model*'))
  #print(f'{trainedModels}')
  for trainedModel in trainedModels:
    print(f'trainedModel') ### CONTINUE HERE, GET MODEL STATS AND SAFE IT IN DF
    model = pickle.load(open(trainedModel, 'rb'))
    #print(f'{model}')
    yPredMean, yPredStd = model.predict(xOpt, return_std=True)
    print(f'{yPredMean}, {yPredStd}')
    diff = yPredMean - yOpt
    break
  break
