# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 00:20:04 2022

@author: pc
"""
import numpy as np


def path (x): 
    a=np.zeros((x,x))
    for i in range (0,x):
        a[0,i]=1
        a[i,0]=1
    k=1
    while k<x:
        for i in range(1,x):
            a[k,i]=a[k-1,i]+a[k,i-1]
        k=k+1
    return print(a[x-1,x-1])
path(21)

    

    
   
        

    




 
    
    