'''Sistema para acréscimo de nota
Conforme combinado com os estudantes:
-Aluno com nota azul no trabalho recebe um ponto na média
-Aluno com nota vermelha no trabalho perde 0,5 ponto na prova mensal
-Com a média azul sendo par o aluno recebe uma caneta azul de prêmio,
caso seja ímpar recebe uma caneta preta.'''

print('Sistema para acréscimo de nota')
p1=float(input('Entre com a nota da prova mensal: '));
p2=float(input('Entre com a nota da prova semestral: '));
trab=float(input('Entre com a nota do trabalho: '));

media=((p1*3.0)+(p2*4.5)+(trab*2.5))/10
premio=media%2.00

if p1>=0 and p1<=10.00 and p2>=0 and p2<=10.00 and trab>=0 and trab<=10.00:
    if trab>=6.00 and media!=10.00:
        media+=1    
        if media>=10:
            media=10
        print('A média do aluno é: %.2f' %media)
        if media>=6.00:
                if premio==0:
                   print('Aluno ganha caneta azul')
                else:
                    print('Aluno ganha caneta preta')
        else:
            print('Aluno não ganha prêmio')
    elif trab<=6.00:
        p1=p1-0.5
        print('A média do aluno é: %.2f' %media)
        if media>=6.00:
            if premio==0:
                print('Aluno ganha caneta azul')
            else:
                print('Aluno ganha caneta preta')
        else:
            print('Aluno não ganha prêmio')
else:
    print('Os valores das notas são inválidos!')


                 



    
