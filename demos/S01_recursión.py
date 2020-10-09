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
# # Recursión

# %%
import math as m


# %%
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


# %%
fact(20)

# %%
m.factorial(20)

# %%
fact(-5)

# %%
m.factorial(-5)


# %% [markdown]
# Para poder manejar arrojar un error cuando la función se utiliza fuera de su dominio necesitamos utilizar la palabra clave `raise` junto con una **excepción** de la forma:

# %%
def fact(n):
    if n < 0:
        raise ValueError("fact no está definida para argumentos negativos")
    elif n == 0:
        return 1
    else:
        return n*fact(n-1)


# %%
fact(-5)

# %%
