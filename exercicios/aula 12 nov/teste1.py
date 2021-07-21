'''num=int(input ("Digite um número inteiro: \n"))
num2=int(input ("Digite outro número inteiro: \n"))'''
resultado = []

for n in range(0,5):
    soma1=0
    soma2=0
    resultado.append([])
    num1=int(input('Digite o primeiro número: '))
    num2=int(input('Digite o segundo número: '))
    
    for i in range (1, num1):
        div1 = num1%i
        if div1 == 0:
            soma1+=i

    for i in range (1, num2):
        div2 = num2%i
        if div2 == 0:
            soma2+=i

    if soma2 == num1 and soma1 == num2:
        resultado[n].append('1')
      
    else:
        resultado[n].append('0')

    

print (resultado)
