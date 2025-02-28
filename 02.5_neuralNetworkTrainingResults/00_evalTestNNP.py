import torch
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import numpy as np

## Sobol1 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']
#print(f'{data_sobol1}')
#print(f'{X_sobol1}')
#print(f'{Y_sobol1}')
#print(f'{X_sobol1.shape}')
#print(f'{Y_sobol1.shape}')

X_train, X_test, Y_train, Y_test = train_test_split(X_sobol1, Y_sobol1, test_size=0.05, random_state=29)
X_TRAINSobol1 = torch.FloatTensor(X_train.to_numpy())
Y_TRAINSobol1 = torch.FloatTensor(Y_train.to_numpy())
X_TESTSobol1 = torch.FloatTensor(X_test.to_numpy())
Y_TESTSobol1 = torch.FloatTensor(Y_test.to_numpy())
#print(f'{X_TRAINSobol1}')
#print(f'{Y_TRAINSobol1}')

# type change into TensorDataset
TrainSobol1 = TensorDataset(X_TRAINSobol1, Y_TRAINSobol1)
TestSobol1 = TensorDataset(X_TESTSobol1, Y_TESTSobol1)

# setting batch size and dataloader
batch_size = len(TrainSobol1)

trainSobol1DL = DataLoader(TrainSobol1, batch_size, shuffle=True)
testSobol1DL = DataLoader(TestSobol1, batch_size, shuffle=True)

# Model structure0
model = net = torch.nn.Sequential(
        torch.nn.Linear(4, 512),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(512, 2048),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(2048, 64),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(64, 4),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(4, 1),
    )
#print(f'model:\n{model}')
#print(f'model[0].weight:\n{model[0].weight}')

## loading model
device = 'cpu'
#model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model-37_0.1716.pth", weights_only=True))
#print(f'model:\n{model}')
#print(f'model[0].weight:\n{model[0].weight}')

## test model
loss_fn = torch.nn.MSELoss()
for step, (xb, yb) in enumerate(testSobol1DL):
    print(f'TODO: CHANGE RMSE TO MAPE!!!!!!')
    #print(f'step: {step}')
    size = len(yb)
    #print(f'size: {size}')
    pred = model(xb)
    #print(f'pred: {pred}')
    #print(f'yb: {yb}')
    npPred = pred.detach().numpy()
    #print(f'{len(npPred)}')
    npY = yb.detach().numpy()
    #print(f'{len(npY)}')
    lossAbs = []
    lossRel = []
    for i in range(0, len(npPred)):
        #print(f'{float(pred[i])}')
        #print(f'{float(npY[i])}')
        thisAbsLoss = np.sqrt(np.power(float(pred[i])-float(npY[i]), 2))
        lossAbs.append(thisAbsLoss)
        lossRel.append(thisAbsLoss/npY[i])
    #print(f'{lossAbs}')
    #print(f'{lossRel}')
    avgLossAbs = np.sum(lossAbs)/size
    avgLossRel = np.sum(lossRel)/size
    print(f'avgLossAbs: {avgLossAbs}')
    print(f'avgLossRel: {avgLossRel}')
    
for step, (xb, yb) in enumerate(trainSobol1DL):
    #print(f'step: {step}')
    size = len(yb)
    #print(f'size: {size}')
    pred = model(xb)
    #print(f'pred: {pred}')
    #print(f'yb: {yb}')
    npPred = pred.detach().numpy()
    #print(f'{len(npPred)}')
    npY = yb.detach().numpy()
    #print(f'{len(npY)}')
    lossAbs = []
    lossRel = []
    for i in range(0, len(npPred)):
        #print(f'{float(pred[i])}')
        #print(f'{float(npY[i])}')
        thisAbsLoss = np.sqrt(np.power(float(pred[i])-float(npY[i]), 2))
        lossAbs.append(thisAbsLoss)
        lossRel.append(thisAbsLoss/npY[i])
    #print(f'{lossAbs}')
    #print(f'{lossRel}')
    avgLossAbs = np.sum(lossAbs)/size
    avgLossRel = np.sum(lossRel)/size
    print(f'avgLossAbs: {avgLossAbs}')
    print(f'avgLossRel: {avgLossRel}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
