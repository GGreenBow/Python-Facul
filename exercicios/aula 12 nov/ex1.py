num=int(input('Digite uma nota entre 0 e 10: '))
while num<0 or num>10:
    print('Valor Inválido!')
    num=int(input('Digite uma nota entre 0 e 10: '))
if num>=6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
