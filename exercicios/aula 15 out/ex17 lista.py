cont=1
num=int(input('Entre com um valor'))
#maior=0
maior=num
while cont<=19:
    num=int(input('Entre com um valor'))
    if num>maior:
        maior=num
    cont+=1
print('O maior valor é %d' %num)
