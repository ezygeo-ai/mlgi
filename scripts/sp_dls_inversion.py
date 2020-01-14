# Code was created by M. Heriyanto, 2020/01/13
# https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/scripts/sp_dls_inversion.py

import numpy as np
import matplotlib.pyplot as plt
import pickle
import os.path

from scipy.optimize import least_squares as ls

# === input syntethic data with noise 10 %
with open(os.path.dirname(__file__) + '/../data/SP_syn_data.pickle', 'rb') as f:
    position, SPData_syntethic = pickle.load(f)


# forward function
def fungsi(par, x):
    x0 = par[0]
    alpha = par[1]
    h = par[2]
    K = par[3]

    SPdata = []
    for i in x:
        var_up = (i - x0) * np.cos(alpha) - h * np.sin(alpha)
        var_down = ((i - x0)*(i - x0) + h*h) ** (3/2)
        var = K * (var_up / var_down)
        SPdata.append(var)

    return SPdata


# misfit equation
def pers(m, x, y):
    return fungsi(m, x) - y


# initial model
x0 = 20  # m
alpha = 300 * (np.pi/180)
h = 40   # m
K = 94500
m0 = np.array([x0, alpha, h, K])

# Levenberg-Marquardt (LM) algorithm
# Ref: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html
result = ls(pers, m0, method='lm', args=(position, SPData_syntethic))
x0 = result.x[0]
alpha = result.x[1]
h = result.x[2]
K = result.x[3]
m = np.array([x0, alpha, h, K])
SPData_calculation = fungsi(m, position)

# real data without noise
x0_real = 77.07  # m
alpha_real = 309.37 * (np.pi/180)
h_real = 41.81   # m
K_real = 94686
m_real = np.array([x0_real, alpha_real, h_real, K_real])
SPData_real = fungsi(m_real, position)

# === Output
print('Real Model x0: %f | alpha: %f | h: %f | K: %f' % (x0_real, alpha_real, h_real, K_real))
print('Inversion Model x0: %f | alpha: %f | h: %f | K: %f' % (x0, alpha, h, K))
print('Error: %f' % (result.optimality * 100))

plt.plot(position, SPData_real, 'b.', label='Real')
plt.plot(position, SPData_syntethic, 'r*', label='Syn')
plt.plot(position, SPData_calculation, 'g', label='Cal')
plt.grid()
plt.xlabel('position (m)')
plt.ylabel('SP data (mV)')
plt.legend()
plt.title('SP Syntethic Data (Syn) Vs Inversion Result (Cal)')
plt.show()
