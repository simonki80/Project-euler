# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 00:48:00 2022

@author: juans
"""

a=[]
for i in range(1234567890,9999999999):
    x=str(i)
    r=set(x)
    if len(r)==10:
        a.append(i)
    else:
        continue
print(a)
        
        