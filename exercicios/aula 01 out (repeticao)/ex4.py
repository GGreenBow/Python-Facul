cont = 1
neg = 0
while cont <= 5:
    num=int(input('Escreva um valor: '))
    if num<0:
        print('O número %d' %num, ' é negativo')
        neg = neg + 1
    cont=cont+1
print('A quantidade de nº negativos é %d' %neg)
print('Fim do programa')
