num=int(input('Digite um número para calcular o fatorial: ') )
fat=1
cont=num

while cont>=1:
    fat*=cont
    cont-=1

print(fat)
