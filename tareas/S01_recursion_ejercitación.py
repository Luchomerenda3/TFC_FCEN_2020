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

# %% [markdown]
# ## Ejercicio 1:
#
# Definir (y probar bla,bla,bla...) una función recursiva que calcule la enésima potencia positiva de $x$:
#
# $$f(x,n) = x^n$$
#

# %%

# %% [markdown]
# ## Ejercicio 2:
#
# Definir (y probar bla,bla,bla...) una función que calcule el miembro $n$ de la secuencia de Fibonacci $F_n$ la cual se define de la forma
# $$F_0=0$$
# $$F_1=1$$
# para $n=0$ y $n=1$ y
# $$F_n=F_{n-1} + F_{n-2}$$
# para $n>1$

# %%

# %% [markdown]
# ## Ejercicio 3
#
# Los *Polinomios de Legendre* pueden ser definidos en base a la siguiente *relación de recurrencia*:
#
# $$P_0(x) = 1$$
# $$P_1(x) = x$$
# $$(j+1) P(j+1) = (2j+1)xP_j(x)-jP_{j-1}(x)$$
#
# Definir y probar una función que evalúe $P_n(x)$.

# %%

# %% [markdown]
# De ahora en adelante le agregamos un (*) a los ejercicios (más) opcionales:
#
# ## Ejercicio 4 (*)
#
# Inplementar y probar una función recursiva que calcule el coeficiente binomial $N\choose k$.

# %% [markdown]
# ## Ejercicio 5 (*)
#
# Inplementar y probar una función recursiva que calcule el máximo común divisor de dos números enteros.

# %% [markdown]
# ## Ejercicio 6 (**)
#
# Los polinomios de Lejendre son *ortonormales* en el intervalo $[-1,1]$, es decir:
#
# $$ \frac{2n+1}{2}\int_{-1}^{1} P_m(x)P_n(x)dx= \delta_{nm} $$
#
# Utilizando el paquete SciPy y la función definida en el ejercicio 2 mostrar que es así construyendo una función que calcule el lado izquierdo de la ecuación para un par arbitrario $n,m$.

# %%
