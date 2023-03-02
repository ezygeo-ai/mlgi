# Ref: https://github.com/rcassani/mlp-example/blob/master/mlp_notebook.ipynb

import mlp
# from mlp import *

import numpy as np
import matplotlib.pyplot as plt
import pickle

import os.path

# === Loading Dataset
# for windows
with open(os.path.dirname(os.path.abspath(__file__)) + '/../data/SP_Dataset.pickle', 'rb') as f:
    sp_dataset = pickle.load(f)

# for linux
#with open(os.path.dirname(__file__) + '/../data/SP_Dataset.pickle', 'rb') as f:
#    sp_dataset = pickle.load(f)

ndata, ncol = np.shape(sp_dataset)
itrain = int(0.8 * ndata)
print('train data: ', itrain)
measure_loc = np.linspace(0, 150, 101)
X_train = []
X_valid = []
y_train = []
y_valid = []
it_split = 1

# getSPData contains SPdata, SPdata_noise, and noise_data
for param, getSPData in sp_dataset:
    # split data for training and validation
    if it_split <= itrain:
        X_train.append(getSPData[1])  # SPdata_noise
        y_train.append(param)
    else:
        X_valid.append(getSPData[1])  # SPdata_noise
        y_valid.append(param)
    it_split = it_split + 1

# Training data
X_train = np.array(X_train)
y_train = np.array(y_train)

# size X_train and y_train
print('size X_train: ', X_train.shape)
print('size y_train: ', y_train.shape)

# === Create MLP object
# input: 101 | hidden 1: 2 | hidden 2: 5 | output: 4
mlp_regression = mlp.Mlp(size_layers=[101, 2, 5, 4],
                         act_funct='relu',  # tanh
                         reg_lambda=0.1,
                         bias_flag=True)
print(mlp_regression)

# === Training MLP object
# Training with Backpropagation and 400 iterations
iterations = 150    # epoch
loss = np.zeros([iterations, 1])

for ix in range(iterations):
    mlp_regression.train(X_train, y_train, 1)
    Y_hat = mlp_regression.predict(X_train)
    y_tmp = np.argmax(Y_hat, axis=1)
    # y_hat = labels[y_tmp]
    y_hat = Y_hat

    loss[ix] = (0.5) * np.square(y_hat - y_train).mean()

# Ploting loss vs iterations
plt.figure()
ix = np.arange(iterations)
plt.plot(ix, loss)

# Training Accuracy
Y_hat = mlp_classifier.predict(X_train)
y_tmp = np.argmax(Y_hat, axis=1)
# y_hat = labels[y_tmp]

# acc = np.mean(1 * (y_hat == y_train))
# print('Training Accuracy: ' + str(acc*100))