# Code was created by M. Heriyanto, 2020/01/13
# Ref: Ilknur Kaftan, et. al. 2014. Pure Appl. Geophys. Vol. 171, Issue 8, pp 1939–1949

import numpy as np
import random as rd
import pickle


# SP forward function
def SPfunc(x, par):
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

    # === give noise for data (Gaussian Noise) 1
    std_noise = 10  # = %
    mean_noise = 0
    noise_data = np.random.normal(mean_noise, np.sqrt(std_noise), len(SPdata))
    SPdata_noise = SPdata + noise_data

    return SPdata, SPdata_noise, noise_data


# === MAKE SYNTHETIC DATASET
min_x0 = 50
max_x0 = 100
n_x0 = 7    # point
val_x0 = np.linspace(min_x0, max_x0, n_x0)

min_alpha = 260
max_alpha = 340
n_alpha = 7     # point
val_alpha = np.linspace(min_alpha, max_alpha, n_alpha)

min_ht = 7
max_ht = 75
n_ht = 5    # point
val_h = np.linspace(min_ht, max_ht, n_ht)

min_K = 70000
max_K = 110000
n_K = 7     # point
val_K = np.linspace(min_K, max_K, n_K)

dataset = []
ndata = 5000
for it_dat in range(ndata):
    # x0s = min_x0 + (max_x0 - min_x0) * np.random.rand()
    x0s = rd.choice(val_x0)

    # alphas = min_alpha + (max_alpha - min_alpha) * np.random.rand()
    alphas = rd.choice(val_alpha)

    # hs = min_ht + (max_ht - min_ht) * np.random.rand()
    hs = rd.choice(val_h)

    # Ks = min_K + (max_K - min_K) * np.random.rand()
    Ks = rd.choice(val_K)

    par_mod = [x0s, alphas, hs, Ks]

    measure_loc = np.linspace(0, 150, 101)     # Location of measurement
    get_SPData = SPfunc(measure_loc, par_mod)
    dataset.append((par_mod, get_SPData))  # [(input, output)]


with open('data/SP_Dataset.pickle', 'wb') as f:
    pickle.dump(dataset, f)
