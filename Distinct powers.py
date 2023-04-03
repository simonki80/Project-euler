# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 00:41:48 2022

@author: pc
"""
lista=[]
a=2
while a<=100: 
    for i in range(2,101):
        b=a**i
        lista.append(b)
    a=a+1
resultado=set(lista)
print(len(resultado))
        