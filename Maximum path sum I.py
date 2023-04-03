# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:29:50 2022

@author: pc
"""
number="759564174782183587102004824765190123750334880277730763679965042806167092414126568340807033414872334732371694295371446525439152975114701133287773177839681757917152381714914358502729486366046889536730731669874031046298272309709873933853600423"

#ordenamiento:
    
lista=[]
pares=""
for i in number:
    pares=pares+i
    if len(pares)==2: 
        lista.append(int(pares))
        pares=""
resultlist=[]
k=1
while len(lista)!=0:
    provicional=lista[:k]
    resultlist.append(provicional)
    del lista[:k]
    k=k+1

#funcion recursiva:
    

def recursividad(matriz, fila, indice):
    a=matriz
    if fila>=len(a):
        return 0
    suma1 = (a[fila])[indice]+recursividad(a, fila+1, indice+1)
    suma2= (a[fila])[indice]+recursividad(a, fila+1, indice)
    return max(suma1, suma2)
print(recursividad(resultlist, 0, 0))




    


    
        
        
    
    
    
    
        
    

    
        



        
        
        
        
    






 
    
    
    


    


    
    



   

        
        
        
    
    


    
    
    