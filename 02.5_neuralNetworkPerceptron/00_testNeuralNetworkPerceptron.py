### imports ###
import torch
import torch.optim as optim

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_percentage_error as skmape

import pandas as pd
import numpy as np
import os
import shutil

import pickle
#print(f'{torch.__version__}')

from sklearn import preprocessing


def print_array_specs(in_arrays: dict):
    ''' Helper function for nicely printing NumPy and
        PyTorch arrays.

        Print: shape, data type and values.
    '''
    for key, value in in_arrays.items():
        print(f'{key}:\n{value.shape}, {value.dtype}')
        print(f'{value}\n')

rng = np.random.default_rng(seed=29)

input_X1_np = rng.normal(size=(2, 10))
target_Y2_np = rng.normal(size=(2, 1))
#print(f'{input_X1_np.shape}')
#print(f'{target_Y2_np.shape}')

weight_W1_np = rng.normal(size=(10, 3))
weight_W2_np = rng.normal(size=(3, 1))

objects_ini = {'input_X1': input_X1_np, 'target_Y2': target_Y2_np,
               'weight_W1': weight_W1_np, 'weight_W2': weight_W2_np}

#print_array_specs(in_arrays=objects_ini)

#input_width = 10
#hidden_width = 3
#output_width = 1

#learning_rate = 1e-3
#num_epochs = 50

#input_X1 = torch.from_numpy(input_X1_np)
#target_Y2 = torch.from_numpy(target_Y2_np)

#weight_W1 = torch.from_numpy(weight_W1_np).requires_grad_(requires_grad=True)
#weight_W2 = torch.from_numpy(weight_W2_np).requires_grad_(requires_grad=True)

#bias_B1 = torch.zeros(hidden_width, requires_grad=True)
#bias_B2 = torch.zeros(output_width, requires_grad=True)

#objects_ini = {'input_X1': input_X1, 'target_Y2': target_Y2,
#               'weight_W1': weight_W1, 'input_B1': bias_B1,
#               'weight_W2': weight_W2, 'input_B2': bias_B2}

#print_array_specs(in_arrays=objects_ini)

#for epoch in range(num_epochs):
    # Forward pass
#    X2 = torch.matmul(input_X1, weight_W1) + bias_B1

#    activation = torch.nn.ReLU()
#    Y1 = activation(X2)

#    output_Y2 = torch.matmul(Y1, weight_W2) + bias_B2

#    loss = torch.mean(torch.square(torch.subtract(output_Y2, target_Y2))) # mean( (Y2 - y_target)^2 )

    # Backward pass
#    loss.backward()

    # Optimization: update weights and biases, don't record operations
#    with torch.no_grad():
#        weight_W1 -= torch.mul(learning_rate, weight_W1.grad)
#        bias_B1 -= torch.mul(learning_rate, bias_B1.grad)
#        weight_W2 -= learning_rate * weight_W2.grad
#        bias_B2 -= learning_rate * bias_B2.grad

        # Reset the gradients to zero
#        weight_W1.grad.zero_()
#        bias_B1.grad.zero_()
#        weight_W2.grad.zero_()
#        bias_B2.grad.zero_()

#    print(f'Epoch {epoch + 1}: Loss = {loss.item():.3f}')




## grid sampling 1296
#data1296 = pd.read_csv('CLEANED_gridsearch_1296.csv')
#data1296 = data1296.drop(data1296.columns[0], axis=1)
#X_1296 = data1296.drop('density', axis=1)
#Y_1296 = data1296['density']
#print(f'{data1296}')
#print(f'{X_1296}')
#print(f'{Y_1296}')

## grid sampling 2401
#data2401 = pd.read_csv('CLEANED_gridsearch_2401.csv')
#data2401 = data2401.drop(data2401.columns[0], axis=1)
#X_2401 = data2401.drop('density', axis=1)
#Y_2401 = data2401['density']
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
print(f'{X_sobol1.shape}')
print(f'{Y_sobol1.shape}')


## sobol2 sampling
#data_sobol2 = pd.read_csv('CLEANED_sobolsampling-2048-2.csv')
#data_sobol2 = data_sobol2.drop(data_sobol2.columns[0], axis=1)
#X_sobol2 = data_sobol2.drop('density', axis=1)
#Y_sobol2 = data_sobol2['density']
#print(f'{data_sobol2}')
#print(f'{X_sobol2}')
#print(f'{Y_sobol2}')

input_width = 4
hidden_width = 3
output_width = 1

weight_W1_np = rng.normal(size=(input_width, hidden_width))
weight_W2_np = rng.normal(size=(hidden_width, output_width))

learning_rate = 1e-3
num_epochs = 1000

X_sobol1 = torch.from_numpy(X_sobol1.to_numpy())
Y_sobol1 = torch.from_numpy(Y_sobol1.to_numpy())

weight_W1 = torch.from_numpy(weight_W1_np).requires_grad_(requires_grad=True)
weight_W2 = torch.from_numpy(weight_W2_np).requires_grad_(requires_grad=True)

bias_B1 = torch.zeros(hidden_width, requires_grad=True)
bias_B2 = torch.zeros(output_width, requires_grad=True)

for epoch in range(num_epochs):
    # Forward pass
    X2 = torch.matmul(X_sobol1, weight_W1) + bias_B1

    activation = torch.nn.ReLU()
    Y1 = activation(X2)

    output_Y2 = torch.matmul(Y1, weight_W2) + bias_B2

    loss = torch.mean(torch.square(torch.subtract(output_Y2, Y_sobol1))) # mean( (Y2 - y_target)^2 )

    # Backward pass
    loss.backward()

    # Optimization: update weights and biases, don't record operations
    with torch.no_grad():
        weight_W1 -= torch.mul(learning_rate, weight_W1.grad)
        bias_B1 -= torch.mul(learning_rate, bias_B1.grad)
        weight_W2 -= learning_rate * weight_W2.grad
        bias_B2 -= learning_rate * bias_B2.grad

        # Reset the gradients to zero
        weight_W1.grad.zero_()
        bias_B1.grad.zero_()
        weight_W2.grad.zero_()
        bias_B2.grad.zero_()

    print(f'Epoch {epoch + 1}: Loss = {loss.item():.3f}')







































