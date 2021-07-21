custo = int (input ('Digite o custo de fábrica do carro: '));
distri = custo * 32 / 100;
impos = custo * 41 / 100;
result = custo + distri + impos;

print ('O custo é igual a %d' %result);
