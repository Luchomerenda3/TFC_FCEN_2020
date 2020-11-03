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
# # Secuencias e iteración
#

# %% [markdown]
# ## Ejercicio 0
#
# Implementar una función que devuelva una secuencia con todos los números primos menores o iguales a $n$.

# %%

# %% [markdown]
# ## Ejercicio 1
#
# Utilizando la función `random` implementada en el módulo del mismo nombre:

# %%
from random import random

# %%
print(random())


# %% [markdown]
# implementar una función que genere un vector de dimensión $d$ (representado como una lista) de números aleatorios en el intervalo $[0,1)$.

# %%
def vector_aleatorio(d):
    return [random() for i in range(d)]


# %%
vector_aleatorio(5)


# %% [markdown]
# ## Ejercicio 2
#
# Implementar una función que calcule el producto escalar de dos vectores de dimensión $d$.

# %%
def producto_escalar(A,B):
    d = len(A)
    return sum([A[i]*B[i] for i in range(d)])


# %%
producto_escalar([1,1,1],[1,1,1])


# %% [markdown]
# ## Ejercicio 3
#
# Implementar una función que genere una matriz cuadrada (representada como una lista de listas) aleatoria de dimensión $d$.

# %%
def matriz_aleatoria(d):
    return [vector_aleatorio(d) for i in range(d)]


# %%
matriz_aleatoria(3)


# %% [markdown]
# ## Ejercicio 4
#
# Implementar una función que calcule el producto de dos matrices cuadradas de dimensión $d$

# %%
def producto_matricial(A,B):
    d = len(A)
    C = [[0 for i in range(d)] for j in range(d)]
    for i in range(d):
        for j in range(d):
            for k in range(d):
                C[i][j] += A[i][k]*B[k][j]
    return C


# %%
producto_matricial(matriz_aleatoria(3),matriz_aleatoria(3))

# %% [markdown]
# ## Ejercicio S1
#
# Implementar una función que devuelva una secuencia de tuplas con todos los pares de números primos gemelos menores o iguales a $n$.
#
#
#
#
#
#



# %%

# %% [markdown]
# ## Ejercicio S2
#
# Implementar una función que devuelva una secuencia de $m$ números pseudoaleatorios a partir de una *semilla* $X_0$ arbitraria usando el método de *congruencia lineal multiplicativa* basado en la relación de recurrencia:
#
# $$X_n = a X_{n-1} \mod m$$
#
# Utilizar alguno de los valores para $m$ y $a$ sugeridos por L'Ecuyer en:
#
# L'Ecuyer, Pierre (1999). "Tables of Linear Congruential Generators of Different Sizes and Good Lattice Structure". Mathematics of Computation. 68 (225): 249–260. ([PDF](https://www.ams.org/journals/mcom/1999-68-225/S0025-5718-99-00996-5/S0025-5718-99-00996-5.pdf))

# %%

# %% [markdown]
# ## Ejercicio S3
#
# Modificar la función del Ejercicio S2 para que devuelva números pseudoaleatorios de punto flotante en el intervalo $[0,1)$

# %%

# %% [markdown]
# ## Ejercicio S4
#
# Implementar una función que, dada una secuencia de objetos arbitrarios, genere todas las posible permutaciones y las devuelva en una lista de listas.

# %%

# %% [markdown]
# ## Ejercicio S5
#
# Implementar una función que calcule todos los números primos menores o iguales a $n$ utilizando el algoritmo conocido como *Criba de Eratóstenes*.

# %%
