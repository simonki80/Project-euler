Squarefirst100n=[]
N100ds=[]
for i in range(1,101):
    i=i*i
    N100ds.append(i)
for x in range (1,101): 
    Squarefirst100n.append(x)
print(int(sum(Squarefirst100n))*int(sum(Squarefirst100n)) - int(sum(N100ds)))

