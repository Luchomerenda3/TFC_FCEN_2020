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
# # Operaciones Lógicas
#
# Las operaciones lógicas se llevan a cabo entre variables (o literales) Booleanos que pueden tomar los valores `True`o `False`:

# %%
A = True

# %%
B = False

# %%
A and B

# %%
A or B

# %%
not A


# %% [markdown]
# Podemos construir otras operaciones lógicas *componiendo* las ya existentes, por ejemplo, podemos hacer una función que devuelva el resultado de la operación XOR. La operación XOR tiene la siguiente *tabla de verdad*:
#
# | Operando A | Operando B | Resultado |
# | --- | --- | --- |
# | `False` | `False` | `False`|
# | `False` | `True` | `True`|
# | `True` | `False` | `True`|
# | `True` | `True` | `False`|
#
# Y puede construirse componiendo las operaciones de negación `not` y `or` de la siguiente forma:

# %%
def xor(A,B):
    return ((not A) and B) or (A and (not B)) 


# %% [markdown]
# veamos si funciona como debe:

# %%
xor(False, False)

# %%
xor(False, True)

# %%
xor(True, False)

# %%
xor(True, True)
