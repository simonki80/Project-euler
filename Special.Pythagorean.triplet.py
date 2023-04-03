lista=[]
for i in range (1,1000): 
    for x in range (1, 1000): 
        for k in range(1,1000):
            if x > k < i:
                if x**2+k**2==i**2:
                    if x+k+i==1000: 
                        print(x)
                        print(k)
                        print(i)
print(lista)

