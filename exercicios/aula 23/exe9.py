num=int(input('Digite um número: '));
print('Intervalos possíveis: ')
print('Intervalos A: de 0 à 25 ')
print('Intervalos B: de 26 à 50 ')
print('Intervalos C: de 51 à 75 ')
print('Intervalos D: entre 75 e 100 ')
if num>=0 and num<=25:
    print('O número %d' %num, 'está no intervalo A')
else:
    if num>=26 and num<=50:
        print('O número %d' %num, 'está no intervalo B')
    else:
        if num>=51 and num<=75:
            print('O número %d' %num, 'está no intervalo C')
        else:
            if num>75 and num<100:
                print('O número %d' %num, 'está no intervalo D')
            else:
                print('Seu número está fora de qualquer intervalo')
