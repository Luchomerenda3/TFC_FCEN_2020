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
# # Operaciones lógicas
#
# Los ejercicios de esta sección tienen comoo objetivo familiarizarnos con el uso de las variables lógicas o Booleanas y las distintas operaciones que pueden realizarse utilizando la composición de los operadores existentes en python junto con otros que hayamos definido.

# %% [markdown]
# ## Ejercicio 1
#
# Este es un poco largo...
#
# Buscar como e implementar funciones para cada una de las operaciones lógicas NAND, NOR, XNOR usando combinaciones de los operadores lógicos definidos en el lenguaje Python: `and`, `or` y `not`.  Probar que producen el resultado correcto para cada posible par de entradas.
#
# **NO UTILIZAR CONDICIONALES**

# %%
def NAND(X,Y):
    return not (X and Y)


# %%
NAND(False,False) == True

# %%
NAND(False,True) == True

# %%
NAND(True,False) == True

# %%
NAND(True,True) == False


# %%
def NOR(X,Y):
    return not (X or Y)


# %%
NOR(False,False) == True

# %%
NOR(False,True) == False

# %%
NOR(True,False) == False

# %%
NOR(True,True) == False


# %%
def XNOR(X,Y):
    return (X or (not Y)) and ((not X) or Y)


# %%
XNOR(False,False) == True

# %%
XNOR(False,True) == False

# %%
XNOR(True,False) == False

# %%
XNOR(True,True) == True


# %% [markdown]
# Los ejercicios que siguen son más complicados (bastante) y pueden no hacerse en una primera entrega (o en ninguna...).
#
# ## Ejercicio 2 
#
# Implementar (y verificar) una función que funcione como semi sumador componiendo las operaciones lógicas definidas en el ejercicio 1.

# %%
def XOR(X,Y):
    return ((not X) and Y) or (X and (not Y)) 


# %%
def semi_sumador(X,Y):
    return XOR(X,Y),X and Y


# %%
def semi_sumador_b(X,Y):
    return NAND(NAND(X,NAND(X,Y)),NAND(NAND(X,Y),Y)),NAND(NAND(X,Y),NAND(X,Y))


# %%
semi_sumador_b(False,False) == (False,False)

# %%
semi_sumador_b(True,False) == (True,False)

# %%
semi_sumador_b(False,True) == (True,False)

# %%
semi_sumador_b(True,True) == (False,True)


# %% [markdown]
# ## Ejercicio 3
#
# Implementar (y verificar) una función que funcione como sumador completo de un bit con acarreo componiendo las operaciones lógicas definidas en el ejercicio 1.

# %%
def sumador_un_bit(A,B,C):
    return XOR(XOR(A,B),C),(XOR(A,B) and C) or (A and B)


# %%
sumador_un_bit(False,False,False) # 0 + 0 + 0 = 0 y acarreo 0

# %%
sumador_un_bit(False,False,True) # 0 + 0 + 1 = 1 y acarreo 0

# %%
sumador_un_bit(False,True,False) # 1 + 0 + 0 = 1 y acarreo = 0

# %%
sumador_un_bit(False,True,True) # 0 + 1 + 1 = 0 y acarreo 1

# %%
sumador_un_bit(True,False,False) # 1 + 0 + 0 = 1 y acarreo 0

# %%
sumador_un_bit(True,False,True) # 1 + 0 + 1 = 0 y acarreo 1

# %%
sumador_un_bit(True,True,False) # 1 + 1 + 0 = 0 y acarreo 1

# %%
sumador_un_bit(True,True,True) # 1 + 1 + 1 = 1 y acarreo 1


# %% [markdown]
# ## Ejercicio 4
#
# Implementar (y verificar) un sumador de números binarios de tres dígitos componiendo sumadores completos con acarreo.

# %%
def ss(A,B,C):
    return XOR(XOR(A,B),C)
def sa(A,B,C):
    return (XOR(A,B) and C) or (A and B)


# %%
def sf(a1,a2,a3,b1,b2,b3):
    return ss(a1,a2,sa(a2,b2,sa(a3,b3,False))),ss(a2,b2,sa(a3,b3,False)),ss(a3,b3,False)


# %%
sf(False,False,True,False,False,False) # 1 + 0 = 1

# %%
sf(False,False,True,False,False,True) # 1 + 1 = 2

# %%
sf(True,True,True,False,True,False) # 7 + 2 = 9

# %%
