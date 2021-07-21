num=int(input('Digite o primeiro número: '));
num2=int(input('Digite o segundo número: '));
num3=int(input('Digite o terceiro número: '));
if num!=num2 and num2!=num3 and num!=num3:
    if num<num2 and num2<num3:
        print(num, num2, num3)
    else:
        if num<num2 and num3<num2:
            print(num, num3, num2)
        else:
            if num2<num and num<num3:
                print(num2, num, num3)
            else:
                if num2<num and num3<num:
                    print(num2, num3, num)
                else:
                    if num3<num and num<num2:
                        print(num3, num, num2)
                    else:
                        if num3<num and num2<num:
                            print(num3, num2, num)
else:
    print('Os valores devem ser diferentes')
