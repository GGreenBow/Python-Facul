cont = 1
neg = 0
pos = 0
par = 0
imp = 0
while cont <= 5:
    num=int(input('Escreva um valor: '))
    rest=num%2
    if num<0:
        print('O número %d' %num, ' é negativo')
        neg = neg + 1
    elif num>0:
        print('O número %d' %num, ' é positivo')
        pos = pos + 1
    if rest == 0:
        print('O número %d' %num, ' é par')
        par = par + 1
    else:
        imp = imp + 1 
    cont=cont+1
print('A quantidade de nº positivos foram %d' %pos, 'e negativos %d' %neg, ', já a quantidade de nº pares foram %d' %par, 'e ímpares %d' %imp)
print('Fim do programa')
