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
#
# Usar **sólo** bucles `while`, las listas también son taboo por ahora.

# %% [markdown]
# ## Ejercicio 1
#
# Implementar una función que imprima todos los números primos menores a $n$.

# %%

# %% [markdown]
# ## Ejercicio 2
#
# Implementar una función que calcule la integral definida de una función arbitraria de una variable utilizando la regla del punto medio. Probar para los siguientes casos:
#
# $$ \int_0^1 x^2\ dx = 1/3 $$
#
# $$ \int_0^\pi \sin(x)\ dx = 2 $$
#
# Comparar con los resultado obtenido a partir de la función `quad` en el módulo `scipy.integrate`.

# %%

# %% [markdown]
# ## Ejercicio 3
#
# Implementar una función que calcule la raíz de una función arbitraria (dada su derivada) utilizando el método de Newton-Raphson. Probar para el caso 
#
# $$ f(x) = e^{-x} - \pi $$
#
# que tiene una única raiz en $-\ln\pi$.

# %%

# %% [markdown]
# # Serie S
#
# Los siguientes ejercicios son más complejos que los anteriores y su complejidad es creciente. Son un poco más opcionales que los anteriores

# %% [markdown]
# ## Ejercicio S1
#
# Comparar la velocidad de convergencia (determinando para que $k$ se logra una determinada tolerancia) de la serie de Gregory y Leibniz para $\pi$ 
#
# $$\pi=4\sum_{k=1}^{\infty}\frac{(-1)^(k+1)}{(2k-1)}$$
#
# con la siguiente serie:
#
# $$\frac{1}{\pi} = \frac{2\sqrt 2}{9801} \sum^\infty_{k=0} \frac{(4k)!(1103+26390k)}{(k!)^4 396^{4k}},$$
#
# una de las tantas sorprendentes fórmulas debidas al matemático indú Srinvasa Ramanujan.

# %%

# %% [markdown]
# ## Ejercicio S2
#
# Implementar una función que calcule el número de Bernouilli utilizando la fórmula implementada por Ada Lovelace en el primer algoritmo de computadora en la famosa [Nota G](https://projectlovelace.net/problems/ada-lovelaces-note-g/) incluída en el documento sobre la Máquina Analítica de Charles Babbage de 1843.

# %%

# %% [markdown]
# ## Ejercicio S3
#
# Extender la implementación de la regla del punto medio para calcular integrales dobles sobre regiones rectangulares en $\mathbb{R}^2$.

# %%

# %% [markdown]
# ## Ejercicio S4
#
# Extender la implementación de la regla del punto medio para calcular integrales sobre un camino circular cerrado de radio, sentido y centro determinado en $\mathbb{C}$. Probar para el caso
#
# $$
# \oint_C \frac{1}{z}dz =  2 \pi i 
# $$
#
# con un par de caminos circulares cambiando radio, origen y sentido.

# %%


