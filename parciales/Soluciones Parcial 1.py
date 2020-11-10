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
# ## Ejercicio 1
#
# Graficar la función 
#
# $$ f(x) = e^{-x}\sin 10x $$
#
# en el intervalo $[0,10]$.

# %%
import matplotlib.pyplot as plt
import math as m

# %%
xs = [i * 10 / 1000 for i in range(1001)]


# %%
plt.plot(xs,[m.exp(-x)*m.sin(10*x) for x in xs])


# %% [markdown]
# ## Ejercicio 2
#
# Implementar una función que clasifique un triángulo como rectángulo, acutángulo u obtuso dadas las longitudes de sus lados $a$,$b$ y $c$ en base a la siguiente tabla:
#
# |     Condición                    |  Tipo|
# |-----|-----|
# | si $a^2 + b^2 = c^2$ | el triángulo es **rectángulo** |
# | si $a^2 + b^2 > c^2$ | el triángulo es **acutángulo** |
# | si $a^2 + b^2 < c^2$ | el triángulo es **obtuso** |

# %%
def que_triángulo(a,b,c):
    if a**2 + b**2 > c**2:
        print('El triángulo es acutángulo')
    elif a**2 + b**2 < c**2:
        print('El triángulo es obtusángulo')
    else:
        print('El triángulo es rectángulo')


# %% [markdown]
# hay que tener cuidado con el igual porque me huele que esa función no va a encontrar ningún triángulo rectángulo

# %%
c = m.sqrt(0.1**2+0.7**2)

# %%
que_triángulo(0.1,0.7,c)

# %%
0.1**2+0.7**2,c**2


# %% [markdown]
# Efectivamente, entonces habría que hacer lo que sigue por lo menos. A esto los que prestaron atención en el teórico deberían intentarlo:

# %%
def que_triángulo2(a,b,c, tol=1e-13):
    if abs(a**2 + b**2 - c**2) <= tol:
        print('El triángulo rectángulo')
    elif a**2 + b**2 > c**2:
        print('El triángulo es acutángulo')
    elif a**2 + b**2 < c**2:
        print('El triángulo es obtusángulo')
    else:
        print('Algo anduvo mal')


# %%
que_triángulo2(0.1,0.7,c)


# %% [markdown]
# ## Ejercicio 3
#
# Implementar una función que encuentre determine las componentes del vector $\mathbf{C}$, donde $\mathbf{C}=\mathbf{A}\times\mathbf{B}$ es el producto vectorial entre los vectores $\mathbf{A}$ y $\mathbf{B}$. La función debe aceptar como parámetros dos listas de tres elementos conteniendo las componentes de $\mathbf{A}$ y $\mathbf{B}$ y devolver una lista 
# de tres elementos que contenga las componentes de $\mathbf{C}$

# %%
def producto_vectorial(A,B):
    C = []
    C += [A[1]*B[2]-A[2]*B[1]]
    C += [A[2]*B[0]-A[0]*B[2]]
    C += [A[0]*B[1]-A[1]*B[0]]
    return C


# %%
producto_vectorial([1,2,3],[3,2,1])


# %% [markdown]
# ## Ejercicio 4
#
# La ecuación Pitagórica 
# $$i^2+j^2=z^2$$
# tiene un número infinito de soluciones enteras **positivas** llamadas "triplas Pitagóricas". 
#
# a. Diseñar e implementar una función que calcule  (imprima) todas las triplas Pitagóricas para un dado $m$ tal que $i \le m$, $j\le m$ y $k\le m$. No importa si el código devuelve algunas triplas repetidas.
#
# b. Modificar la función para "probar" el último teorema de Fermat, que asegura que no existe ninguna solución de enteros positivos a 
# $$i^n+j^n=z^n$$
# si $n>2$, para un dado $m$ tal que $i \le m$, $j\le m$ y $k\le m$.
#
# c. (**opcional**) Modificar la función para que devuelva una secuencia de tuplas que contenga las triplas sin repeticiones.

