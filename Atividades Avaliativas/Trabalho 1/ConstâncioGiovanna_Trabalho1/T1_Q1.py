num1=int(input('Digite o primeiro número: '));
num2=int(input('Digite o segundo número: '));
ope=input('Qual operação você deseja fazer? \nDigite + para somar \nDigite - para subtrair \nDigite * para multiplicar \nDigite / para dividir \nDigite % para ver o resto da divisão \n')

if ope=='+' or ope=='-' or ope=='*' or ope=='/':
    if ope=='+':
        result=num1+num2;
        print('A soma é igual a %d' %result)
    elif ope=='-':
        result=num1-num2;
        print('A subtração é igual a %d' %result)
    elif ope=='*':
        result=num1*num2;
        print('A multiplicação é igual a %d' %result)
    elif ope=='/':
        result=num1/num2;
        print('A divisão é igual a %d' %result)
    elif ope=='%':
        result=num1%num2;
        print('A divisão é igual a %d' %result)
    soma=num1+num2;
    soma+=10;
    sub=num1-num2;
    sub-=5;
    print('A soma do seus números mais 10 é: %d' %soma, ' e a subtração do seus números menos 5 é: %d' %sub)
else:
    print('Escolha uma operação válida.')

