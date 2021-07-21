cont = 1
neg = 0
while cont <= 20:
    num=int(input('Escreva um valor: '))
    if num<0:
        print('O número %d' %num, ' é negativo')
        neg = neg + 1
    cont=cont+1
    
print('Quantidade de números negativos foi %d' %neg)
print('Fim do programa')
