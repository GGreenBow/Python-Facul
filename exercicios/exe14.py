num1=int(input('Digite o primeiro número: '));
num2=int(input('Digite o segundo número: '));
print('Antes %d' %num1, 'e %d' %num2);
num1, num2 = num2, num1;
print('Depois %d' %num1, 'e %d' %num2);
