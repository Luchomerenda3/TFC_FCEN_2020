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
#   kernel_info:
#     name: python3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Transformada de Fourier Discreta y Transformada Rápida de Fourier
#
# <section class="post-meta">
# Carlos Ruestes, Cristián Sanchez
# </section>
# Última edición: Noviembre de 2020
# ___

# %% [markdown]
# Este notebook presenta una introducción corta a la transformada de Fourier discreta (DFT) y a la transformada rápida de Fourier (FFT). Se utilizará el algoritmo radix-2 Cooley-Tukey FFT.
#
# Estos conceptos tiene una amplia variedad aplicaciones en diferentes áreas de la ciencia, tanto en física como en matemática, por ejemplo, procesamiento de señales, filtrado de sonido e imágenes, compresión de datos, ecuaciones diferenciales en derivadas parciales, etc.

# %%
import numpy as np
from numpy import random as rnd
import timeit
from scipy import fftpack as fft


# %% [markdown]
# ## Transformada de Fourier Discreta (DFT)

# %% [markdown]
# Sea $\vec x = [x_0,x_1,...,x_{n-1}]$ un vector con $n$ elementos complejoss (o reales). La DFT de $\vec x$ es el vector complejo $\vec y = [y_0,y_1,...,y_{n-1}]$, donde los elementos estan definidos como 
# $$y_k=\sum_{j=0}^{n-1}x_j\omega^{k\cdot j},$$
# donde $\omega = \exp(-2\pi i /n)$. 

# %%
def DFT(x):
    """ Calcula la DFT unidimensional de un vector.
    
    :x: double arr. El vector a transformar.
    :returns: double arr. Transformada de x.
    """
    n = len(x)
    y = [0]*n
    omega = np.exp(-2.0j*np.pi/n)
    for k in range(0,n):
        y[k] = np.sum(x*omega**(np.arange(0,n)*k))
    return y


# %% [markdown]
# Es fácil darse cuenta que la DFT inversa esta dada por
# $$x_k = \sum_{j=0}^{n-1} y_j\omega^{k\cdot j},$$
# donde $\omega = \exp(2\pi i/n)$.

# %%
def inverseDFT(y):
    """ Calcula la inversa de la DFT unidimsensional 
    de un vector.
    
    :y: double arr. El vector a transformar.
    :returns: double arr. la inversa de la transformada de y.
    """
    n = len(y)
    x = [0]*n
    omega = np.exp(2.0j*np.pi/n)
    for k in range(0,n):
        x[k] = np.sum(y*omega**(np.arange(0,n)*k))/float(n)
    return x


# %% [markdown]
# Tomemos un ejemplo sencillo donde transformamos y antitransformamos (inversa de la transformada) de un vector arbitrario.

# %%
# Definimos un array a transformar.
x = rnd.randint(8,size=8)
print('x =', x)
# Transformada de Fourier
y = DFT(x)
print('y =', np.round(y,2))
# Inversa DFT 
x = inverseDFT(y)
print('x =', np.round(x,2))


# %% [markdown]
# Este algoritmo DFT es algo ineficiente. Hay muchos subcálculos que se realizan más de una vez y como consecuencia, el algoritmo escalea como $\mathcal O(n^2)$. 

# %% [markdown]
# ## Transformada rápida de Fourier (FFT)
# Los algoritmos de FFT explotan las simetrías y el hecho de que muchas operaciones son similares, obteniendo rendimientos mejorados. Comentaremos aquí el algoritmo de Cooley–Tukey [1].
#
# Asumimos que $N$ es compuesto. Es decir, que $N=n_1\cdot n_2$, donde $N$, $n_1$ y $n_2$ son enteros. Reescribiendo los dos índices como 
# $$k=n_2k_1+k_2,$$
# $$j = n_1j_2 + j_1,$$
# donde $k_{1,2} = 0,1,...,n_{1,2}-1$ y $j_{1,2} = 0,1,...,j_{1,2}-1$. Si insertamos estos nuevos índices en la DFT, algunos términos cruzados desaparecen, y el resultado final es 
# $$y_{n_2k_1+k_2}=\sum_{j_1=0}^{n_1-1}\sum_{j_2=0}^{n_2-1}x_{n_1j_2+n_1}\exp\left[\frac{-2\pi i}{n_1n_2}(n_1j_2+j_1)(n_2k_1+k_2)\right]$$
# $$=\sum_{j_1=0}^{n_1-1}\exp\left[-\frac{2\pi i}{n}j_1k_2\right]\left(\sum_{j_2=0}^{n_2-1}x_{n_1j_2+j_1}\exp\left[-\frac{2\pi i}{n_2}j_2k_2\right]\right)\exp\left[-\frac{2\pi i}{n_1}j_1k_1\right].$$
#
# En esta ecuación, cada suma interna es una DFT de tamaño $n_2$ y cada suma externa is una DFT de tamaño $n_1$. Esto da una fórmula recursiva para computar la DFT, que se explica en mayor detalle en [3]. Por simplicidad, usaremos el algoritmo radix-2. Este algoritmo escalea como $\mathcal O (n\log n)$, lo que lo hace casi lineal para conjuntos de datos muy grandes.

