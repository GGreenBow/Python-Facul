cont2=1
S=0.0
for cont1 in range (1, 11, 1):
    cont2=cont1*cont1
    calc=float(cont1/(cont1*cont1))
    if cont1%2==0:
        S=S-calc
    else:
        S=S+calc
    cont1+=1
print('%.2f' %S)
