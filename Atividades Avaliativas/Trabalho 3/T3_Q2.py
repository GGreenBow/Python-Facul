lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pos=0
num=0
cont=0
alt=0
for i in range (0, 10):
    cont+=1
    lista[i]=int(input(f'Digite um valor para posição {[cont]} da sua lista: '))

print ('\n',lista)

while alt>=0:
    print ('\nDeseja fazer alguma alteração na sua lista? \n [ 1 ]- Sim \n [-1 ]- Não')
    alt=int(input(''))

    if alt==1:

        pos=int(input('\nInsira uma posição que deseja: '))
        num= int(input('Insira o numero que queira adicionar à lista: '))
        pos1= pos-1

        if pos1>=0 and pos1<10 and num>=0:
            lista.insert(pos1, num)
            lista.pop(pos)
            
            print ('\n', lista)

        elif num>=0:
            print('\n Posição invalida')

    elif alt>1 or alt<-1:
        print('Opção invalida')
         
   
print('\n Programa encerrado')

