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
# # Identificadores y asignaciones
#
# Las siguientes son asignaciones válidas, notar que podemos usar caracteres unicode:

# %%
# se asigna un literal a un identificador
π = 3.14159265358979323846264338327950288419716939937510 

# %%
π

# %%
# se asigna un literal a un identificador
RadioEsfera = 2.718 

# %%
esto_ = 2

# %%
esto_y_esto = 5

# %% [markdown]
# Las siguientes no son válidas:

# %%
😀 = 'esto es una cara feliz'

# %%
esto y esto = 5

# %%
esto/esto = 5

# %%
esto.esto = 5 # esta podría ser válida, lo vemos cuando lleguemos a objetos

# %% [markdown]
# Notemos que en programación el signo `=` no representa lo mismo que en notación matemática. La operación de asignación siguiente involucra varios pasos, por un lado la evaluación de la expresión a la derecha (que implica varios pasos) y luego la operación de asignación:

# %%
# se asigna el valor de una expresión a un identificador
VolumenEsfera = (4/3) * π * RadioEsfera**3 

# %%
print(VolumenEsfera)

# %% [markdown]
# Quizás es un poco redundante pero la asignación no implica una relación funcional entre las variables que la conforman, si cambiamos `RadioEsfera` la variable `VolumenEsfera` sigue valiendo lo mismo:

# %%
RadioEsfera = 3.0

# %%
print(VolumenEsfera)

# %% [markdown]
# Por lo que decimos más arriba, si invertimos el orden de la asignación la misma no funciona, sólo es posible asignar a *identificadores*:

# %%
(4/3) * π * RadioEsfera**3 = VolumenEsfera

# %% [markdown]
# Es un corolario de lo anterior casi, pero como mencionamos cuando hablamos de las f-strings, la expresión entre llaves se evalúa en el momento de crear el literal:

# %%
s = f"El volumen de la esfera es {VolumenEsfera}"

# %%
print(s)

# %%
VolumenEsfera = 0

# %% [markdown]
# A pesar de cambiar el valor de la variable `VolumenEsfera`, `s` vale lo mismo que antes:

# %%
print(s)

# %% [markdown]
# No lo mencionamos en la "teoría" pero la siguiente es una asignación válida en Python:

# %%
a = b = RadioEsfera - 1 # La cadena de variables e iguales puede ser todo lo larga que quiera

# %%
a

# %%
b

# %% [markdown]
# Pero por las mismas razones que antes la que sigue no:

# %%
a = b + 1 = 2

# %% [markdown]
# # Asignaciones múltiples
#
# Las asignaciones múltiples son útiles:

# %%
a, b = 1, 2

# %%
print(a,b)

# %% [markdown]
# Pero tampoco hay que llevarlas al extremo porque el código se hace muy dificil de leer

# %%
a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7

# %% [markdown]
# La razon por la cual esas asignaciones funcionan es porque en realidad son una notación abreviada de:

# %%
(a, b, c, d, e, f, g) = (1, 2, 3, 4, 5, 6, 7)

# %% [markdown]
# donde las expresiones entre paréntesis son "tuplas" a las cuales aún no llegamos. La palabra más adecuada en castellano para este tipo quizás sea n-upla.

# %% [markdown]
# Podemos agregar a nuestra lista de funciones útiles, sobre todo para programación interactiva la función `type` que pertenece a la librería estándard y me dice de qué tipo es el parámetro:

# %%
type(1)

# %%
type((a,b))

# %%
type(π)

# %%
type(s)

# %% [markdown]
# Notemos que en el último caso `s` que era una f-string es una `str` o cadena. Las f-strings sólo existen como literales que se transforman en una cadena cuando se evalúan.

# %% [markdown]
# Hay un caso muy útil para las asignaciones múltiples que es el intercambio de nombres de variables:

# %%
a = 1

# %%
b = 2

# %%
print(a,b)

# %%
a,b = b,a

# %%
print(a,b)

# %% [markdown]
# # Asignación aumentada
#
# Como dijimos, la expresión `a += 1` es equivalente a `a = a + 1`:

# %%
a = 1
a += 1
a

# %%
a = 2
a *= 2
a

# %%
a = 2
a /= 2
a

# %%
a = 2
a //= 2
a

# %%
a = 2
a -= 1
a

# %% [markdown]
# # Operaciones con cadenas
#
# Nos salimos de tema pero:

# %%
s1 = 'Hola'
s2 = ' '
s3 = 'Humano'
s1 + s2 + s3

# %% [markdown]
# El operador `+` cuando opera con cadenas las concatena. Y la multiplicación:

# %%
'tres' * 3

# %%
3 * 'tres'

# %% [markdown]
# pero

# %%
'tres' * 'tres'

# %% [markdown]
# # Una cápsula de sintaxis e interactividad

# %% [markdown]
# En Python casi todas las expresiones tienen un valor de algún tipo. Cuando ejecutamos una línea en el intérprete de forma interactiva o en una celda de Jupyter Notebook lo que se devuelve en `Out` es el valor de la última expresión que lo posea, si lo posee:

# %%
a = 1
b = 2
a + 2 # esta expresión vale 3, pero no es la última
a + 3 # esta expresión vale 4, la celda devuelve 4

# %%
a = 1
b = 2
c = a + 3 # esta expresión no tiene un valor, a pesar de que hace algo, la celda no devuelve nada

# %% [markdown]
# Hasta ahora hemos separado las expresiones con separadores de línea, pero también se pueden separar con `;`:

# %%
a = 1; b = 2; a + 2; a + 3; 

# %% [markdown]
# Notar la diferencia con la línea que sigue:

# %%
a = 1; b = 2; a + 2; a + 3

# %%
a = 1; b = 2; c = a + 3

# %% [markdown]
# Hay un valor para eso que no vale nada y es `None`, si ponemos `None` en una celda no nos devuelve nada:

# %%
None

# %% [markdown]
# `None`, como todo en python, incluso tiene un tipo:

# %%
type(None)

# %% [markdown]
# Nos adelantamos un poco pero tenemos que:

# %%
print(2)

# %% [markdown]
# "parece" devolver 2, pero ese es un "efecto colateral" de la función `print` que imprime el resultado de la o las expresiones que tenga como argumento pero que en realidad no devuelve nada como resultado, no hay `Out`. Si hacemos:

# %% [markdown]
# La expresión se evalúa de adentro hacia afuera, el primer `print` imprime `2`, el segundo imprime el resultado del primer `print` que es `None`:

# %%
print(print(2))

# %% [markdown]
# Quizás es un poco más explícito si hacemos lo que sigue, que imprime 2 al evaluar el `print` y devuelve en `Out` el valor del tipo de la salida de print:

# %%
type(print(2))

# %% [markdown]
# Ok, nos estamos pasando de rosca!

# %%
print("fin")

# %%
