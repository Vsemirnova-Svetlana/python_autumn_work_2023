n = int(input("Введите n: "))

dct={0:1,1:1}

if n==1:
    print(dct[0])
elif n==2:
    print(dct[0],dct[1])
else:
    x=0
    y=0
    for i in range(2, n+1):
        x=dct[i-2]
        y=dct[i-1]
        dct[i]=x+y

    for values in dct.values():
        print(values,end = " ")

