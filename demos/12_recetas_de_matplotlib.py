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
# # Recetas de matplotlib

# %% [markdown]
# ## Gráficos simples
#
# Vamos a a aprender como graficar funciones. Uno de los paquetes de graficación más utilizados en Python es el subpaquete `pyplot` que se encuentra en la librería `matplotlib` Para armar un gráfico simple necesitamos un conjunto de puntos definidos de forma fal que sus absisas estén en una lista y sus ordenadas en otra.

# %%
import matplotlib.pyplot as plt
import math as m

# %%
xs = [0.0, 1.0 , 2.0, 3.0]

# %%
ys = [0.0, 1.0, 4.0, 9.0 ]

# %%
ys2 = xs

# %%
plt.plot(xs,ys)
plt.plot(xs,ys2)

# %%
plt.plot(xs,ys,color='red',linewidth='2.0',marker='o',label='parábola')
plt.xlim(0,5)
plt.ylim(0,10)
plt.xlabel('abcisas')
plt.ylabel('ordenadas')
plt.title('Mi Bello Gráfico')
plt.grid(True)
plt.legend(loc=2)
plt.text(3.1,9,'Este punto es el último')

# %%
nx = 100
xmin = -m.pi
xmax = m.pi

# %%
xs = []
ys = []
for (i,x) in enumerate(range(nx)):
    x = xmin + i * (xmax - xmin)/nx
    y = m.cos(3*x)
    xs.append(x)
    ys.append(y)

# %%
plt.plot(xs,ys)


# %%
def generar_puntos(f,xmin,xmax,nx):
    xs = []
    ys = []
    for i in range(nx):
        x = xmin + i * (xmax - xmin)/nx
        y = f(x)
        xs.append(x)
        ys.append(y)
    return xs, ys


# %%
xs, ys = generar_puntos(lambda x: (m.cos(10*x)*m.exp(-x)),0,5,1000)
plt.plot(xs,ys)

# %%
xs, ys = generar_puntos(lambda x: 10**x,0,5,1000)
plt.plot(xs,ys)
plt.yscale('log')


# %% [markdown]
# ## Gráficos de funciones paramétricas

# %%
def generar_puntos_parametric(f_x,f_y,tita_min=0.0,tita_max=2*m.pi,ntita=10000):
    xs = []
    ys = []
    for i in range(ntita):
        tita = tita_min + i * (tita_max - tita_min)/ntita
        x = f_x(tita)
        y = f_y(tita)
        xs.append(x)
        ys.append(y)
    return xs, ys


# %%
xs, ys = generar_puntos_parametric(lambda x: m.cos(x),lambda x: m.sin(x))
plt.plot(xs,ys)

# %%
figura = plt.figure()
ejes = figura.add_subplot(1,1,1)
ejes.plot(xs,ys)
ejes.set_aspect('equal')

# %%
xs, ys = generar_puntos_parametric(lambda x: m.cos(3*x),
                                   lambda x: m.sin(4.0*x),
                                   tita_max=20*m.pi)
figura = plt.figure(figsize=(9.0,9.0))
ejes = figura.add_subplot(1,1,1)
ejes.plot(xs,ys)
ejes.set_aspect('equal')

# %%
xs, ys = generar_puntos_parametric(lambda x: m.cos(3*x),
                                   lambda x: m.sin(4.05*x),
                                   tita_max=20*m.pi)
figura = plt.figure(figsize=(9.0,9.0))
ejes = figura.add_subplot(1,1,1)
ejes.plot(xs,ys)
ejes.set_aspect('equal')

# %%
xs, ys = generar_puntos_parametric(lambda x: m.cos(3*x),
                                   lambda x: m.sin(m.pi*x),
                                   tita_max=100*m.pi)
figura = plt.figure(figsize=(9.0,9.0))
ejes = figura.add_subplot(1,1,1)
ejes.plot(xs,ys)
ejes.set_aspect('equal')


# %% [markdown]
# ## Gráficos de funciones polares

# %%
def generar_puntos_polar(f,tita_min=0.0,tita_max=2*m.pi,ntita=10000):
    xs = []
    ys = []
    for i in range(ntita):
        tita = tita_min + i * (tita_max - tita_min)/ntita
        r = f(tita)
        x = r * m.cos(tita)
        y = r * m.sin(tita)
        xs.append(x)
        ys.append(y)
    return xs, ys


# %%
x1, y1 = generar_puntos_parametric(lambda x: m.cos(x)/(1+m.sin(x)**2)
                             ,lambda x: m.sin(x)*m.cos(x)/(1+m.sin(x)**2))

# %%
x2, y2 = generar_puntos_polar(lambda x: (1+m.cos(x)))

