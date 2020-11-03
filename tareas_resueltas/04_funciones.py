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
# # Funciones

# %% [markdown]
# ## Ejercicio 1
#
# Definir (y probar con tres casos) una función que calcule el polinomio
#
# $$p(x) = 1 + x + x^2$$

# %%
def p(x):
    return(1+x+x)


# %%
p(0)

# %%
p(1)

# %%
p(2)


# %% [markdown]
# ## Ejercicio 2
#
# Escribir una función que calcule la parte real e imaginaria de un número complejo.

# %%
def real_e_imag(z):
    return z.real,z.imag


# %%
real_e_imag(1j)

# %%
real_e_imag(1.)

# %%
real_e_imag(1.+1j)


# %% [markdown]
# ## Ejercicio 3
#
# Definir (y probar con tres casos) una función que calcule la duración en segundos de un intervalo de tiempo indicado en horas, minutos y segundos.

# %%
def s(h,m,s):
    return h*3600+m*60+s


# %%
s(1,1,1)

# %%
s(2,30,0)

# %%
s(2,46,40)


# %% [markdown]
# ## Ejercicio 4
#
# Escribir una función que agregue la cadena "fin de la cadena" precedida de un espacio a cualquier cadena de entrada.

# %%
def agrega(s):
    return s + " fin de la cadena"


# %%
agrega('hola')

# %%
agrega('hola mundo')

# %%
agrega('hola este mundo')

# %%
agrega('hola')


# %% [markdown]
# ## Ejercicio 5
#
# Definir (y probar con tres casos) una función que calcule la duración en horas, minutos y segundos de un intervalo de tiempo indicado en segundos.

# %%
def hms(s):
    return s//3600,(s%3600)//60,(s%3600)%60


# %%
hms(3661)


# %%
hms(9000)

# %%
hms(10000)


# %% [markdown]
# ## Ejercicio 6
#
# Definir (y probar con tres casos) una función que evalúe una función racional de la forma
#
# $$f(x) = \frac{a_1 + b_1 x + c_1 x^2}{a_2 + b_2 x + c_2 x^2}$$

# %%
def funcion_racional(x,a1,b1,c1,a2,b2,c2):
    return (a1+b1*x+c1*x**2)/(a2+b2*x+c2*x**2)


# %%
funcion_racional(0,1,0,0,1,0,0)

# %%
funcion_racional(1,1,1,1,1,1,1)

# %%
funcion_racional(3.1415,1,1,1,2,2,2)


# %% [markdown]
# ## Ejercicio 7
#
# Definir (y probar con tres casos) una función que evalúe:
# \begin{equation}
#   H'(x)=\left\{
#   \begin{array}{@{}ll@{}}
#     1, & \text{si}\ x > 0 \\
#     0, & \text{si}\ x < 0
#   \end{array}\right.
# \end{equation} 
#

# %%
def H(x):
    return 1/2 + abs(x)/x/2


# %%
H(-5)

# %%
H(5)

# %%
H(0.000000000000000001)

# %%
