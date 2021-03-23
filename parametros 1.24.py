# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:58:46 2021

@author: 57314
"""

#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida

def f_ordenar(v1,v2,v3):
    if v1<v2 and v2<v3:
         if v1<v3:
             print("v1,v2,v3")
         else:
             print("v1,v3,v2")
    else:
        if v2<v3:
            if v1<v3:
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if v1<v2:
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)
                
                
def cargar():
    num1=int(input("ingrese primer valor:"))
    num2=int(input("ingrese segundo valor:"))
    num3=int(input("ingrese tercer valor:"))
    f_ordenar(num1,num2,num3)
             
             
             
             
cargar()

