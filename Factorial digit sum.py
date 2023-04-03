# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:57:00 2022

@author: pc
"""

n=100
a=1
for i in range(1,100+1): 
    a=a*i
numero=str(a)
lista=[]
for e in numero: 
    lista.append(int(e))
print(sum(lista))
    

    
    