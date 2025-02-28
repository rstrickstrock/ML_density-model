import torch
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_percentage_error as skmape
import pandas as pd
import os
import shutil
import numpy as np


testmode = True

dataset = "Grid1296"

rndInts = [678, 147, 561, 237, 588, 951, 490, 395, 877, 297, 721, 711, 985, 171, 75, 16, 669, 530, 999, 794, 936, 111, 816, 968, 48, 986, 829, 996, 272, 759, 390, 930, 633, 928, 854, 554, 562, 78, 222, 294, 725, 582, 731, 249, 791, 35, 180, 510, 593, 634]

testSize = [0.80]

statisticsFileName = f'StatsPart-{dataset}-{testSize[0]}.csv'

learningRate = 0.001
num_epochs = 1000

print(f'Dataset: {dataset}')
print(f'num_epochs: {num_epochs}')
print(f'learning rate: {learningRate}')

pwd = os.getcwd()
### create current working directory ###
cwd = os.path.join(pwd, "trainedModels")
#print(f'{cwd}')
if os.path.exists(cwd):
  if testmode:
    #shutil.rmtree(cwd)
    pass
  else:
    print(f'\nPATH \'{cwd}\' already exists. \n\nExiting without starting or changing anything.\n')
    exit()
else:
  os.mkdir(cwd)
#os.mkdir(cwd)

## grid sampling 1296
data1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
data1296 = data1296.drop(data1296.columns[0], axis=1)
X_1296 = data1296.drop('density', axis=1)
Y_1296 = data1296['density']
#print(f'{data1296}')
#print(f'{X_1296}')
#print(f'{Y_1296}')

## grid sampling 2401
data2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
data2401 = data2401.drop(data2401.columns[0], axis=1)
X_2401 = data2401.drop('density', axis=1)
Y_2401 = data2401['density']
#print(f'{data2401}')
#print(f'{X_2401}')
#print(f'{Y_2401}')

## sobol2 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']
#print(f'{data_sobol1}')
#print(f'{X_sobol1}')
#print(f'{Y_sobol1}')

## sobol2 sampling
data_sobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
data_sobol2 = data_sobol2.drop(data_sobol2.columns[0], axis=1)
X_sobol2 = data_sobol2.drop('density', axis=1)
Y_sobol2 = data_sobol2['density']
#print(f'{data_sobol2}')
#print(f'{X_sobol2}')
#print(f'{Y_sobol2}')

dfStatistics = pd.DataFrame({"ratio": [],
                             "rndint": [],
                             "dataset": [],
                             "learning_rate": [],
                             "epoch": [],
                             "rmse": [],
                             "mape": [],
                             "r2": []})


