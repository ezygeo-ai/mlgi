[![Online](https://img.shields.io/badge/read-online-green.svg)](https://mheriyanto.dev/mlgi)
![Jupyter Book Badge](https://jupyterbook.org/badge.svg)
![GitHub contributors](https://img.shields.io/github/contributors/ezygeo-ai/mlgi)
![GitHub last update](https://img.shields.io/github/last-commit/ezygeo-ai/mlgi)

# 🧑‍💻 ***Hands-On* Pembelajaran Mesin untuk Inversi Geofisika**

Halaman muka dari kumpulan artikel terkait implementasi pembelajaran mesin (*machine learning*) untuk inversi geofisika.

*Hands-on* disini memakai bahasa pemograman [**Python**](https://en.wikipedia.org/wiki/Python_(programming_language)), [**MATLAB (Octave)**](https://en.wikipedia.org/wiki/GNU_Octave) dan [**C++**](https://en.wikipedia.org/wiki/C%2B%2B). 

<p align="center">
  <code><a href="https://www.python.org" target="_blank"><img title="python" height="40" width="40" src="https://www.svgrepo.com/show/374016/python.svg"></a></code>
  <code><a href="https://octave.org" target="_blank"><img title="octave" height="40" width="40" src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Gnu-octave-logo.svg"></a></code> 
  <code><a href="https://www.mathworks.com/products/matlab.html" target="_blank"><img title="matlab" height="40" width="40" src="https://www.svgrepo.com/show/373830/matlab.svg"></a></code>  
  <code><a href="https://en.cppreference.com/w/" target="_blank"><img title="c++" height="40" width="40" src="https://www.svgrepo.com/show/303480/c-logo.svg"></a></code>
</p>

## **Daftar isi**

```{tableofcontents}
```

## **Instalasi**

:::{note}
Program dalam bahasa MATLAB (**berbayar**) bisa dijalankan dengan compiler Octave (**gratis**), sehingga dalam buku ini *keyword* MATLAB akan dituliskan sebagai **Octave**.
:::


**Instalasi *environment* (Linux Ubuntu) dan menjalankan program**

````{tab-set-code}
```{code} python
python3 fwd_gravity.py
```

```{code} octave
sudo apt-get install gcc g++ gfortran make 
sudo apt-get install libopenblas-dev liblapack-dev libpcre3-dev libarpack2-dev libcurl4-gnutls-dev epstool libfftw3-dev fig2dev libfltk1.3-dev libfontconfig1-dev libfreetype6-dev libgl2ps-dev libglpk-dev libreadline-dev gnuplot-x11 libgraphicsmagick++1-dev libhdf5-dev openjdk-11-jdk libsndfile1-dev 
sudo apt-get install llvm-dev texinfo libgl1-mesa-dev pstoedit portaudio19-dev libqhull-dev libqrupdate-dev libsuitesparse-dev texlive-latex-extra libxft-dev zlib1g-dev autoconf automake bison flex gperf gzip icoutils librsvg2-bin libtool perl rsync tar 
sudo apt-get install qtbase5-dev qttools5-dev qttools5-dev-tools libqscintilla2-qt5-dev libsundials-dev rapidjson-dev
octave fwd_gravity.m
```

```{code} c++
g++ fwd_gravity.cpp -o fwd_gravity
./fwd_gravity
```
````