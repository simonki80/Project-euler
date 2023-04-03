pares=[]
def fibS(n):
    a=0
    b=1
    for k in range(n):
        f=a+b
        a=b
        b=f
    return b
for x in range(34):
   if fibS(x) % 2 == 0: 
       pares.append(fibS(x))
print(sum(pares))
       








  





        
    



    