for thisRatio in testSize:
  trainSize = 1-thisRatio
  print(f'Training NN Models with {trainSize}% of the dataset.\n')
  tmp_cwd = os.path.join(cwd, str(thisRatio))
  #print(f'{tmp_cwd}')
  if os.path.exists(tmp_cwd):
    if testmode:
      pass
      #shutil.rmtree(cwd)
    else:
      print(f'\nPATH \'{cwd}\' already exists. \n\nExiting without starting or changing anything.\n')
      exit()
  else:
    os.mkdir(tmp_cwd)
  os.chdir(tmp_cwd)
  
  for rndInt in rndInts:
    print(f'rndInt: {rndInt}')
    ## split dataset into test/train data
    X_train, X_test, Y_train, Y_test = train_test_split(X_1296, Y_1296, test_size=thisRatio, random_state=rndInt)
    X_TRAIN = torch.FloatTensor(X_train.to_numpy())
    Y_TRAIN = torch.FloatTensor(Y_train.to_numpy())
    Train = TensorDataset(X_TRAIN, Y_TRAIN)
    
    X_test = pd.concat([X_test, X_2401, X_sobol1, X_sobol2], ignore_index=True)
    Y_test = pd.concat([Y_test, Y_2401, Y_sobol1, Y_sobol2], ignore_index=True)
    X_TEST = torch.FloatTensor(X_test.to_numpy())
    Y_TEST = torch.FloatTensor(Y_test.to_numpy())
    Test = TensorDataset(X_TEST, Y_TEST)
    
    ## setting batch size and dataloader
    batchSize = len(Train)
    
    trainDL = DataLoader(Train, batchSize, shuffle=True)
    testDL = DataLoader(Test, batchSize, shuffle=True)
    
    ## setup model structure
    model = net = torch.nn.Sequential(
                    torch.nn.Linear(4, 8),
                    torch.nn.LeakyReLU(),
                    torch.nn.Linear(8, 1),
                   )
    #print(f'model:\n{model}')
    
    ## train model

    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)
    
    modelNameOld = None
    thisRMSE = None
    thisMape = None
    thisR2 = None
    thisEpoch = None
    lossOld = None
    for epoch in range(num_epochs):
      print(f'  epoch: {epoch}')
      for step, (xb, yb) in enumerate(trainDL):
        #print(f'  xb: {xb}')
        #print(f'  yb: {yb}')
        #print(f'  type(yb): {type(yb)}')
        ybNumpy = yb.detach().numpy()
        #print(f'  ybNumpy: {ybNumpy}')
        #print(f'  type(ybNumpy): {type(ybNumpy)}')
        pred = model(xb)
        predNumpy = pred.detach().numpy()
        #print(f'  pred: {pred}')
        #print(f'  pred.detach().numpy(): {predNumpy}')
        #print(f'  type(pred.detach().numpy()): {type(predNumpy)}')
        loss = loss_fn(pred, yb)
        #print(f'  loss: {loss}')
        #print(f'  loss.item(): {loss.item()}')
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
          
        if epoch%10 == 9:
          print(f'  Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
          
        thisRMSE = 0
        thisMape = 0
        thisR2 = 0
        i = 0
        for tmpStep, (tmpXB, tmpYB) in enumerate(testDL):
          #print(f'    step: {tmpStep}')
          #print(f'    tmpXB: {tmpXB}')
          #print(f'    tmpYB: {tmpYB}')
          tmpYBNumpy = tmpYB.detach().numpy()
          tmpPred = model(tmpXB)
          tmpPredNumpy = tmpPred.detach().numpy()
          #
          thisRMSE = thisRMSE + np.sqrt(mean_squared_error(tmpYBNumpy, tmpPredNumpy))
          thisMape = thisMape + skmape(tmpYBNumpy, tmpPredNumpy)
          thisR2 = thisR2 + r2_score(tmpYBNumpy, tmpPredNumpy)
          #print(f'    rmse: {thisRMSE}')
          #print(f'    mape: {thisMape}')
          #print(f'    r2: {thisR2}')
          i = i + 1
        #print(f'    i:{i}')
        thisRMSE = thisRMSE/i
        thisMape = thisMape/i
        thisR2 = thisR2/i
        thisEpoch = epoch+1
        
        if epoch == 0:
          lossOld = thisMape
          modelName = f'model-{thisRatio}-{rndInt}-{dataset}_{thisEpoch}_{thisMape:.4f}_{thisR2:.4f}.pth'
          ## saving model
          torch.save(model.state_dict(), modelName)
          print(f'    Saved PyTorch Model State to {modelName}')
          print(f'    rmse: {thisRMSE}')
          print(f'    mape: {thisMape}')
          print(f'    r2: {thisR2}')
          modelNameOld = modelName
          optEpoch = thisEpoch
          optRMSE = thisRMSE
          optMape = thisMape
          optR2 = thisR2
        elif lossOld > thisMape:
          lossOld = thisMape
          modelName = f'model-{thisRatio}-{rndInt}-{dataset}_{thisEpoch}_{thisMape:.4f}_{thisR2:.4f}.pth'
          ## saving model
          torch.save(model.state_dict(), modelName)
          print(f'    Saved PyTorch Model State to {modelName}')
          print(f'    rmse: {thisRMSE}')
          print(f'    mape: {thisMape}')
          print(f'    r2: {thisR2}')
          ## remove old model file:
          if os.path.exists(modelNameOld):
            os.remove(modelNameOld)
            print(f'      Removed old PyTorch Model State {modelNameOld}')
          modelNameOld = modelName
          optEpoch = thisEpoch
          optRMSE = thisRMSE
          optMape = thisMape
          optR2 = thisR2
        else:
          print(f'    rmse: {thisRMSE} (rejected)')
          print(f'    mape: {thisMape} (rejected)')
          print(f'    r2: {thisR2} (rejected)')
    
    dfEntry = pd.DataFrame({"ratio": [thisRatio],
                            "rndint": [rndInt],
                            "dataset": [dataset],
                            "learning_rate": [learningRate],
                            "epoch": [optEpoch],
                            "rmse": [optRMSE],
                            "mape": [optMape],
                            "r2": [optR2]})
    dfStatistics = pd.concat([dfStatistics, dfEntry], ignore_index=True)
    print(f'\n')
    #break
  os.chdir(cwd)
    
os.chdir(pwd)
if os.path.exists(statisticsFileName):
  os.remove(statisticsFileName)
  print(f'Removed existing statistics file: \'{statisticsFileName}\'.')
dfStatistics.to_csv(statisticsFileName)
print(f'Wrote statistics to file: \'{statisticsFileName}\'.')
print(f'{dfStatistics}')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
