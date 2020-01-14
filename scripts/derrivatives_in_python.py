# Code was created by M. Heriyanto, 2020/01/13
# https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion/edit/master/fwd_sp.py

import sympy as sym
# https://scipy-lectures.org/packages/sympy.html

# === example
x = sym.Symbol('x')
y = sym.Symbol('y')

print(sym.diff(3*x**2 + 3*y, x))
print(sym.diff(3*x**2 + 3*y, y))


def func(vx, vy):
    return 3*vx**2 + 3*vy


print(sym.diff(func(x, y), x))
print(sym.diff(func(x, y), y))

# === SP case
x = sym.Symbol('x')
x0 = sym.Symbol('x0')
alpa = sym.Symbol('alpa')
h = sym.Symbol('h')
K = sym.Symbol('K')


# forward function
def func_SP(vx, vx0, va, vh, vk):
    return vk * (((vx-vx0)*sym.cos(va)-vh*sym.sin(va))/((vx-vx0)**2 + vh**2)**3/2)


# x0
print(sym.diff(func_SP(x, x0, alpa, h, K), x0))

# alpa
print(sym.diff(func_SP(x, x0, alpa, h, K), alpa))

# h
print(sym.diff(func_SP(x, x0, alpa, h, K), h))

# K
print(sym.diff(func_SP(x, x0, alpa, h, K), K))
