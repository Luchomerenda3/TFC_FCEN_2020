# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Ejercicio 1
#
# Graficar las siguientes funciones en los intervalos dados:
#
# 1. $f(x) = \cos(x^2)$ en $[-3\pi,3\pi]$
# 1. $f(x) = x\sin(1/x)$ en $[-1,1]$ (se necesita un poco de ingeniería para lidiar con las infinitas discontinuidades)
# 1. $J_n(x)$ con $n=1,2,3,\ldots,5$ en el intervalo $[0,10]$ donde $J_n$ es la función de Bessel del primer tipo.
#

# %%
import matplotlib.pyplot as plt
import math as m
import cmath as cm
from scipy.special import jv


# %%
def evalua(f,a,b,n):
    xs = []
    ys = []
    for i in range(n):
        xs += [a + i* (b - a) / n]
        ys += [f(xs[-1])]
    return xs, ys


# %%
xs,ys = evalua(lambda x : m.cos(x**2),-3*m.pi,3*m.pi,1000)
plt.plot(xs,ys)

# %%
xs,ys = evalua(lambda x : x * m.cos(1/x),-1,1,1001)
plt.plot(xs,ys)

# %%
for i in range(1,6):
    xs,ys = evalua(lambda x : jv(i,x),0,10,1000)
    plt.plot(xs,ys)


# %% [markdown]
# ## Ejercicio 2
#
# Dada la función compleja de variable real:
#
# $\mu(t) = e^{it} + \frac{1}{2}e^{6it} + \frac{i}{3}e^{-14it}$,
#
# graficar la curva paramétrica dada por $(\Re \mu(t),\Im \mu(t))$ con $t\in[0,2\pi]$.
#
# Referencia: Creating symmetry : the artful mathematics of wallpaper patterns, Farris, Frank A, Princeton University Press, 2015

# %%
def mu(t):
    return cm.exp(1j*t) + cm.exp(6j*t)/2 + 1j*cm.exp(-14j*t)/3


# %%
def evalua_parametrica(f,a,b,n):
    xs = []
    ys = []
    for i in range(n):
        t = a + i* (b - a) / n
        xs += [f(t).real]
        ys += [f(t).imag]
    return xs, ys


# %%
xs,ys = evalua_parametrica(mu,0,2*m.pi,500)
plt.plot(xs,ys)



# %%
