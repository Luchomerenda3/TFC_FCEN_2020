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
# # Bucles

# %%
import math as m
import cmath as cm

# %%
i = 2
while True:
    i *=2

# %%
i

# %%
i = 0
while (i <= 10):
    print(f"i vale {i:2d}")
    i += 1

# %%
i = 0
while (i <= 10):
    print(f"i vale {i:2d}")
    i += 1
else:
    print("final del loop")

# %%
i = 0
while (i <= 20):
    print(f"Al principio i vale {i:2d}")
    if (i == 8):
        print("Pasamos por ocho y saltamos")
        i += 1
        continue
    elif (i == 12):
        break
    i += 1
    print(f"Al final i vale {i:2d}")
else:
    print("final del loop")

# %%
alpha = 0
delta = 2 * m.pi / 10
while (alpha <= 2*m.pi):
    z = cm.exp(1j*alpha)
    print(f"alpha es {alpha:20.16g} {z.real:24.16g} {z.imag:24.16g}")
    alpha += delta

# %%
x = 0
delta = 0.1
while (x <= 2):
    y = x**2
    print(f"x es {x:20.16g} {y:24.16g}")
    x += delta

# %%
alpha = 0
delta = 2 * m.pi / 20
while (abs(alpha - 2*m.pi - delta) >= 1e-15):
    z = cm.exp(1j*alpha)
    print(f"alpha es {alpha:20.16g} {z.real:24.16g} {z.imag:24.16g} {i}")
    alpha += delta

# %%
xmin = -3.0
xmax =  7.0
nx = 10
x = xmin
delta = (xmax - xmin) / nx

while (x < xmax + delta/2):
    fdex = 1-3*x+x**2
    print(f"{x:5.3f} {fdex:5.3f} {(x - xmax - delta):25.19f}")
    x += delta

# %%
xmin = -3.0
xmax =  7.0
nx = 100

i = 0

while (i <= nx):
    x = xmin + (xmax - xmin) * i / nx
    fdex = 1-3*x+x**2
    print(f"{x:5.3f} {fdex:5.3f} {(x - xmax - delta):25.19f}")
    i += 1
    

# %%
xmin = -3.0
xmax =  7.0
nx = 10000

i = 0
fmin = m.inf
fmax = -m.inf

while (i <= nx):
    x = xmin + (xmax - xmin) * i / nx
    fdex = (x-1)*(x+1)*(x-3)
    if fdex < fmin: fmin = fdex
    if fdex > fmax: fmax = fdex
    i += 1
else:
    print(f"el minimo es {fmin:20.6f}, el máximo es {fmax:20.6f}")

# %%
