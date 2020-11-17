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
# ## Ejercicio
#
# Utilize la rutina `minimize` del paquete `numpy.optimize` para encontrar el mínimo global de la [función de Rosenbrock](http://mathworld.wolfram.com/RosenbrockFunction.html).
#
# Compare los resultados obtenidos utilizando los algoritmos Nelder-Mead, CG y BFGS. En los últimos dos casos compare el resultado utilizando gradientes numéricos (la entrada por defecto de la subrutina) o explícitos, para lo cual deberá clalcular el gradiende de la función respecto de los parámetros.

# %%
