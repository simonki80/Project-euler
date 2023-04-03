# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 23:31:26 2022

@author: pc
"""

def palindromic(x): 
    a=str(x)
    number=""
    for i in range(1,len(a)+1): 
        number=number+a[-i]
    if int(a)==int(number): 
        return x
    else:
        return 75
 
def binary(x):
    bi=bin(x)[2:]
    if palindromic(bi)==bi: 
        return bi
    else: 
        return 15

listaP=[]
for i in range(1,1000000): 
    listaP.append(palindromic(i))
    
Resultado=[]
for i in set(listaP): 
    b=binary(i)
    if b==15:
        continue
    else: 
        Resultado.append(i)

print(sum(Resultado))
        


    
        
        
    
    