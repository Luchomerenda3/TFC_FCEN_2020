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
# # Tarea 02b
#
# Utilizamos Python como calculadora. Para hacer la cosa más interesante los ejercicios de este *Notebook* deben ser resueltos utilizando **únicamente** los operadores aritméticos `+ - / * ** %` y `//` operando entre literales y/o las funciones de la librería estándard (.

# %% [markdown]
# ## Ejercicio 1
#
# Calcular el módulo de la aceleración que sufre el electrón en el estado fundamental del átomo de hidrógeno. Expresar el resultado en unidades SI.
#
# Vuelta de tuerca: Estimar el error en la aceleración calculada utilizando un modelo de propagación lineal de errores y asumiendo que los errores en las cantidades necesarias para el cálculo no están correlacionados.
#
# Utilizar los valores de las constantes físicas de [aquí](https://physics.nist.gov/cuu/Constants/index.html), hay info útil [aquí](https://arxiv.org/pdf/1610.08716.pdf) y [aquí](https://xkcd.com/2110/).

# %% [markdown]
# Asumiendo un modelos clásico en el que el electrón orbita a una distancia $a_0$ del protón y que está sometido a una fuerza radial producida por la interacción electrostática entre ambos, tenemos que el módulo de la acelarción que sufre es:
#
# $$a= \frac{1}{4\pi\epsilon_0}\frac{e^2}{a_0^2m_e}$$
#
# Los valores CODATA para las constantes son:
#
# `m_e = 9.109 383 7015(28) x 10-31 kg`
#
# `a_0 = 5.291 772 109 03(80) x 10-11 m`
#
# `e = 1.602 176 634  x 10-19 C` (valor exacto, desde la redefinición del SI en 2018)
#
# `epsilon_0 =8.854 187 8128(13) x 10-12 F m-1`

# %%
(1/4/3.141592653589793/8.854_187_8128e-12)* \
(1.602_176_634e-19**2/5.291_772_109_03e-11**2/9.109_383_7015e-31)

# %% [markdown]
# Usando las derivadas parciales
#
# $$\frac{\partial a}{\partial\epsilon_0} = -\frac{1}{4\pi\epsilon_0^2}\frac{e^2}{a_0^2m_e}$$
#
# $$\frac{\partial a}{\partial a_0} = -\frac{1}{2\pi\epsilon_0^2}\frac{e^2}{a_0^3m_e}$$
#
# $$\frac{\partial a}{\partial m_e} = -\frac{1}{2\pi\epsilon_0^2}\frac{e^2}{a_0^2m_e^2}$$
#
# Usamos la siguiente espresión para estimar el error en el resultado:
#
# $$\sqrt{\sum_i \left( \Delta p_i  \frac{\partial a}{\partial p_i} \right)^2}$$
#
# donde $\Delta p_i$ es el error en cada parámetro

# %%
( \
(0.0000000013e-12*abs((1/4/3.141592653589793/8.854_187_8128e-12**2)* \
(1.602_176_634e-19**2/5.291_772_109_03e-11**2/9.109_383_7015e-31)))**2 \
+ \
(0.000_000_000_80e-11*abs((1/2/3.141592653589793/8.854_187_8128e-12)* \
(1.602_176_634e-19**2/5.291_772_109_03e-11**3/9.109_383_7015e-31)))**2 \
+ \
(0.000_000_0028e-31*abs((1/4/3.141592653589793/8.854_187_8128e-12)* \
(1.602_176_634e-19**2/5.291_772_109_03e-11**2/9.109_383_7015e-31**2)))**2
)**(1/2)

# %% [markdown]
# ## Ejercicio 2
#
# Calcular una aproximación para el Número de Euler ($e$). Hay una buena lista de formas para hacerlo en [Wikipedia](https://en.wikipedia.org/wiki/E_(mathematical_constant)).

# %% [markdown]
# En [MathWorld](https://mathworld.wolfram.com/eApproximations.html) hay una serie de expresiones para aproximar $e$, entre ellas la siguiente:
#
# $$e\approx\left(1097 -\frac{55^5+311^3-11^3}{68^5} \right)^{1/7}$$
#
# Que comparando con:
#
# $$2.71828182845904523536028747135266249775724709369995957
# 49669676277240766303535475945713821785251664274$$
#
# es correcta a 15 decimales:

# %%
(1097-(55**5+311**3-11**3)/68**5)**(1/7)

# %%
ee = 2.718

# %%
(ee**(1j/2)+ee**(-1j/2))/2

# %% [markdown]
# ## Ejercicio 3
#
# Utilizando el resultado anterior calcular valores aproximados para $\cos(1/2)$ y $\sin(1/3)$. Estimar los errores para cada valor.

# %% [markdown]
# Teniendo en cuenta que:
#
# $$\cos x = \frac{e^{ix}+e^{-ix}}{2}$$
#
# y que
#
# $$\sin x = \frac{e^{ix}-e^{-ix}}{2i}$$
#
# aproximamos:

# %%
# cos(1/2)

((((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(1j/2)
 +((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(-1j/2))/2)

# %%
# sin(1/3)

((((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(1j/3)
 -((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(-1j/3))/2j)

# %% [markdown]
# En base a una expansión de primer order alrededor del valor $x_0$, una estimación en el error de cada uno de los resultados anteriores es:
#
# $$h\left| \frac{\partial \cos x}{\partial e} \right| = \frac{1}{2}h \left|
# ixe^{ix-1}-ixe^{-ix-1}\right|$$
#
# $$h\left|\frac{\partial \sin x}{\partial e} \right| = \frac{1}{2}h \left|
# ixe^{ix-1}+ixe^{-ix-1}\right|$$
#
# donde , en nuestro caso $h\approx 10^{-15}$

# %%
1e-15*abs((((1j/2)*((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(1j/2-1)
 -(1j/2)*((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(-1j/2-1))/2))

# %%
1e-15*abs((((1j/2)*((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(1j/2-1)
 +(1j/2)*((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(-1j/2-1))/2j))

# %% [markdown]
# ## Ejercicio 4
#
# Y si queremos $\tan(\sqrt{2}/2)$?

# %% [markdown]
# Teniendo en cuenta que
#
# $$\tan x = \frac{\sin x}{\cos x}$$

# %%
((((1097-(55**5+311**3-11**3)/68**5)**(1/7))**((2**0.5)*1j/2)
 -((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(-(2**0.5)*1j/2))/2j) /(
    (((1097-(55**5+311**3-11**3)/68**5)**(1/7))**((2**0.5)*1j/2)
 +((1097-(55**5+311**3-11**3)/68**5)**(1/7))**(-(2**0.5)*1j/2))/2)

# %% [markdown]
# Subir los ejercicios completos en formato `ipynb` a Google Classroom. Describiendo en celdas de *Markdown* cada paso de los cálculos, sin demasiada exigencia, sólo para que el que lee pueda entender de qué se trata lo que el código hace.
