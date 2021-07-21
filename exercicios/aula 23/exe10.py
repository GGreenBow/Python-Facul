resp = input('Deseja usar o programa? \n')
while resp == 'sim':
    alt=float(input('Digite sua altura: '));
    sex=int(input('Digite 1 se você for do sexo masculino ou digite 2 se você for do sexo feminino: '));
    if sex==1:
        peso=(62.1*alt)-44.7;
        print('Seu peso ideal aproximadamente é: %d' %peso)
    else:
        if sex==2:
            peso=(72.7*alt)-58;
            print('Seu peso ideal aproximadamente é: %d' %peso)
    resp=input('Deseja continuar o programa? \n')
print('Fim do programa')
