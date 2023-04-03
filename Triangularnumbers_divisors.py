# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:37:37 2022

@author: pc
"""

#numeros triangulares 
resultado=0
a=1
resultadosreales=[]
while resultado<1000000: 
    resultado=resultado+a
    a=a+1
    provisional=[]
    for x in range(1,resultado+1):
        if resultado%x==0:
            provisional.append(x)
    if len(provisional)==500:
        resultadosreales.append(resultado)
    else: 
        provisional.clear()
print(resultadosreales)
                








        
            

            
            


                
            
                
                

            