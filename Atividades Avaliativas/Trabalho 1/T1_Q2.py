num=int(input('Digite o número de dois dígitos: '));
dez=int(num/10);
uni=num%10;
som=dez+uni;

if num>10 and num<99:
    if som>=10:
        result=(dez*1000)+(som*10)+uni;
        print('A estrutura DSU é igual a %d' %result)
    else:
        result2=(dez*100)+(som*10)+uni;
        print('A estrutura DSU é igual a %d' %result2)
else:
    print('Valor de entrada não possui 2 dígitos.')
