# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 00:26:08 2022

@author: juans
"""
import math as mt

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

a=primos(10000)



k=1000
numbersresut=[]
while k<150000:
    primefactors=[]
    if a.count(k)==0:
        for i in a:
            if i<k/2:
                if k%i==0:
                    primefactors.append(i)
                else:
                    pass
            else: 
                pass
    if len(set(primefactors))==4:
        numbersresut.append(k)
        
    primefactors.clear()
    k=k+1
    
    
for i in numbersresut:
    a=i
    b=i+1
    c=i+2
    d=i+3
    if numbersresut.count(b)==1:
        if numbersresut.count(c)==1:
            if numbersresut.count(d)==1:
                print(a)
                print(b)
                print(c)
                print(d)
                
                

    
    
        
    
    
        