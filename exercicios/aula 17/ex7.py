num1=int(input('Digite seu numero (3 digitos): '))

cen=int(num1/100);
dez=int(num1%100);
dez2=int(dez/10);
uni= dez%10;

if num1==((uni*100)+(dez2*10)+cen):
    print('O seu numero é um palindromo')
else:
    print('o seu numero nao é um palindromo')
    

        
