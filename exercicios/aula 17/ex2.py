num1=int(input('Digite o tamanho do primeiro arquivo:' ));
num2=int(input('Digite o tamanho do segundo arquivo:' ));
if num1 == num2:
    print('Os arquvios possuem mesmo tamanho')
else:
    if num1!=num2:
        print('São diferentes')
        if num1<num2:
            print('O maior arquivo é %d' %num2, 'e o menor arquivo é %d' %num1)
        else:
            print('O maior arquivo é %d' %num1, 'e o menor arquivo é %d' %num2)

