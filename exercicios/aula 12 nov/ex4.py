n=int(input("Digite o número: "))
ult=1
pen=1

if(n==1)or(n==2):
    print("1")
else:
    for count in range(2,n):
        result=ult+pen
        pen=ult
        ult=result
        count+=1
    print(result)
