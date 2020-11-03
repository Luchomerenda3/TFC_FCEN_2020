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

# %% [markdown] colab_type="text" id="Nyi9eCPxLUJd"
# # Fórmula Integral de Cauchy
#
# ---
#
# A partir del *Teorema de Cauchy-Goursat* es posible demostrar proposiciones como la siguente:
#
# > Sea $f(z)$ una función analítica sobre $\mathcal{C}$, siendo $C$ un contorno cerrado simple, y en el interior de $\mathcal{C}$. Si se toma un punto interior $z_0$ de $\mathcal{C}$, se cumple que:
# >$$
# \oint_C \frac{f(z)}{z-z_0}dz =  2 \pi i f(z_0)
# $$
# > que corresponde a la **fórmula integral de Cauchy**.
#
# Extraído de [Wikipedia](https://es.wikipedia.org/wiki/Teorema_integral_de_Cauchy)
#
