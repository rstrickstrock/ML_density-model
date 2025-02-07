import torch
#import torch.optim as optim
import optuna
from torch.utils.data import TensorDataset, DataLoader

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
#import numpy as np
#import os
#import shutil

import pickle
#print(f'{torch.__version__}')

def objective(trial):
    # hyper parameter definition
    lr = trial.suggest_float('lr', 1e-5, 1e-1, log=True)
    hidden_size = trial.suggest_int('hidden_size', 10, 50)
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    # model training
    for epoch in range(100):
        for inputs, targets in train_dl:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets.view(-1, 1))
            loss.backward()
            optimizer.step()

    # evaluation of model
    model.eval()
    with torch.no_grad():
        predictions = model(X_TESTSobol1)
        test_loss = criterion(predictions, Y_TESTSobol1.view(-1, 1)).item()

    return test_loss

## Sobol1 sampling
data_sobol1 = pd.read_csv('CLEANED_sobolsampling-2048.csv')
data_sobol1 = data_sobol1.drop(data_sobol1.columns[0], axis=1)
X_sobol1 = data_sobol1.drop('density', axis=1)
Y_sobol1 = data_sobol1['density']
#print(f'{data_sobol1}')
#print(f'{X_sobol1}')
#print(f'{Y_sobol1}')
print(f'{X_sobol1.shape}')
print(f'{Y_sobol1.shape}')

X_train, X_test, Y_train, Y_test = train_test_split(X_sobol1, Y_sobol1, test_size=0.05, random_state=29)
X_TRAINSobol1 = torch.tensor(X_train.to_numpy())
Y_TRAINSobol1 = torch.tensor(Y_train.to_numpy())
X_TESTSobol1 = torch.tensor(X_test.to_numpy())
Y_TESTSobol1 = torch.tensor(Y_test.to_numpy())
#print(f'{X_TRAINSobol1}')
#print(f'{Y_TRAINSobol1}')

# type change into TensorDataset
train_data_nn = TensorDataset(X_TRAINSobol1, Y_TRAINSobol1)

# setting batch size and dataloader
batch_size = len(X_TRAINSobol1)
train_dl = DataLoader(train_data_nn, batch_size, shuffle=True)

# Model structure
model = net = torch.nn.Sequential(
        torch.nn.Linear(4, 100),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(100, 1),
    )
epoch_count = 0

#study = optuna.create_study(direction='minimize')
#study.optimize(objective, n_trials=10)
#lr_optuna = study.best_trial.params['lr']
#print('Best trial:', study.best_trial.params)
# optimizer = torch.optim.Adam(model.parameters(), lr=lr_optuna)

optimizer = torch.optim.Adam(model.parameters(), lr=0.00002)

num_epochs = 100
loss_fn = torch.nn.MSELoss()

for epoch in range(num_epochs):
    for step, (xb, yb) in enumerate(train_dl):
        pred = model(xb)

        loss = loss_fn(pred, yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # if epoch%10 == 9:
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

    epoch_count = epoch_count+1