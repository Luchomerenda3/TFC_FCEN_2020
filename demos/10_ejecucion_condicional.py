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
# # Ejecución condicional
#
# Como una primera aplicación de la ejecución condicional construiremos una función que verifique que la función que diseñamos para ejecutar la operación XOR funciona correctamente probando que de el resultado de la tabla de verdad para cada entrada. No temos que estamos pasando como argumento a la función otra función.

# %%
def prueba_xor(func):
    falla = True # Inicializamos esta variable asumiendo que falla
    if func(False,False) != False:
        print("FALLA!!!!!")
    elif func(False,True) != True:
        print("FALLA!!!!!")
    elif func(True,False) != True:
        print("FALLA!!!!!")
    elif func(True,True) != False:
        print("FALLA!!!!!")
    else:
        falla = False
        print("Funciona BIEN.")
    return falla


# %%
def xor(A,B):
    return ((not A) and B) or (A and (not B)) 


# %%
def mala(A,B):
    return ((not A) and B) or (A and B)


# %%
prueba_xor(xor)

# %%
prueba_xor(mala)


# %% [markdown]
# Pero qué pasa si queremos saber dónde falla, podemos hacer lo que sigue por ejemplo:

# %%
def prueba_xor_v2(func):
    falla = True
    if func(False,False) != False:
        print("FALLA en 1!!!!!")
    elif func(False,True) != True:
        print("FALLA en 2!!!!!")
    elif func(True,False) != True:
        print("FALLA en 3!!!!!")
    elif func(True,True) != False:
        print("FALLA en 4!!!!!")
    else:
        falla = False
        print("Funciona BIEN.")
    return falla


# %%
prueba_xor_v2(mala)

# %% [markdown]
# Pero notemos que la función `mala` también falla en el caso 4 pero nuestro probador no detecta esa falla:

# %%
mala(True,True)


# %% [markdown]
# Si recordamos el diagrama de flujo del conjunto `if elif else` vemos que la segunda prueba 4 nunca llega a ejecutarse porque alcanza conque **una** de las condiciones sea cierta para que se ejecuten las sentencias de ese bloque y el programa salga de la declaración `if`. Para este caso entonces, si queremos hacer todas y cada una de las pruebas necesitamos una serie de `if` independientes cambiando la lógica de la siguenete manera:

# %%
def prueba_xor_v3(func):
    falla = False
    if func(False,False) != False:
        print("FALLA en 1!!!!!")
        falla = True
    if func(False,True) != True:
        print("FALLA en 2!!!!!")
        falla = True
    if func(True,False) != True:
        print("FALLA en 3!!!!!")
        falla = True
    if func(True,True) != False:
        print("FALLA en 4!!!!!")
        falla = True
    if falla:
        print("Funciona MAL.")
    else:
        falla = False
        print("Funciona BIEN.")
    return falla


# %%
prueba_xor_v3(xor)

# %%
prueba_xor_v3(mala)

# %%
