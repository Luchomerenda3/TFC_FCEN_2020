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
# Las siguientes son asignaciones v谩lidas, notar que podemos usar caracteres unicode:

# %%
# se asigna un literal a un identificador
蟺 = 3.14159265358979323846264338327950288419716939937510 

# %%
蟺

# %%
# se asigna un literal a un identificador
RadioEsfera = 2.718 

# %%
esto_ = 2

# %%
esto_y_esto = 5

# %% [markdown]
# Las siguientes no son v谩lidas:

# %%
馃榾 = 'esto es una cara feliz'

# %%
esto y esto = 5

# %%
esto/esto = 5

# %%
esto.esto = 5 # esta podr铆a ser v谩lida, lo vemos cuando lleguemos a objetos

# %% [markdown]
# Notemos que en programaci贸n el signo `=` no representa lo mismo que en notaci贸n matem谩tica. La operaci贸n de asignaci贸n siguiente involucra varios pasos, por un lado la evaluaci贸n de la expresi贸n a la derecha (que implica varios pasos) y luego la operaci贸n de asignaci贸n:

# %%
# se asigna el valor de una expresi贸n a un identificador
VolumenEsfera = (4/3) * 蟺 * RadioEsfera**3 

# %%
print(VolumenEsfera)

# %% [markdown]
# Quiz谩s es un poco redundante pero la asignaci贸n no implica una relaci贸n funcional entre las variables que la conforman, si cambiamos `RadioEsfera` la variable `VolumenEsfera` sigue valiendo lo mismo:

# %%
RadioEsfera = 3.0

# %%
print(VolumenEsfera)

# %% [markdown]
# Por lo que decimos m谩s arriba, si invertimos el orden de la asignaci贸n la misma no funciona, s贸lo es posible asignar a *identificadores*:

# %%
(4/3) * 蟺 * RadioEsfera**3 = VolumenEsfera

# %% [markdown]
# Es un corolario de lo anterior casi, pero como mencionamos cuando hablamos de las f-strings, la expresi贸n entre llaves se eval煤a en el momento de crear el literal:

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
# No lo mencionamos en la "teor铆a" pero la siguiente es una asignaci贸n v谩lida en Python:

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
# # Asignaciones m煤ltiples
#
# Las asignaciones m煤ltiples son 煤tiles:

# %%
a, b = 1, 2

# %%
print(a,b)

# %% [markdown]
# Pero tampoco hay que llevarlas al extremo porque el c贸digo se hace muy dificil de leer

# %%
a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7

# %% [markdown]
# La razon por la cual esas asignaciones funcionan es porque en realidad son una notaci贸n abreviada de:

# %%
(a, b, c, d, e, f, g) = (1, 2, 3, 4, 5, 6, 7)

# %% [markdown]
# donde las expresiones entre par茅ntesis son "tuplas" a las cuales a煤n no llegamos. La palabra m谩s adecuada en castellano para este tipo quiz谩s sea n-upla.

# %% [markdown]
# Podemos agregar a nuestra lista de funciones 煤tiles, sobre todo para programaci贸n interactiva la funci贸n `type` que pertenece a la librer铆a est谩ndard y me dice de qu茅 tipo es el par谩metro:

# %%
type(1)

# %%
type((a,b))

# %%
type(蟺)

# %%
type(s)

# %% [markdown]
# Notemos que en el 煤ltimo caso `s` que era una f-string es una `str` o cadena. Las f-strings s贸lo existen como literales que se transforman en una cadena cuando se eval煤an.

# %% [markdown]
# Hay un caso muy 煤til para las asignaciones m煤ltiples que es el intercambio de nombres de variables:

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
# # Asignaci贸n aumentada
#
# Como dijimos, la expresi贸n `a += 1` es equivalente a `a = a + 1`:

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
# El operador `+` cuando opera con cadenas las concatena. Y la multiplicaci贸n:

# %%
'tres' * 3

# %%
3 * 'tres'

# %% [markdown]
# pero

# %%
'tres' * 'tres'

# %% [markdown]
# # Una c谩psula de sintaxis e interactividad

# %% [markdown]
# En Python casi todas las expresiones tienen un valor de alg煤n tipo. Cuando ejecutamos una l铆nea en el int茅rprete de forma interactiva o en una celda de Jupyter Notebook lo que se devuelve en `Out` es el valor de la 煤ltima expresi贸n que lo posea, si lo posee:

# %%
a = 1
b = 2
a + 2 # esta expresi贸n vale 3, pero no es la 煤ltima
a + 3 # esta expresi贸n vale 4, la celda devuelve 4

# %%
a = 1
b = 2
c = a + 3 # esta expresi贸n no tiene un valor, a pesar de que hace algo, la celda no devuelve nada

# %% [markdown]
# Hasta ahora hemos separado las expresiones con separadores de l铆nea, pero tambi茅n se pueden separar con `;`:

# %%
a = 1; b = 2; a + 2; a + 3; 

# %% [markdown]
# Notar la diferencia con la l铆nea que sigue:

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
# "parece" devolver 2, pero ese es un "efecto colateral" de la funci贸n `print` que imprime el resultado de la o las expresiones que tenga como argumento pero que en realidad no devuelve nada como resultado, no hay `Out`. Si hacemos:

# %% [markdown]
# La expresi贸n se eval煤a de adentro hacia afuera, el primer `print` imprime `2`, el segundo imprime el resultado del primer `print` que es `None`:

# %%
print(print(2))

# %% [markdown]
# Quiz谩s es un poco m谩s expl铆cito si hacemos lo que sigue, que imprime 2 al evaluar el `print` y devuelve en `Out` el valor del tipo de la salida de print:

# %%
type(print(2))

# %% [markdown]
# Ok, nos estamos pasando de rosca!

# %%
print("fin")

# %%
