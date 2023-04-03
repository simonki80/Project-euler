# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:09:22 2022

@author: pc
"""
necesary_words=["one","two","three","four","five","six","seven","eight","nine","teen","eleven","twelve","thirteen","fourteen","fifteen","twenty","thirty","forty","fifty","sixty","seventy","eigthty","ninety","hundred"]
def palabras_numeros(x): 
    a=str(x)
    contador=0
    for i in a: 
        contador=contador+1
    return contador
#list1
numbers_letters=[0]
for i in necesary_words:
    numbers_letters.append(palabras_numeros(i))
#list2
listh=[]
for i in range(0,16): 
    listh.append(i)
for i in range(20,101): 
    if i%10==0: 
        listh.append(i)
dic=dict(zip(listh,numbers_letters))
result=[]
k=1
while k<99+1:
    if k<(15)+1: 
        a=dic[k]
        result.append(a)
        k=k+1
    else: 
        number=[]
        for x in str(k): 
            number.append(x) 
        if len(number)==2: 
            number1=number
            number1.insert(1, 0)
            p1=number1[0]
            p2=number1[1]
            Ldecenas=str(p1)+str(p2)
            ndecenas=int(Ldecenas)
            a=dic[ndecenas]
            b=number1[-1]
            c=dic[int(b)]
            g=int(a)+int(b)
            result.append(g)
            k=k+1
k=101
while k<999+1:
    number=[]
    for x in str(k): 
        number.append(x)
    l=dic[int(number[0])]
    number.pop(0)
    k1=int(str(number[0]+str(number[1])))
    if k1<(15)+1: 
        a=dic[k1]+11+l
        result.append(a)
        k=k+1
    else: 
        number1=[]
        for x in str(k1): 
            number1.append(x) 
        if len(number1)==2: 
            number2=number1
            number2.insert(1, 0)
            p1=number2[0]
            p2=number2[1]
            Ldecenas=str(p1)+str(p2)
            ndecenas=int(Ldecenas)
            a=dic[ndecenas]
            b=number2[-1]
            c=dic[int(b)]
            g=int(a)+int(b)+l+9
            result.append(g)
            k=k+1
h=sum(result)
print(h)
print(palabras_numeros("ninehundredandnine"))
    
    
       

#hay que quitarle 9 veces 3 o sea 27 y añadimos el 100 
            
            

        
        
        
        
        
    
    


    
        
        
    
    














    


        
                
                
            
        
  
        
         
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
        
                
            
        
   







    
        
        





    
    
    
    
  
    
    










