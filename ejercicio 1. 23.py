# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:31:24 2021

@author: 57314
"""

#Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el 
#cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.

def f_calcular_cuadrado ():
    valor =int(input("ingrese un numero entero:"))
    cuadrado= valor*valor
    print("el cuadrado es: ",cuadrado)
    
    

def f_calcular_producto():
    valor1=int(input("ingrese primer numero entero:"))
    valor2=int(input("ingrese segundo numero entero:"))
    producto= valor1 * valor2
    print("el producto es :",producto)
    
    
    
    
    
    
#llamada a la funcion 
    
    
f_calcular_cuadrado ()
f_calcular_producto ()