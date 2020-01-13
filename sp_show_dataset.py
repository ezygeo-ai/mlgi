# Code was created by M. Heriyanto, 2020/01/13

import numpy as np
import matplotlib.pyplot as plt
import pickle

# Visualization of the data set
with open('data/SP_Dataset.pickle', 'rb') as f:
    SPdataset = pickle.load(f)

ndata, ncol = np.shape(SPdataset)
itrain = int(0.8 * ndata)
print('train data: ', itrain)
measure_loc = np.linspace(0, 150, 101)
X_train = []
X_valid = []
y_train = []
y_valid = []
it_split = 1

# getSPData contains SPdata, SPdata_noise, and noise_data
for param, getSPData in SPdataset:
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
