# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 21:19:39 2022

@author: pc
"""
totalnums=[]
deficit=[]
abundant=[]
perfectn=[6, 28, 496, 8128]

n=1
divisors=[]
while n<=28123:
    totalnums.append(n)
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    else:
        abundant.append(n)
    divisors.clear()
    n=n+1
for i in perfectn: 
    abundant.remove(i)

everysums=[]
k=0
while k<=len(abundant)-1:
    s1=abundant[k]
    for i in abundant:
        if s1==i:
            pass
        else: 
            everysums.append(s1+i)
    k=k+1

for i in everysums: 
    totalnums.remove(i)    
print(sum(totalnums))

    





        
            
        
            