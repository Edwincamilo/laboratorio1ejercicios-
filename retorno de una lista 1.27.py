# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:24:34 2021

@author: 57314
"""

#En una empresa se almacenaron los sueldos de 10 personas.
#Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#1) Carga de los sueldos en una lista.
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos.
#5) Mostrar todos los sueldos que están por debajo del promedio.



def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        sueldo=int(input("ingrese el sueldo")
        sueldos.append(sueldo)
    return sueldos 

def imprimir_sueldos(sueldos):
    print("lista de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])
        
        
def sueldos_mayor4000(sueldos):
    cant=0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            cant=cant+1
    print("cantidad de empleados con un sueldo mayor a 4000", cant)
    
    
def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma=suma+sueldos[x]
    promedio=suma//10
    return promedio

def sueldos_bajos(sueldos):
    pro=promedio(sueldos)
    print("sueldos inferiores al promedio",pro)
    print("sueldos inferiores al promedio")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])
    
    
    
    
    
#bloque principal
sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor4000(sueldos)
sueldos_bajos(sueldos)
    
    
    
    


    