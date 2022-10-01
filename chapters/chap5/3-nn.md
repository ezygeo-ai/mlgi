# Neural Network (NN)

```{contents}
:local:
```

<ins>**Machine Learning: Multilayer Perceptron Neural Networks (MLP)**</ins>

Self-Potential Dataset that was generated with 5,000 different spherical models (using [sp_make_dataset.py](https://github.com/ezygeo-ai/mlgi/blob/master/scripts/sp_make_dataset.py)) with differing electrical dipole moment, polarization angle, origin and depth to the centre of sphere [here](https://github.com/ezygeo-ai/mlgi/blob/master/data/SP_Dataset.pickle) and seen below (using [sp_show_dataset.py](https://github.com/ezygeo-ai/mlgi/blob/master/scripts/sp_show_dataset.py)). This dataset contains training (**80%**) dan validation (**20%**) dataset.

```{figure} /figures/chap5/results/training_dataset.png
---
name: training_dataset
---
```
```{figure} /figures/chap5/results/validation_dataset.png
---
name: validation_dataset
---
```

This MLPNN used two (2) hidden layers, input layer used 101 point of data (neurons), first layer used 2 neurons and second layer used five (5) neurons. Then, learning rate = 0.1, activation function = hyperbolic tangent sigmoid function. The final MSE = 0.00306092 from 150 epochs.

```{figure} /figures/chap5/tutorials/mlp.png
---
name: mlp
---
```