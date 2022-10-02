# Levenberg Marquardt (LM)

```{contents}
:local:
```

<ins>**Geophysical Inversion: Damped Least Squares (Levenberg–Marquardt) inversion (DLS)**</ins>

I use DLS algorithm from [Kode Praktikum GP2103 Metode Komputasi versi Python](https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python) tutorial: [Modul 6 - Metode Komputasi 2018 - GP UP.pdf, page 34](https://osf.io/36yh8/) and [pm6f.py](https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python/blob/master/pm6f.py) code. This result was showed using [sp_dls_inversion.py](https://github.com/ezygeo-ai/mlgi/blob/master/python/sp_dls_inversion.py) below.

```{figure} /figures/chap3/results/sp_dls_inv_result.png
---
name: sp_dls_inv_result
---
```

**Initial Model** x0: 20 | alpha: 100 (deg) | h: 40 | K: 94500

**Real Model** x0: 77.070000 | alpha: 5.399525 (rad) | h: 41.810000 | K: 94686.000000

**Inversion Model** x0: 76.243426 | alpha: 5.415794 (rad) | h: 42.776603 | K: 99102.106072

**Error**: 0.029529 %

with research paper reference [W. Srigutomo, et al, 2016](http://ijphysics.com/index.php/ijp/article/view/138) that is modified [sp_dls_inversion_scratch.py](https://github.com/ezygeo-ai/mlgi/blob/master/sources/python/sp_dls_inversion.py) below. Jacobian matrix was calculated using [derrivatives_in_python.py](https://github.com/ezygeo-ai/mlgi/blob/master/python/derrivatives_in_python.py).