num=int(input('Digite um número entre 10 à 99: '));
if num>10 and num<99:
    result=num+(num-1)+(num+1);
    print('A soma do número lido mais o antecessor e o consecutivo é %d' %result)
else:
    print('Obedeça as instruções e insira um valor válido!')