# %%
x3, y3 = generar_puntos_polar(lambda x: x,tita_max=10*m.pi)

# %%
x4, y4 = generar_puntos_polar(lambda x: 1)

# %%
figura = plt.figure(figsize=(9.0,9.0))
figura.subplots_adjust(hspace=0.3, wspace=0.3)

ejes1 = figura.add_subplot(2,2,1)
ejes1.set_title('lemniscata')
ejes2 = figura.add_subplot(2,2,2)
ejes2.set_title('cardioide')
ejes3 = figura.add_subplot(2,2,3)
ejes3.set_title('espiral de Arquímedes')
ejes4 = figura.add_subplot(2,2,4)
ejes4.set_title('círculo')

ejes1.plot(x1,y1,color='red',linewidth='2.0')
ejes2.plot(x2,y2,color='red',linewidth='2.0')
ejes3.plot(x3,y3,color='red',linewidth='2.0')
ejes4.plot(x4,y4,color='red',linewidth='2.0')

# %%
xs, ys = generar_puntos_polar(lambda x: m.cos(3*x))

figura = plt.figure(figsize=(9.0,9.0))
figura.subplots_adjust(hspace=0.3, wspace=0.3)

ejes1 = figura.add_subplot(1,1,1)

ejes1.plot(xs,ys,color='red',linewidth='2.0')
#ejes1.plot(xs,xs,color='green',linewidth='2.0')
ejes1.set_xlim(-1.1,1.1)
ejes1.set_ylim(-1.1,1.1)
ejes1.set_title('paquerette de mélibée',fontsize=50)
ejes1.set_xlabel('x',fontsize=25)
ejes1.set_ylabel('y',fontsize=25)
for axis in ['top','bottom','left','right']:
  ejes1.spines[axis].set_linewidth(2.0)
ejes1.xaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.yaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.grid(True)

# %%
xs, ys = generar_puntos_polar(lambda x: m.cos((2/5)*x),tita_max=10*m.pi)

figura = plt.figure(figsize=(9.0,9.0))
figura.subplots_adjust(hspace=0.3, wspace=0.3)

ejes1 = figura.add_subplot(1,1,1)

ejes1.plot(xs,ys,color='red',linewidth='2.0')
#ejes1.plot(xs,xs,color='green',linewidth='2.0')
ejes1.set_xlim(-1.1,1.1)
ejes1.set_ylim(-1.1,1.1)
ejes1.set_title('Rosa (coef. racional)',fontsize=50)
ejes1.set_xlabel('x',fontsize=25)
ejes1.set_ylabel('y',fontsize=25)
for axis in ['top','bottom','left','right']:
  ejes1.spines[axis].set_linewidth(2.0)
ejes1.xaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.yaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.grid(True)

# %%
xs, ys = generar_puntos_polar(lambda x: m.cos(m.e*x),tita_max=20*m.pi)

figura = plt.figure(figsize=(9.0,9.0))
figura.subplots_adjust(hspace=0.3, wspace=0.3)

ejes1 = figura.add_subplot(1,1,1)

ejes1.plot(xs,ys,color='red',linewidth='2.0')
#ejes1.plot(xs,xs,color='green',linewidth='2.0')
ejes1.set_xlim(-1.1,1.1)
ejes1.set_ylim(-1.1,1.1)
ejes1.set_title('Rosa (coef. irracional)',fontsize=50)
ejes1.set_xlabel('x',fontsize=25)
ejes1.set_ylabel('y',fontsize=25)
for axis in ['top','bottom','left','right']:
  ejes1.spines[axis].set_linewidth(2.0)
ejes1.xaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.yaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.grid(True)

# %%
xs1, ys1 = generar_puntos_polar(lambda x: m.cos(3*x))
xs2, ys2 = generar_puntos_polar(lambda x: m.cos(4*x))

figura = plt.figure(figsize=(9.0,9.0))
figura.subplots_adjust(hspace=0.3, wspace=0.3)

ejes1 = figura.add_subplot(1,1,1)

ejes1.plot(xs1,ys1,color='red',linewidth='2.0',linestyle='--',label='3')
ejes1.plot(xs1,xs2,color='green',linewidth='2.0',linestyle='-',label='4')
ejes1.set_xlim(-1.1,1.1)
ejes1.set_ylim(-1.1,1.1)
ejes1.set_title('$gráficos$',fontsize=50)
ejes1.set_xlabel('x',fontsize=25)
ejes1.set_ylabel('y',fontsize=25)
for axis in ['top','bottom','left','right']:
  ejes1.spines[axis].set_linewidth(2.0)
ejes1.xaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.yaxis.set_tick_params(width=2.0,length=5.0,labelsize=20)
ejes1.grid(True)
ejes1.legend()

# %%
