# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 23:20:08 2022

@author: pc
"""
lista=[]
resta=1000
a=1001*1001
b=a-resta
c=b-resta
d=c-resta
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
while a > 1: 
    a=d-resta
    lista.append(a)
    resta=resta-2
    b=a-resta
    lista.append(b)
    c=b-resta
    lista.append(c)
    d=c-resta
    lista.append(d)
    
resultado=set(lista)
print(sum(resultado))
