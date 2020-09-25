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
# # Módulos
#
# Empecemos con un ejemplo, vamos a importar el módulo `decimal`que es parte de la biblioteca estándard de Python:

# %%
import decimal

# %% [markdown]
# Este módulo implementa clases y funciones para trabajar con números decimales a una precisión arbitraria. Como vimos antes, hay números decimales que no tienen una representación exacta en binario. Esto tiene como consecuencia el resultado "extraño" que obtuvimos anteriormente:

# %%
0.1 + 0.2

# %% [markdown]
# Sin embargo, 0.1 y 0.2 son representaciones exactas en base 10 de 1/10 y 1/5. Utilizando módulo `decimal` tenemos que:

# %%
# notar las cadenas literales como parámetro
decimal.Decimal('0.10') + decimal.Decimal('0.20')

# %% [markdown]
# Notemos que incluso se preservan las cifras significativas. Si bien el pequeño error que obtenemos en la suma de punto flotante no parece demasiado importante hay situaciones en las que la suma de 0.10 y 0.20 debe ser exactamente 0.20, por ejemplo si estamos hablando de dinero...

# %% [markdown]
# Podemos facilitar nuestra vida importando el módulo de la forma:

# %%
import decimal as d

# %% [markdown]
# con lo cual acortamos un poco las expresiones usando el "alias" `d`:

# %%
d.Decimal('0.10') + d.Decimal('0.20')

# %% [markdown]
# Podríamos acortar aún más la cosa importando sobre el "espacio de nombres" de nuestro programa, pero corremos el riesgo de "pisar" nombre ya existentes, por ejemplo, supongamos que tenemos definido el nombre siguiente:

# %%
MAX_PREC = """MAX_PREC es una variable valiosa
que contiene un precioso secreto que
no recordaré jamás si llega a ser modificada"""

# %%
print(MAX_PREC)

# %%
# pero
print(d.MAX_PREC)

# %%
# entonces si importamos
from decimal import *

# %%
print(MAX_PREC) 

# %% [markdown]
# 😱😱😱😱😱😱😱😱😱
#
# nuestra valiosa variable se convirtió en entropía del universo.
#
# Si bien en general no es aconsejable guardar preciosos secretos en variables de programas en Python el problema más grave se produce en general al usar varios módulos a la vez. Hay módulos que contienen muchos, muchos nombres y conviene a cada uno tenerlo bien encerrado.
#
# En síntesis, no usar `from módulo import *`

# %% [markdown]
# # NumPy
#
# Dada la gran frustración que nos ha generado no poder usar funciones trascendentes hasta ahora estamos a punto de sentir una gran liberación catártica. Empecemos con lo más simple de NumPy:

# %%
import numpy as np

# %%
print(np.e) # SEEEEEEEEEEEEEEEEE

# %% [markdown]
# NumPy implementa todo lo que podemos necesitar y quizás más (y también está SciPy), la lista completa está en la [documentación](https://numpy.org/doc/stable/reference/routines.math.html) pero podemos abrir el apetito con algunos ejemplos simples:

# %%
np.angle(1+1j)/np.pi

# %%
np.e**(1j * np.pi) + 1.0

# %%
np.sqrt(2.0)**2

# %%
theta = np.pi/17

# %%
np.sin(theta)**2 + np.cos(theta)**2

# %%
np.sin(2*theta) - 2*np.sin(theta)*np.cos(theta)

# %%
np.cos(3*theta) - 4*np.cos(theta)**3 + 3*np.cos(theta)

# %%
alpha = 0.1
beta = 0.2

# %%
np.tan((alpha+beta)/2) - (np.sin(alpha)+np.sin(beta))/(np.cos(alpha)+np.cos(beta))

# %% [markdown]
# Si bien los módulos `math` y `cmath` de la biblioteca estándar contienen las mismas rutinas para reales y complejos relativamente, vamos a preferir usar desde temprano las rutinas implementadas en NumPy ya que nos permitirán trabajar con otros argumentos, por ejemplo vectoriales o matriciales, más adelante.

# %% [markdown]
# # SciPy
#
# Si con las funciones trascendentales no nos alcanza podemos agregar el módulo de funciones especiales de SciPy ([documentación](https://docs.scipy.org/doc/scipy/reference/special.html))

# %%
import scipy.special as sp

# %%
sp.gamma(6) - sp.factorial(5)

# %%
z = 2+3j

# %%
sp.gamma(1-z)*sp.gamma(z) - np.pi/np.sin(np.pi*z) 

# %%
sp.gamma(1/2) - np.sqrt(np.pi)

# %%
(-3.843888588848283e-20+0j).real

# %%
(-3.843888588848283e-20+0j).imag

# %%
