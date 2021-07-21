num=int(input ("Digite um número inteiro: \n"))
num2=int(input ("Digite outro número inteiro: \n"))
soma=0
soma2=0
for i in range(1,num):
    div=num%i    
    if div==0:
        soma+=i

for i in range(1,num2):
    div=num2%i
    if div==0:
        soma2+=i

if soma==num2 and soma2==num:
    print('1')
else:
    print('0')
    
        
