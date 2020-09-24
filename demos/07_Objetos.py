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
# # Objetos
#
# Es posible utilizar python sin utilizar a fondo el paradigma de prgramación orientada a objetos (POO). Se puede utilizar Python de manera muy eficiente sin jamás diseñar una *Clase*. Pero es dificil evadir conocer *algo* de la implementación de POO en Python sobre todo si usamos bibliotecas como NumPy o matplotlib.
#
# Como dijimos, *todo* en Python es un objeto, y como tal tiene *propiedades* y *metodos*. Para ejemplificar a vuelo de pájaro algunos de los conceptos vamos a usar el tipo `complex`.
#
# Un objeto nuevo que pertenece a una determinada *clase* se crea (generalmente) utilizando una función llamada *constructor* que devuelve una *instancia*. El constructor de la clase `complex` es la función del mismo nombre:

# %%
z = complex(1.0,2.0)

# %%
type(z)

# %% [markdown]
# Podemos ver todos los métodos y propiedades del objeto usando la función `dir`. La lista es larga e incluye métodos de la forma `__método__`. Estos métodos son especiales e implementan, entre otras cosas las operaciones binarias como suma o producto en `__add__` y `__mul__`. Esos métodos o propiedades especiales no están diseñados para ser utilizados a través de sus respectivos operadores.

# %%
dir(z)

# %% [markdown]
# En la lista aparecen tres que no tienen guiones bajos, dos de ellos son propiedades:

# %%
z.real

# %%
z.imag

# %% [markdown]
# Y el otro es un método, en este caso muy simple, que no modifica al objeto:

# %%
z.conjugate()

# %% [markdown]
# Con esos elementos debería alcanzarnos para hacer uso de los elementos de POO que necesitaremos durante el resto del curso.
