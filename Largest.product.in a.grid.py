# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:32:04 2022

@author: pc
"""
import numpy as np
lista=np.array([8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7 ,78 ,52 ,12 ,50 ,77 ,91 ,8, 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0, 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65, 52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91, 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80, 24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50, 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70, 67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21, 24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95, 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92, 16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57, 86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58, 19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40, 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66, 88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36, 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16, 20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54, 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48,]).reshape((20,20))

resultados=[]
for i in range(0,20): 
    a=lista[i,:]
    while len(a)>3: 
        multiplicacion=1
        primeros4=a[:4]
        #print(primeros4)
        for x in primeros4: 
            multiplicacion=multiplicacion*x
        resultados.append(multiplicacion)
        a = np.delete(a,0)
#print(max(resultados))


resultadosverticales=[]
for i in range(0,20): 
    b=lista[:,i]
    while len(b)>3: 
        pr1meros4=b[:4]
        #print(pr1meros4)
        multiplicacion1=1
        for x in pr1meros4:     
            multiplicacion1=multiplicacion1*x
        resultadosverticales.append(multiplicacion1)
        b = np.delete(b,0)
#print(max(resultadosverticales))


resultadodiagonal=[]
k=0
while k<20:
    for i in range(0,20):
        numeros4=[]
        try:
            h=lista[i,i+k]
            numeros4.append(h)
        except IndexError:
            continue
        try:
            a=lista[i+1,i+1+k]
            numeros4.append(a)
        except IndexError:
            continue
        try:
            b=lista[i+2,i+2+k]
            numeros4.append(b)
        except IndexError:
            continue
        try:
            c=lista[i+3,i+3+k]
            numeros4.append(c)
        except IndexError:
            continue
        
        if len(numeros4)==4: 
            multi=h*a*b*c
            resultadodiagonal.append(multi)
            numeros4.clear()
        else:
            continue
    k=k+1
resultadodiagonal2=[]
s=0
while s<20:
    for i in range(0,20):
        numeros4=[]
        try:
            h=lista[s+i,i]
            numeros4.append(h)
        except IndexError:
            continue
        try:
            a=lista[s+i+1,i+1]
            numeros4.append(a)
        except IndexError:
            continue
        try:
            b=lista[s+i+2,i+2]
            numeros4.append(b)
        except IndexError:
            continue
        try:
            c=lista[s+i+3,i+3]
            numeros4.append(c)
        except IndexError:
            continue
        
        #multiplicacion
        if len(numeros4)==4: 
            multi=h*a*b*c
            resultadodiagonal2.append(multi)
            numeros4.clear()
        else:
            continue
    s=s+1
resultadodiagonal.extend(resultadodiagonal2)
#print(max(resultadodiagonal))

resultadodiagona3=[]
k=0
while k<20: 
    for i in range(0,20):
        numeros4=[]
        try:
            h=lista[i,19-i+k]
            numeros4.append(h)
        except IndexError:
            continue
        try:
            a=lista[i+1,19-1-i+k]
            numeros4.append(a)
        except IndexError:
            continue
        try:
            b=lista[i+2,19-2-i+k]
            numeros4.append(b)
        except IndexError:
            continue
        try:
            c=lista[i+3,19-3-i+k]
            numeros4.append(c)
        except IndexError:
            continue
        #print(numeros4)
        if len(numeros4)==4: 
            multi=h*a*b*c
            resultadodiagona3.append(multi)
            numeros4.clear()
        else:
            continue
    k=k+1
resultadodiagonal4=[]
j=0
while j<20: 
    for i in range(0,20):
        numeros14=[]
        try:
            h=lista[i,19-i-j]
            numeros14.append(h)
        except IndexError:
            continue
        try:
            a=lista[i+1,19-1-i-j]
            numeros14.append(a)
        except IndexError:
            continue
        try:
            b=lista[i+2,19-2-i-j]
            numeros14.append(b)
        except IndexError:
            continue
        try:
            c=lista[i+3,19-3-i-j]
            numeros14.append(c)
        except IndexError:
            continue
        print(numeros14)
        if len(numeros14)==4: 
            multi=h*a*b*c
            resultadodiagonal4.append(multi)
            numeros14.clear()
        else:
            continue
    j=j+1










    
    
    
    
    
            
            
        
        
        
    
    