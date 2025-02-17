import torch
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
import pandas as pd
import os

learningRate = 0.001

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
print(f'model:\n{model}')

num_epochs = 100
print(f'num_epochs: {num_epochs}')
loss_fn = torch.nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=lr_optuna)
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)
print(f'learning rate: {learningRate}')

lossOld = None
modelNameOld = None
print(f'\n')
for epoch in range(num_epochs):
    for step, (xb, yb) in enumerate(TrainSobol1):
        pred = model(xb)

        loss = loss_fn(pred, yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    #if epoch%10 == 9:
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
    if epoch == 0:
        lossOld = float(loss.item())
        modelName = f'model-{epoch+1}_{lossOld:.4f}.pth'
        ## saving model
        torch.save(model.state_dict(), modelName)
        print(f'\tSaved PyTorch Model State to {modelName}')
        modelNameOld = modelName

    if lossOld > float(loss.item()):
        lossOld = float(loss.item())
        modelName = f'model-{epoch+1}_{lossOld:.4f}.pth'
        ## saving model
        torch.save(model.state_dict(), modelName)
        print(f'\tSaved PyTorch Model State to {modelName}')
        ## remove old model file:
        if os.path.exists(modelNameOld):
            os.remove(modelNameOld)
            print(f'\tRemoved old PyTorch Model State {modelNameOld}')
        modelNameOld = modelName
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
