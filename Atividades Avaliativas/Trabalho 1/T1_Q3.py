num1=int(input('Digite um número de quatro dígitos: '));
num2=int(input('Digite um número de dois dígitos: '));

'''num1'''
mil=int(num1/1000);
cen=int(num1%1000);
cen2=int(cen/100);
dez=int(cen%100);
dez2=int(dez/10);
uni=dez%10;

'''num1'''
dez3=int(num2/10);
uni3=num2%10;
    


if num1>999 and num1<10000 and num2>9 and num2<100:
    
    if dez3==dez2 and uni3==uni:
        print('Encaixa')
    else:
        print('Não encaixa')
       
else:
    print('Dados de entrada inadequados, siga as instruções!')





