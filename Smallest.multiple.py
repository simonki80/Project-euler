#encontrar el numero mas pequeño que pueda ser divisible por los numeros del 2,20
numbers=[]
pronumbs=[]
for i in range (350000,450000):
    for n in range (1,21): 
        if i % n == 0: 
            numbers.append(i)
            if numbers.count(i)==20:
                pronumbs.append(i)
print(pronumbs)

        




    
    







        





    

    
        




