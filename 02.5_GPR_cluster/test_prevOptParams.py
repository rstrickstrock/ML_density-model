### imports ###
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process.kernels import RationalQuadratic as RQ
from sklearn.gaussian_process.kernels import ExpSineSquared as ESS
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import time
import pickle

minRMSEFile = 'diffKernels_trained_GPModels/0.2/trained_modelSobol2_0.2_816_Matern.sav'
maxR2File = 'diffKernels_trained_GPModels/0.5/trained_modelSobol1_0.5_721_RQ.sav'
optParamFile = 'optimized_parameters.csv'

optParams = pd.read_csv(optParamFile)
#print(f'{optParams}')
xOpt = optParams.drop('density', axis=1)
#print(f'{xOpt}')
yOpt = optParams['density']
#print(f'{yOpt}')


with open(minRMSEFile, "rb") as thisFile:
    modelMinRMSE = pickle.load(thisFile)

with open(maxR2File, "rb") as thisFile:
    modelMaxR2 = pickle.load(thisFile)

predictionMinRMSE_mean, predictionMinRMSE_std = modelMinRMSE.predict(xOpt, return_std=True)
print(f'Prediction: {predictionMinRMSE_mean} +/- {predictionMinRMSE_std}')
predictionMaxR2_mean, predictionMaxR2_std = modelMaxR2.predict(xOpt, return_std=True)
print(f'Prediction: {predictionMaxR2_mean} +/- {predictionMaxR2_std}')

rmseMinRMSE = np.sqrt(mean_squared_error(yOpt, predictionMinRMSE_mean))
rmseMaxR2 = np.sqrt(mean_squared_error(yOpt, predictionMaxR2_mean))

print(f'RMSE using minRMSEModel: {rmseMinRMSE}')
print(f'RMSE using maxR2Model: {rmseMaxR2}')
