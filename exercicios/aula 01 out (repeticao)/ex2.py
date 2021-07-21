resp = input('Deseja usar o programa? \n')
while resp == 'sim':
    cont = 1
    while cont<=100:
        result = 13 * cont;
        print(result)
        cont=cont+1
    resp('Deseja continuar o programa? \n')
print('Fim do programa')
    