# %%
def triplas_pitagóricas(n):
    cuantas = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i**2 + j**2 == k**2:
                    print(i,j,k)
                    cuantas += 1
    print(f'hay {cuantas} triplas')


# %%
triplas_pitagóricas(100)

# %%
9**2+12**2,15**2


# %%
def plimpton(m):
    cuantas = 0
    for n in range(1, m+1): #Empiezo desde 1 para evitar las ternas con cero por la trivialidad
        for l in range(1, m+1):
            if (l > n):
                i = l**2 - n**2
                j = 2 * n * l
                k = n**2 + l**2
                if i<=m and j<=m and k<=m:
                    print(i,j,k)
                    cuantas += 1
    print(f'hay {cuantas} triplas')


# %%
plimpton(50)


# %%
def triplas_pitagóricas(n):
    cuantas = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i**2 + j**2 == k**2:
                    print(i,j,k)
                    cuantas += 1
    print(f'hay {cuantas} triplas')


# %%
import itertools # Acá estoy haciendo trampa para encontrar las permutaciones, hay formas más simples (ordenar las triplas por ej. )


# %%
def triplas_p_únicas(n):
    l = []
    for p in itertools.permutations([i for i in range(1,n)],r=3):
        if p[0]**2 + p[1]**2 == p[2]**2: l += [p]
    return l


# %%
lista = triplas_p_únicas(100)

# %%
len(lista)


# %%
def fermat(m,n):
    fermat = True
    for i in range(1,m+1):
        for j in range(1,m+1):
            for k in range(1,m+1):
                if i**n + j**n == k**n: fermat = False

    if fermat: print(f'Fermat tiene razón hasta {m}')


# %%
fermat(50,3)


# %% [markdown]
# ## Ejercicio 5
#
# Una serie de Fourier tiene la forma
#
# $$s(x) = \frac{a_0}{2}+\sum_{i=1}^n \left( a_i \cos(ix) + b_i \sin(ix) \right)$$
#
# y puede aproximar (con valores adecuados de ($a_i$ y $b_i$) cualquier función periódica de período $2\pi$.
#
# a. Implementar una función que acepte como parámetros dos listas conteniendo los conjuntos de coeficientes $\{a_i\}$ y $\{b_i\}$ y evalúe la correspondiente serie de Fourier para un argumento $x\in \mathbb{R}$.
#
# b. Utilizar la función anterior para implementar una nueva función que evalúe la serie de Fourier de la función *serrucho* para la cual 
#
# $$a_i = 0\ \forall\ i$$
# y
# $$b_i = \frac{2(-1)^{i+1}}{i \pi}\ \forall i\ge 1$$
#
# c. Comparar gráficamente la aproximación de órden $6$ para la función serrucho. Utilizar la siguiente definición para la función serrucho:
#
# `def f(x):
#     return 2*((x+1/2) - m.floor(x+1/2)) - 1`
#

# %%
def serie_fourier(x,ass,bss,N):
    s = ass[0]/2
    for n in range(1,N+1):
        s += ass[n] * m.cos(n*x) + bss[n] * m.sin(n*x)
    return s


# %%
def bs_serrucho(N):
    return [0] + [2*(-1)**(i+1)/i/m.pi for i in range(1,N+1)]


# %%
N = 10
bs = bs_serrucho(N)
ass = [0 for i in range(0,N+1)]


# %%
def f(x):
    return 2*((x+1/2) - m.floor(x+1/2)) - 1


# %%
xmin = - 2
xmax = 2
nx = 1000
xs = [xmin + i * (xmax-xmin) / nx for i in range(1001)]
ys = [serie_fourier(x*2*m.pi,ass,bs,N) for x in xs]
yss = [f(x) for x in xs]

# %%
plt.plot(xs,ys)
plt.plot(xs,yss)

# %%
bs

# %%
