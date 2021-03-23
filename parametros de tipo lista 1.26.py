# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:11:24 2021

@author: 57314
"""

#Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y 
#un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.


def multiplicar(lista,valor):
    for x in range(len(lista)):
        multi= lista[x] * valor
        print(multi)



# Bloque principal 




lista =[3,7,8,10,2]
print("lista original:")
print(lista)
print("lista de elementos multiplicados por 3")
multiplicar(lista,3)
