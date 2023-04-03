# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:07:58 2022

@author: pc
"""

def factorial(x): 
    multiplicacion=1
    for i in range(1,x+1):
        multiplicacion=multiplicacion*i
    return multiplicacion

#hagamoslo hasta 200 y vemos a ver is hay algo que no diga algo mas: 

    
curiusNums=[]
for i in range(145,362880+100000): 
    a=str(i)
    suma=[]
    for x in a: 
        suma.append(factorial(int(x)))
    if sum(suma)==i: 
        curiusNums.append(i)
        suma.clear()
    else: 
        suma.clear()
        continue

print(sum(curiusNums))
        
        