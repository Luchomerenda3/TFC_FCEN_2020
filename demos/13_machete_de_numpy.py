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
# # Taller de Física Computacional
#
# Carlos Ruestes / Cristián Sánchez - Taller de Física Computacional - FCEN - UNCUYO
#
# # Machete de NumPy

# %% [markdown]
# Las listas en Python son contenedores abstractos que pueden contener estructuras de datos de cualquier tipo, números, cadenas, otras listas, etc.. Esa versatilidad tiene un problema. Las hace **lentas**. Si bien es posible utilizar listas para almacenar objetos tales como vectores, matrices o arreglos multidimensionales no son la estructura de datos ideal. Esto es porque los vectores o matrices que podemos necesitar en física computacional son, en general, de elementos que tienen todos el mismo tipo: números reales por ejemplo. El que los elementos sean del mismo tipo implica un acceso más rápido. Para lograr ese acceso rápido el objeto `ndarray` de Numpy almacena los datos numéricos en una sección de memoria única en direcciones contiguas. 
#
# La estructura `ndarray` y las rutinas para su manipulación implementadas en el paquete NumPy proporcionan la base para poder trabajar en Python con arreglos multidimensionales de forma eficiente. 

# %%
import numpy as np
import matplotlib.pyplot as plt
import math as m

# %% [markdown]
# ## Formas de crear arreglos

# %%
n = 3

# %%
a = np.empty((n,n)) # Arreglo vacío no inicializado, matrix de 3x3
a

# %%
b = np.zeros((n,n)) # Arreglo inicializado con ceros
b

# %%
c = np.zeros_like(b) # Arreglo inicializado a cero con la misma forma de b
c

# %%
d = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]]) # conversión de una lista a un ndarray
d

# %%
e = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]],dtype=complex) # establecemos el tipo de datos explícitamente
e

# %%
f = np.arange(0,10,0.1) # vector de números equiespaciados en 0.1 entre 0 y 10
f

# %%
g = np.linspace(0,2*np.pi,10) # vector de 10 elementos equiespaciados entre 0 y 2*pi
g

# %%
o = np.random.rand(3,3) # matriz 3x3 de números aleatorios
o

# %% [markdown]
# ## Formas de acceder y asignar los elementos de un arreglo

# %%
a = np.random.rand(3,3)

# %%
a

# %% [markdown]
# Acceso y asignación por índices

# %%
a[0,0]

# %%
a[2,1]

# %%
a[0,0] = 1.0

# %%
a[2,1] = 1.0

# %% [markdown]
# Acceso y asignación por *slices*

# %%
a[:,2]

# %%
a[2,:]

# %%
a[0:1,:]

# %%
a

# %%
a[:,2] = 1.0

# %%
a[2,:] = 5.0

# %% [markdown]
# ## Vectorización, operaciones entre arreglos y funciones de arreglos

# %%
# dos matrices 3x3 de números aleatorios entre cero y uno
a = np.random.rand(3,3)
b = np.random.rand(3,3)

# %%
a

# %%
b

# %%
# multiplicar por dos cada elemento de a
2 * a

# %%
# sumar 3j a cada elemento de a, notar la transformación de tipo
a + 3.0j

# %%
# suma de a y b
a + b

# %%
# resta de a y b
a - b

# %%
# producto ELEMENTO A ELEMENTO entre a y b
a * b

# %%
# producto matricial de a y b
a @ b

# %%
# otra forma de expresar el producto matricial de a y b
a.dot(b)

# %%
# otra forma mas de expresar el producto matricial de a y b
np.dot(a,b)

# %%
# seno elemento a elemento
np.sin(a)

# %%
# loraritmo elemento a elemento
np.log(b)

# %%
# matriz transpuesta
a.T

# %%
# suma de todos los elementos de a
np.sum(a)

# %%
# vector con los elementos diagonales de a
a.diagonal()

# %%
a

