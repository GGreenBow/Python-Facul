num=int(input ('Digite um numero inteiro: '))
soma=0

for i in range(1,num):
    div=num%i
    if div==0:
        soma+=i
        i+=1
        
if soma==num:
    print('O número é perfeito, pois %d' %num, ' = %d' %soma)

else:
    print('O número não é perfeito, pois %d' %num, ' != %d' %soma)
