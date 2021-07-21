print('Pense em número para que o programa possa adivinhar')
maxi=int(input('Seu número está entre 0 e qual outro número? \n'))
mini=0
result=0
while result!=1:
    meio=(mini+maxi)/2
    perg=input('Seu número é maior(+), menor(-) ou igual(=) a: %d \n' %meio)
    if meio>0:
        if perg=='+':
            mini=meio
        elif perg=='-':
            maxi=meio
        elif perg=='=':
            print('Adivinhei seu número!')
            result=1
        else:
            print('ERRO')
    else:
        print('ERRO')
        
