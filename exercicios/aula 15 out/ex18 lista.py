num=1
cont=1
soma=0
while cont<=100:
    alg=num%2
    if alg!=0:
        soma=somar+num
    num+=1
    cont+=1
print('%d' %soma)
