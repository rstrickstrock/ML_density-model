### imports ###
from sklearn.gaussian_process import GaussianProcessRegressor
import pandas as pd
import os
import pickle

parametersFile = 'this_parameters.csv'
modelFile = 'trained_modelSobol1_0.05_111_Matern.sav'
predictionFile = 'this_prediction.csv' 

thisParameters = pd.read_csv(parametersFile)
#print(f'{thisParameters}')
thisParameters = thisParameters.drop('density', axis=1)
#print(f'{thisParameters}')

with open (modelFile, "rb") as model:
  thisModel = pickle.load(model)
  
thisPrediction = thisModel.predict(thisParameters)
print(f'{thisPrediction}')
thisDF = pd.DataFrame({"prediction": []})
for pred in thisPrediction:
  tmpDF = pd.DataFrame({"prediction": [pred]})
  thisDF = pd.concat([thisDF, tmpDF], ignore_index=True)
  
print(f'{thisDF}')

if os.path.exists(predictionFile):
  os.remove(predictionFile)
  print(f'Removed existing predictions file: \'{predictionFile}\'.')
thisDF.to_csv(predictionFile)
print(f'Wrote prediction(s) to file: \'{predictionFile}\'.')
#print(f'{thisDF}')
