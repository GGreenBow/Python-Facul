cont = 1
neg = 0
pos = 0
while cont <= 100:
    num=int(input('Escreva um valor: '))
    if num<0:
        print('O número %d' %num, ' é negativo')
        neg = neg + 1
    elif num>0:
        print('O número %d' %num, ' é positivo')
        pos = pos + 1
    cont=cont+1
print('A quantidade de nº positovos foram %d' %pos, ' e negativos %d' %neg)
print('Fim do programa')
