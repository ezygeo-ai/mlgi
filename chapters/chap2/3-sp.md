---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# Self Potential (SP)

```{contents}
:local:
```

The purpose of this repository is to reconstruct paper from Y. Kim and N. Nakata (The Leading Edge, Volume 37, Issue 12, Dec 2018) about [Geophysical inversion versus machine learning in inverse problems](https://library.seg.org/doi/10.1190/tle37120894.1) and B. Russel (The Leading Edge, Volume 38, Issue 7, Jul 2019) about [Machine learning and geophysical inversion — A numerical study](https://library.seg.org/doi/10.1190/tle38070512.1).

Reference: Inversion of Self Potential Anomalies with Multilayer Perceptron Neural Networks [Ilknur Kaftan et. al, 2014, Pure Appl. Geophys](https://link.springer.com/article/10.1007/s00024-014-0778-y)
Syntethic data was created from sphere model (using [fwd_sp.py](https://github.com/ezygeo-ai/mlgi/blob/master/scripts/fwd_sp.py)) with parameters K = 94,686, h = 41.81 m, alpha = 309.37, dan x0 = 77.07 m. This result can be downloaded [here](https://github.com/ezygeo-ai/mlgi/blob/master/data/SP_syn_data.pickle) and seen below with noise distribution. 

```{figure} /figures/chap2/results/syntethic_data.png
---
name: syntethic_data
---
```
```{figure} /figures/chap2/results/noise_distribution.png
---
name: noise_distribution
---
```