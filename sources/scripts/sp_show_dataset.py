# Code was created by M. Heriyanto, 2020/01/13
# https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/scripts/sp_show_dataset.py

import numpy as np
import matplotlib.pyplot as plt
import pickle
import os.path

# Visualization of the data set
# for windows
with open(os.path.dirname(os.path.abspath(__file__)) + '/../data/SP_syn_data.pickle', 'rb') as f:
    sp_dataset = pickle.load(f)

# for linux
#with open(os.path.dirname(__file__) + '/../data/SP_syn_data.pickle', 'rb') as f:
#    position, SPData_syntethic = pickle.load(f)

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
        X_valid.append(getSPData[1])   # SPdata_noise
        y_valid.append(param)
    it_split = it_split + 1

for i in np.arange(itrain):
    plt.plot(measure_loc, X_train[i], 'b.')

plt.xlabel('position (m)')
plt.ylabel('SP data (mV)')
plt.title('Self-Potential Dataset: Training')
plt.grid()
plt.show()

for i in np.arange(ndata-itrain):
    plt.plot(measure_loc, X_valid[i], 'r.')

plt.xlabel('position (m)')
plt.ylabel('SP data (mV)')
plt.title('Self-Potential Dataset: Validation')
plt.grid()
plt.show()

