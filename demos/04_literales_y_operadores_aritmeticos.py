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
# # Literales, números y operaciones aritméticas
#
# Parte del TFC 2020

# %% [markdown]
# ## Literales enteros

# %% [markdown]
# Todas las que siguen son formas válidas de expresar el entero 1234567890

# %%
1234567890

# %%
1_234_567_890

# %%
0o11145401322

# %%
0x499602d2

# %%
0B100_10011_0010110_0000001_011010010

# %% [markdown]
# Para obtener la representación binaria, octal o hexadecimal de un entero podemos usar las funciones siguientes. Notar que los resultados son cadenas de caracteres.

# %%
bin(3141592654)

# %%
oct(3141592654)

# %%
hex(3141592654)

# %% [markdown]
# Como dijimos, los enteros en Python no tienen cota superior ni inferior:

# %%
4713 * 2**4713 + 1 # El segundo número primo (de los 15 conocidos) en la secuencia de Cullen

# %% [markdown]
# ## Literales de punto flotante

# %% [markdown]
# Todas las que siguen son formas válidas de expresar números de punto flotante:

# %%
1.0e4

# %%
10_000.0

# %%
10000.

# %%
1 + 3 * 0. # Al haber un operando que es de punto flotante se "promociona" a la expresión

# %%
234.5e-14

# %% [markdown]
# Los números de punto flotante en la implementación "C" de python son de 64 bits, lo que involucra una precición de 16 cifras decimales (después haremos esta frase más precisa).

# %%
1e-15 + 1 

# %%
1e-16 + 1

# %% [markdown]
# Los números de punto flotante son siempre racionales. La precisión finita hace que algunas operaciones tengan resultados no evidentes.

# %%
(1e-15 + 1) - 1

# %%
1e-15 + (1 - 1.0)

# %%
1e-15 + (2. - 1.)

# %%
(1e-15 + 2.) - 1.

# %%
0.1 + 0.2

# %% [markdown]
# Este último es un resultado famoso y tiene su propio sitio web: [0.30000000000000004.com](https://0.30000000000000004.com)

# %%
3602879701896397 / 2 ** 55

# %%
0.1 + 0.1 + 0.1

# %%
0.1.hex()

# %% [markdown]
# ## Complejos

# %% [markdown]
# Los imaginarios se representan con una "j" pegada (una notación "ingenieril" por lo general):

# %%
0.1j

# %% [markdown]
# Como dijimos los complejos se construyen como suma de un real y un imaginario:

# %%
1.0 + 1.0j

# %% [markdown]
# O usando la función `complex`:

# %%
complex(1.0,1.0)

# %% [markdown]
# La función `abs` se comporta como es de esperar:

# %%
abs(-1)

# %%
abs(1.0+1.0j)

# %%
abs(-1.)

# %% [markdown]
# # Cadenas de caracteres
#
# Todas las siguientes son cadenas de caracteres válidas

# %%
'''a
b'''

# %%
"""a
b"""

# %%
'a\nb'

# %% [markdown]
# `\n` es el 'código de escape' para una nueva línea.

# %%
print('a\nb')

# %%
'esto es una cadena'

# %%
"esto es una cadena"

# %%
"esta no anda'

# %%
'esta tampoco"

# %%
"una cadena puede usar comillas 'adentro', si es distinta de la de afuera"

# %%
'una cadena puede usar comillas "adentro", si es distinta de la de afuera'

# %%
"también puedo \"escapar\" las comillas"

# %%
'también puedo \'escapar\' las comillas'

# %% [markdown]
# Las cadenas de caracteres (y el código) en Python son cadenas [Unicode](https://home.unicode.org), con encoding (usualmente) [UTF-8](http://www.utf-8.com).
#
# Si alguien quiere saber más sobre Unicode hay [excelente artículos escritos](http://www.joelonsoftware.com/articles/Unicode.html) y por supuesto, [documentación sobre su uso en Python](https://docs.python.org/3/howto/unicode.html). 
#
# Pero... ¿Qué es Unicode y porqué me puede llegar a importar?

# %%
'\U0001F618\U0001F617\U0001F615\U0001F614\U0001F613\U0001F612'

# %%
'文字化け  لوحة المفاتيح العربية अशऋ'

# %%
'\U000003C0'

# %% [markdown]
# Para una lista de códigos mirar [aquí](https://www.unicode.org/charts/)

# %% [markdown]
# ## Cadenas de formato
#
# Las cadenas de formato son una evolución de la forma de construir cadenas a partir de expresiones para poder mostrar resultados. Tienen un montón de detalles de construcción pero en general basta con acordarse algunas pocas cosas para producir un gran conjunto de `f-strings` útiles. Si bien normalmente se las deja para más adelante creo que conviene encontrárselas lo antes posible para saber que están ahí para cuando sean necesarias y no pasarse horas googleando y haciendo un paste que quizás no resuelva del todo el problema.
#
# Una `f-string` permite generar una cadena que contiene el resultado de una expresión. La cadena empieza con `f'`, `F'`, `f"` o `F"` y contiene uno o más pares de llaves `{}`. Cuando se genera una `f-string` se evalúa la expresión que va entre las llaves, se le "da formato" es decir se convierte el resultado en una cadena de caracteres y se reemplaza esta cadena en donde estaban las llaves.
#
# Por ejemplo:

# %%
f"1/18, es en punto flotante, igual a {1/18}"

# %%
f"1/18 es, en punto flotante, igual a {1/18:.3g}, redondeado a tres cifras significativas"

# %%
f"1/18 es en punto flotante igual a {1/18:.3f}, redondeado a tres decimales"

# %%
f"1/18 es en notación exponencial igual a {1/18:.3e}, redondeado a tres decimales"

# %%
f"|{10*10*10:10d}|{10*10*10+5:10d}|{10*10*10-3145:10d}|"

# %%
f"|{1/3:10.5f}|{-1*1/3:10.5f}|{2-1/3:10.5f}|"

# %%
f"uno mas complicado {abs(10000+1j):x^+30_.3f}"

# %% [markdown]
# ## Precedencia
#
# Si uno tiene muy claro las reglas de precedencia puede escribir las cosas de manera que siempre funcionen, pero en general conviene usar paréntesis para aclarar el orden, que igual, como vimos más arriba en algunos casos es importante porque distintos órdenes dan distintos resultados.

# %%
1 + 2 * 3 / 2 * 3 / 3**2 - 2

# %%
2**2**2**2

# %%
2**(2**(2**2))

# %%
((2**2)**2)**2

# %% [markdown]
# # Cuando las cosas no andan

# %%
1/0 # La división por cero es un error

# %%
2.0**10000 

# %%
2.0e10000 # Este número es mayor al mayor número representable (en valor absoluto) 
          # pero no da Overflow 🤔

# %%
2.0e-10000 # Este número es menor al menor número representable (en valor absoluto)

# %%
0.1.hex()

# %%
2.0e10000/2.0e10000 # Infinito sobre Infinito

# %%
2.0e10000 - 2.0e10000 # Infinito menos Infinito

# %%
