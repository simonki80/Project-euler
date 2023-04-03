# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:52:11 2022

@author: pc
"""

#Longest Collatz sequence

#sequence:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)



a=1000000
def reduccion(x):
    contador=0
    while x != 1:
        if x%2==0:
            x=x/2
            contador=contador+1
        else: 
            x=3*x+1 
            contador=contador+1
    return contador+1
lista1=[]
resultados=[]
for i in range(2,a):
    lista1.append(i)
    resultados.append(reduccion(i))
mayor=resultados.index(max(resultados))
resultado=lista1[mayor]
print(resultado)
    
    
    