# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:23:33 2021

@author: 57314
"""

def cantidad_mayores18(edad,*edades):
    cant=0
    if edad>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant

#llamada a la variable
print("cantidad de personas mayores de 18 años son:",cantidad_mayores18(23,23,45,67,34,5,7,23))
