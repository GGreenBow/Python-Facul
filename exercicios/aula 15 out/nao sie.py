num=int(input('Digite um numero: '))
par=0
imp=0
while(num>0):
    if num%2==0:
        par=par+1
        print('O número %d' %num, ' é par')
    else:
        imp=imp+1
        print('O número %d' %num, ' é ímpar')
    num=int(input('Digite um numero: '))
print('O total de números pares é %d' %par, ' e ímpares é %d' %imp)
