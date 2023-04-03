# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 00:53:21 2022

@author: juans
"""


def primos(x):
    numeros = list(range(2,x+1))
    d=0
    while numeros[d]**2 <= x:
        for n in numeros:
            if n != numeros[d]:
              if n % numeros[d] == 0:
                numeros.remove(n)
        d += 1
    return numeros

a=primos(9999)
k=0
while k< 168:
    a.pop(0)
    k=k+1


listacompleta=[]
semejantes=[]
k=0
while k<len(a): 
    number=a[k]
    semejantes.append(number)
    cadenanumero=str(number)
    for i in a:
        iteracion=str(i)
        print(iteracion)
        print(cadenanumero)
        if set(iteracion+cadenanumero)==set(iteracion):
            semejantes.append(i)

    listacompleta.append(semejantes)
    semejantes.clear()
    k=k+1
print(listacompleta)
    
    
        

