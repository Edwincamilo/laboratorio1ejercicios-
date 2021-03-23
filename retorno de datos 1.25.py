# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:31:19 2021

@author: 57314
"""

# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos


def retornar_promedio(v1,v2,v3):
    promedio=(v1,v2,v3)/3
    return promedio

#
valor1=int(input("ingrese primer valor:"))
valor2=int(input("ingrese segundo valor:"))
valor3=int(input("ingrese tercer valor:"))
print("promedio de los tres numeros ingresados:",retornar_promedio(valor1,valor2,valor3))
