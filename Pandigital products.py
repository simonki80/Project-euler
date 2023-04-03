# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 00:35:21 2022

@author: pc
"""
def multiplos(x): 
    mult=[]
    for i in range(1,x): 
        if x%i==0:
            mult.append(i)
    if len(mult)>=2: 
        a=mult[-1]
        b=mult[-2]
        k=str(a)+str(b)
    else: 
        k="0"
    return k

     



pandigitalNum=[]

for i in range(13,10000):
    l=str(i)
    h=multiplos(i)
    o=h+l
    if len(set(o))!=9 or o.count("0")>=1: 
        continue
    else: 
        pandigitalNum.append(o)
print(pandigitalNum)
        
    
        
        
            
            

    
    
    
    