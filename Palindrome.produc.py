palindromosmultiplos3cifras=[]
c=998001
for i in range(int(c/2), c+1):
    b=(str(i)[:: - 1])
    if i==int(b):
        multiplos=[]
        for x in range(100 , 999):
            if i % x==0:
                multiplos.append(x)
                if len(multiplos)>2: 
                    z=(multiplos[-1])
                    y=(multiplos[-2])
                    if int(z)*int(y)==i: 
                        palindromosmultiplos3cifras.append(i)
                else:
                    continue
print(palindromosmultiplos3cifras[0])

