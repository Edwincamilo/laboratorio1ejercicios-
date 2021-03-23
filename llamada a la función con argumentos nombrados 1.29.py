# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:15:30 2021

@author: 57314
"""

def tabla(numero,terminos=0):
    for x in range(terminos):
        va=x*numero
        print(va,",",sep="",end="")  #sep =separador
    
    print()
    
#llamdo a las variables
print("tabla del 3")
tabla(3)
print("tabla del 3 con 5 terminos")
tabla (3,5)
print("tabla del 3 con 20 terminos")
tabla(3,20)

    