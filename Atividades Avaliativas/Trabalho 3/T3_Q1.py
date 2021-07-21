listA=[]
listB=[]

for i in range(5):
    listA.append(int(input('Digite um valor para lista A: ')))
print(listA)

for i in range(5):
    listB.append(int(input('Digite um valor para lista B: ')))
print(listB)

j=4

for i in range(5):
    aux = listA[i]
    listA[i]=listB[j]
    listB[j]=aux    
    j-=1

print('\n')
print(listA)
print(listB)
