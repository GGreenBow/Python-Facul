nume=int(input('Digite um valor inteiro maior que 0: '))
if nume>0:
    den=1
    num=1
    while num<=nume:
        print(' %d/%d '%(num,den), end='')
        num+=1
        den+=2
else:
    print('Valor Inválido')
    
