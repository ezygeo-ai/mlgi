[![HitCount](http://hits.dwyl.com/ezygeo-ai/machine-learning-and-geophysical-inversion.svg)](http://hits.dwyl.com/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub contributors](https://img.shields.io/github/contributors/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub last commit](https://img.shields.io/github/last-commit/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub top language](https://img.shields.io/github/languages/top/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub language count](https://img.shields.io/github/languages/count/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub repo size](https://img.shields.io/github/repo-size/ezygeo-ai/machine-learning-and-geophysical-inversion)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ezygeo-ai/machine-learning-and-geophysical-inversion)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555)](https://www.linkedin.com/company/28696953)

# Machine Learning and Geophysical Inversion

The pupose of this repo is to reconstruct paper from Y. Kim and N. Nakata (The Leading Edge, Volume 37, Issue 12, Dec 2018) about [Geophysical inversion versus machine learning in inverse problems](https://library.seg.org/doi/10.1190/tle37120894.1) and B. Russel (The Leading Edge, Volume 38, Issue 7, Jul 2019) about [Machine learning and geophysical inversion — A numerical study](https://library.seg.org/doi/10.1190/tle38070512.1). We construct this paper using **Python** and **PyCharm IDE**.

Before I will do it, I just try to compare Machine Learning (Multilayer Perceptron Neural Networks
(MLPNN)) and Geophysical Inversion (traditional Damped Least Squares (Levenberg–Marquardt) inversion technique (DLS)) using paper from Ilknur Kaftan (Pure Appl. Geophys., Vol. 171, Issue 8, pp 1939–1949, 2014) about [Inversion of Self Potential Anomalies with Multilayer Perceptron Neural Networks](https://link.springer.com/article/10.1007/s00024-014-0778-y).

## Machine Learning and Geophysical Inversion: Self-Potential Case
Reference: Inversion of Self Potential Anomalies with Multilayer Perceptron Neural Networks [Ilknur Kaftan et. al, 2014, Pure Appl. Geophys](https://link.springer.com/article/10.1007/s00024-014-0778-y)
Syntethic data was created from sphere model (using [fwd_sp.py](https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/fwd_sp.py)) with parameters K = 94,686, h = 41.81 m,
alpha = 309.37, dan x0 = 77.07 m. This result can be downloaded [here](https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/data/SP_syn_data.pickle) and seen below. 

<p align="center">
<img src="https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/figure/syntethic_data.png" width="80%">
</p>

Self-Potential Dataset that was generated with 5,000 different spherical models (using [sp_make_dataset.py](https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/sp_make_dataset.py)) with differing electrical dipole moment, polarization angle, origin and depth to the centre of sphere [here](https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/data/SP_Dataset.pickle) and seen below (using [sp_show_dataset.py](https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/sp_show_dataset.py)). This dataset contains training (**80%**) dan validation (**20%**) dataset.

<p align="center">
<img src="https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/figure/training_dataset.png" width="40%"> <img src="https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/blob/master/figure/validation_dataset.png" width="40%">
</p>
