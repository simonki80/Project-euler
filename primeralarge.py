from math import sqrt
def primelarge(n): 
    lista=[]
    for i in range(2, int(sqrt(n))):
        while n % i == 0: 
            lista.append(i)
            n=n/i     
    return lista 
print(primelarge(600851475143))


             
