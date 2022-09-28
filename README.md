[![HitCount](http://hits.dwyl.com/ezygeo-ai/machine-learning-and-geophysical-inversion.svg)](http://hits.dwyl.com/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub contributors](https://img.shields.io/github/contributors/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub last commit](https://img.shields.io/github/last-commit/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub top language](https://img.shields.io/github/languages/top/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub language count](https://img.shields.io/github/languages/count/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub repo size](https://img.shields.io/github/repo-size/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ezygeo-ai/machine-learning-and-geophysical-inversion)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555)](https://www.linkedin.com/company/28696953)

# Machine Learning for Geophysical Inversion

The purpose of this repository is to reconstruct paper from Y. Kim and N. Nakata (The Leading Edge, Volume 37, Issue 12, Dec 2018) about [Geophysical inversion versus machine learning in inverse problems](https://library.seg.org/doi/10.1190/tle37120894.1) and B. Russel (The Leading Edge, Volume 38, Issue 7, Jul 2019) about [Machine learning and geophysical inversion — A numerical study](https://library.seg.org/doi/10.1190/tle38070512.1). We construct this paper using **Python** and **PyCharm IDE**.

Before I will do it, I just try to compare Machine Learning (Multilayer Perceptron Neural Networks
(MLPNN)) and Geophysical Inversion (traditional Damped Least Squares (Levenberg–Marquardt) inversion technique (DLS)) using paper from Ilknur Kaftan (Pure Appl. Geophys., Vol. 171, Issue 8, pp 1939–1949, 2014) about [Inversion of Self Potential Anomalies with Multilayer Perceptron Neural Networks](https://link.springer.com/article/10.1007/s00024-014-0778-y).

## Machine Learning and Geophysical Inversion: Self-Potential Case
Reference: Inversion of Self Potential Anomalies with Multilayer Perceptron Neural Networks [Ilknur Kaftan et. al, 2014, Pure Appl. Geophys](https://link.springer.com/article/10.1007/s00024-014-0778-y)
Syntethic data was created from sphere model (using [fwd_sp.py](scripts/fwd_sp.py)) with parameters K = 94,686, h = 41.81 m, alpha = 309.37, dan x0 = 77.07 m. This result can be downloaded [here](data/SP_syn_data.pickle) and seen below with [noise distribution](images/results/noise_distribution.png). 

<p align="center">
<img src="images/results/syntethic_data.png" width="45%"> <img src="images/results/noise_distribution.png" width="45%">
</p>

<ins>**Geophysical Inversion: Damped Least Squares (Levenberg–Marquardt) inversion (DLS)**</ins>

I use DLS algorithm from [Kode Praktikum GP2103 Metode Komputasi versi Python](https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python) tutorial: [Modul 6 - Metode Komputasi 2018 - GP UP.pdf, page 34](https://osf.io/36yh8/) and [pm6f.py](https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python/blob/master/pm6f.py) code. This result was showed using [sp_dls_inversion.py](scripts/sp_dls_inversion.py) below.

<p align="center">
<img src="images/results/sp_dls_inv_result.png" width="80%">
</p>

**Initial Model** x0: 20 | alpha: 100 (deg) | h: 40 | K: 94500

**Real Model** x0: 77.070000 | alpha: 5.399525 (rad) | h: 41.810000 | K: 94686.000000

**Inversion Model** x0: 76.243426 | alpha: 5.415794 (rad) | h: 42.776603 | K: 99102.106072

**Error**: 0.029529 %

with research paper reference [W. Srigutomo, et al, 2016](http://ijphysics.com/index.php/ijp/article/view/138) that is modified [sp_dls_inversion_scratch.py]() below. Jacobian matrix was calculated using [derrivatives_in_python.py](scripts/derrivatives_in_python.py).

<ins>**Machine Learning: Multilayer Perceptron Neural Networks (MLPNN)**</ins>

Self-Potential Dataset that was generated with 5,000 different spherical models (using [sp_make_dataset.py](scripts/sp_make_dataset.py)) with differing electrical dipole moment, polarization angle, origin and depth to the centre of sphere [here](data/SP_Dataset.pickle) and seen below (using [sp_show_dataset.py](scripts/sp_show_dataset.py)). This dataset contains training (**80%**) dan validation (**20%**) dataset.

<p align="center">
<img src="images/results/training_dataset.png" width="40%"> <img src="images/results/validation_dataset.png" width="40%">
</p>

This MLPNN used two (2) hidden layers, input layer used 101 point of data (neurons), first layer used 2 neurons and second layer used five (5) neurons. Then, learning rate = 0.1, activation function = hyperbolic tangent sigmoid function. The final MSE = 0.00306092 from 150 epochs.

<p align="center">
<img src="images/tutorials/mlp.png" width="80%">
</p>