# %%
# valor máximo de entre los elementos de a
a.max()

# %%
# valor mínimo de entre los elementos de a
a.min()

# %%
# tupla de coordenadas del elemento máximo
np.unravel_index(np.argmax(a), a.shape)

# %%
# media entre los elementos de a
a.mean()

# %%
# suma de los elementos de a fila a fila
np.sum(a,axis=0)

# %%
# suma de los elementos de a columna a columna
np.sum(a,axis=1)

# %%
# transpuesta congujada de a
(a + 1j).conjugate().T

# %%
# ndarray de Booleanos conteniendo la evaluación de la expresión lógica elemento a elemento
a > 0.5

# %%
# valores de a que cumplen con la condición
a[a > 0.5]

# %% [markdown]
# ## Vectorización de funciones definidas por el usuario

# %%
a = np.random.rand(3,3) - 0.5

# %%
a


# %% [markdown]
# Defino una función como lo hemos hecho siempre

# %%
def val_abs(x):
    if x >= 0.0:
        return x
    else:
        return -x


# %% [markdown]
# al tratar de aplicarla a un `ndarray` falla

# %%
val_abs(a)

# %% [markdown]
# la función `numpy.vectorize()` me devuelve una versión *vectorizada* que puedo utilizar con argumentos de tipo `ndarray`

# %%
vec_abs = np.vectorize(val_abs)

# %%
vec_abs(a)

# %% [markdown]
# ## Siempre que sea posible usar operaciones vectorizadas

# %%
a = np.random.rand(1000,1000) - 0.5
b = np.random.rand(1000,1000) - 0.5
c = np.zeros_like(a)

# %%
# %%timeit
for i in range(1000):
    for j in range(1000):
        c[i,j] = m.cos(a[i,j]) + m.sin(b[j,i])

# %%
# %%timeit
c = np.cos(a) + np.sin(b.T)

# %% [markdown]
# Notar que la versión vectorizada es 100 veces más rápida!

# %% [markdown]
# ## Algunos gráficos

# %% [markdown]
# Utilizando Numpy y sus herramientas para generar arreglos y aplicarles funciones se facilita enormemente la creación de gráficos, entre muuuuchas otras operaciones. Si utilizaramos listas deberíamos (como lo hicimos antes) escribir bucles para operar elemento a elemento. La potente interfaz vectorial de numpy permite generar código complejo de forma elegante y legible.

# %%
x = np.linspace(0,15*m.pi,1000)
y = np.exp(-0.1*x)*np.sin(5*x)

# %%
plt.plot(x,y)

# %% [markdown]
# La función `numpy.meshgrid()` permite obtener dos matrices que contienen los valores de las coordenadas x e y en una grilla dimensional a partir de un par de vectores conteniendo los valores de x e y en los ejes. Esto me permite generar luego, sobre esa greilla los valores de una función de dos variables y graficarla.

# %%
x = np.linspace(0, 2*m.pi, 500)
y = np.linspace(0, 2*m.pi, 500)  
xm, ym = np.meshgrid(x, y)

# %%
z = np.sin(xm)**10 + np.cos(10 + ym*xm) * np.cos(xm)

# %% [markdown]
# El siguiente es un gráfico de contornos

# %%
plt.contour(x, y, z)

# %% [markdown]
# El siguiente es un gráfico de contornos llenos

# %%
plt.contourf(x, y, z)
plt.colorbar()

# %% [markdown]
# La función `streamplot` permite hacer gráficos de funciones vectoriales.

# %%
x = np.linspace(-m.pi, m.pi, 300)
y = np.linspace(-m.pi, m.pi, 300)  
xm, ym = np.meshgrid(x, y)

# %%
u = -1 - xm**2 + ym
v = 1 + xm - ym**2
speed = np.sqrt(u*u + y*y)

# %%
plt.streamplot(xm,ym,u,v,color=speed)

# %%
