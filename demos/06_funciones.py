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
# # Definiciones de funciones
#
# Como dijimos, para definir funciones usamos las siguentes sintaxis:

# %%
def cubo(x):
    return x*x*x


# %%
cubo(2)


# %%
def cuadrática(x,a,b,c):
    p = a
    p += b * x
    p += c * x**2
    return p


# %%
cuadrática(1,1,1,1)


# %%
def otra_cuadrática(x,a=0,b=0,c=0):
    p = a
    p += b * x
    p += c * x**2
    return p


# %%
otra_cuadrática(2)

# %%
otra_cuadrática(2,1)

# %%
otra_cuadrática(2,1,1)

# %%
otra_cuadrática(2,1,1,1)

# %%
otra_cuadrática(2,a=1,b=1,c=2)

# %%
otra_cuadrática(2,a=1,b=1,d=2)


# %%
def tres_potencias(x):
    x2 = x**2
    x3 = x**3
    x4 = x**4
    return x2,x3,x4


# %%
a,b,c = tres_potencias(2)

# %%
print(a,b,c)


# %%
def colateral(a,b):
    print(f'a es {a} y b es {b}')
    c = a + b


# %%
colateral(1,2)

# %%
c = colateral(1,2)

# %%
c

# %%
type(c)

# %%
type(f)


# %%
def colateral2(a,b):
    print(f'a es {a} y b es {b}')
    c = a + b
    return c


# %%
c = colateral2(1,2)

# %%
c


# %%
def nocambia(a):
    a += 1
    return a


# %%
a = 2

# %%
nocambia(a)

# %%
a
