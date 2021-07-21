num=[0]*5
i=0
while (i<5):
    num[i]=int(input('Digite um valor: '))
    i=i+1
impar=num[i]%2
i=0
if impar!=0:
    result=impar
print(result)
