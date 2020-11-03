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
# ## Nota
#
# En todos los casos que se pide definir una función se debe evaluara para algunos argumentos (por lo menos tres en cada caso) que comprueben que funciona como es debido.

# %% [markdown]
# ## Ejercicio 1
#
# Definir una función que calcule las raíces de un polinomio arbitrario de grado 2.

# %%
import cmath as cm
import math as m


# %%
def raices(a,b,c):
    return (-b+cm.sqrt(b**2-4*a*c))/(2*a),(-b-cm.sqrt(b**2-4*a*c))/(2*a)


# %%
raices(1,1,1)

# %%
raices(1,-1,-1)

# %%
raices(3,4,5)


# %% [markdown]
# ## Ejercicio 2
#
# Rehacer el ejercicio 1 de la tarea 02b utilizando las constantes físicas definidas en el módulo [ScyPy](https://docs.scipy.org/doc/scipy/reference/constants.html).

# %%

# %% [markdown]
# ## Ejercicio 3
#
# Verificar para tres triplas de $\alpha$, $\beta$ y $x$ que si
#
# $$f(x) = \frac{(\cos\alpha)x - \sin\alpha}{(\sin\alpha)x + \cos\alpha}$$
#
# y
#
# $$g(x) = \frac{(\cos\beta)x - \sin\beta}{(\sin\beta)x + \cos\beta}$$
#
# entonces se cumple que
#
# $$f\big(g(x)\big) = g\big(f(x)\big)$$

# %%
def f(x,alpha):
    return (m.cos(alpha)*x-m.sin(alpha))/(m.sin(alpha)*x+m.cos(alpha))


# %%
f(f(2,0.5),1.5) - f(f(2,1.5),0.5)

# %%
f(f(3,4.5),2.5) - f(f(3,2.5),4.5)

# %%
f(f(3.14,1),2) - f(f(3.14,2),1)


# %% [markdown]
# ## Ejercicio 4
#
# Verificar para tres casos que si $a_1$, $a_2$ y $z$ son constantes complejas entonces es cierto que
#
# $\cot(z - a_1)\cot(z - a_2) = -1 + \cot(a_1 - a_2)\cot(z - a_1) + \cot(a_2 - a_1)\cot(z - a_2)$

# %%
def ff(z,a1,a2):
    return (1/cm.tan(z-a1))*(1/cm.tan(z-a2)) + 1 - (1/cm.tan(a1-a2))*(1/cm.tan(z-a1)) - (1/cm.tan(a2-a1))*(1/cm.tan(z-a2)) 


# %%
ff(1j,0.1+1j,0.21j)

# %%
ff(3j,0.1+4j,0.2555j)

# %%
ff(3+1j,2+2j,1+3j)

# %%
