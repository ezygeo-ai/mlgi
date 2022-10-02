# Gaya Berat (Gravity)
> Diperbarui: Selasa, 18 Oktober 2016

```{contents}
:local:
```

Program awalnya dibuat dalam bahasa Octave {cite}`Heriyanto2017grav`, kemudian dituliskan juga dalam Python dan C++.

````{tab-set-code}
```{code-block} python
rho = 1
R = 10
z = 20
x0 = 10
cGrav = 6.674e-11; % Konstanta Gravitasi (m^3 kg^-1 s^-2)
si2mg = 1e5;
# 1 SI(ms^-2) = 1e5 mGal
x = range(-100, 100, 10)
k = (4/3) * pi * cGrav * rho * (R^3)
for i in range(len(x)):
    dg(i) = k*(z/((x(i)-x0)^2 + z^2)^(1.5)); # m s^2
dg = dg * si2mg
```

```{code-block} octave
clc; clear all; close all;
rho = 1;
R = 10;
z = 20;
x0 = 10;
cGrav = 6.674e-11; % Konstanta Gravitasi (m^3 kg^-1 s^-2)
si2mg = 1e5;
% 1 SI(ms^-2) = 1e5 mGal
x = -100:10:100;
k = (4/3) * pi * cGrav * rho * (R^3);
for i = 1:length(x)
    dg(i) = k*(z/((x(i)-x0)^2 + z^2)^(1.5)); % m s^2
end
dg = dg * si2mg;
```

```{code-block} c++
#include <iostream>

int main()
{
    int rho, R, z, x0;
    return 0;
}
```
````