# %%
def CooleyTukeyRadix2FFT(x):
    """ Calcula la DFT unidim de un vector usando algoritmo radix-2 Cooley-Tukey 
    El vector a transformar debe tener una cantidad de elementos potencia de 2.
    
    :x: double arr. Vector a transformar
    :returns: double arr. Transformada del vector
    """
    # Verificar que n es pot de 2.
    if ( len(x) & (len(x) - 1)):
        raise Exception("El numero de elementos de x debe ser potencia de 2!")
    # Formula recursiva para la FFT.
    def foo(x):
        n = len(x)
        if n == 1:
            y = x
        else:
            y2 = foo(x[0:n:2])
            y1 = foo(x[1:n + 1:2])
            d = np.exp(-2j*np.pi/n)**np.arange(0,n/2)
            y = np.append(y2 + d*y1,y2 - d*y1)
        return y
    return foo(x)

def inverseCooleyTukeyRadix2FFT(y):
    """ Calcula la antitransformada unidimens. de un vector usando
    algoritmo radix-2 Cooley-Tukey FFT. El vector a transformar
    debe tener elementos en cantidad potencia de 2.
    Parametros:
        x: double arr. El vector a transformar.
    Returns:
        y: double arr. transformada del vector.
    """
    # Verificar que n es potencia de 2.
    if (len(y) & (len(y) - 1)):
        raise Exception("El numero de elementos de x debe ser potencia de 2!")
    # Formula recursiva para la FFT.
    def foo(y):
        n = len(y)
        if n == 1:
            x = y
        else:
            x2 = foo(y[0:n:2])
            x1 = foo(y[1:n + 1:2])
            d = np.exp(2j*np.pi/n)**np.arange(0,n/2)
            x = np.append(x2 + d*x1,x2 - d*x1)
        return x
    return foo(y)/len(y)


# %% [markdown]
# Veamos nuevamente un ejemplo sencillo

# %%
# Definimos el array a transformar.
x = rnd.randint(10,size=8)
print('x =', x)
# Transformada de Fourier.
y = CooleyTukeyRadix2FFT(x)
print('y =', np.round(y,2))
# Antitransformada. 
x = inverseCooleyTukeyRadix2FFT(y)
print('x =', np.round(x,2))

# %% [markdown]
# Para demostrar la superioridad de la FFT, calculemos la transformada de Fourier de un conjunto de datos grande, comparando además con el función fft de scipy.fftpack.

# %%
x = rnd.rand(16)
# Tomemos los tiempos de DFT, CooleyTukeyRadix2FFT y scipy.fftpack.fft.
# %timeit y = DFT(x)
# %timeit y = CooleyTukeyRadix2FFT(x)
# %timeit y = fft.fft(x)

# %% [markdown]
# ## Significado físico
#
# La DFT mapea una secuencia finita de datos equiespaciados de su dominio original a un dominio en frecuencia. En otras palabras, un conjunto de datos temporales discreto resulta transformado a un conjunto de frecuencias discreto.
#
# Para ilustrar esto, necesitamos entender el significado físico de la fórmula de DFT. Comenzamos reescribiendo la misma 
# $$x_k=\sum_{j=0}^{n-1}y_j\exp\left(2\pi i\frac{k}{n\Delta t}j\Delta t\right).$$
# Lo que la expresión nos dice es simplemente que $\vec x$ es una superposición de funciones exponenciales con diferences frecuencias $f_j = \frac{j}{n\Delta t}$ y amplitudes $y_j$. Por esta razón, podemos ver la magnitud de las amplitudes $|y_k|^2$ como una medida del "peso de la frecuencia $f_j$" en $\vec x$!

# %% [markdown]
# ## DFT multidimensional
# Sea $\vec j = (j_1,j_2,...,j_d)$ y $\vec k = (k_1,k_2,...,k_d)$ vectores $d$-dimensionales con indices de $\vec 0$ a $\vec n-1 = (n_1-1,n_2,...,n_d-1)$. Luego, La DFT $d$-dimensional esta dada por
# $$y_\vec{k}=\sum_{\vec j=\vec 0}^{\vec n-1}x_\vec{j}\exp\left[-2\pi\vec k\cdot\vec \xi\right],$$
# donde $\vec \xi$ es la división elemento a elemento $(j_1/n_1,...,j_d/n_d)$ [3]. Por ejemplo, la DFT bidimensional esta dada por
# $$\vec y_{k_1,k_2}=\sum_{j_1=0}^{n_1-1}\sum_{j_2=0}^{n_2-1}x_{j_1,j_2}\exp\left[-2\pi i\left(\frac{ k_1j_1}{n_1}+\frac{k_2j_2}{n_2}\right)\right].$$

# %% [markdown]
# Referencias:  
# [1] James W. Cooley and John W. Tukey: An Algorithm for the Machine Calculation of Complex Fourier Series, Math. Comp. 19 (1965), p. 297-301  
# [2] Wikipedia: https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm,   
# [3] Wikipedia: https://en.wikipedia.org/wiki/Discrete_Fourier_transform,  
#
# Ref. FFT pack en SciPy:
# http://docs.scipy.org/doc/scipy/reference/fftpack.html  

# %%

# %%
