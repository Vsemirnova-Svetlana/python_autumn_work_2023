n = int(input("Введите n: "))

dct ={1:[1]}
if n == 1:
    for values in dct.values():
        num = list(map(str,values))
        print(' '.join(num))

else:
    for i in range(2,n+1):
        dct[i]=[0]*(i-2)
        dct[i].insert(0,1)
        dct[i].append(1)

    line = 3
    j = 1
    d = 0
    while line<=n:
        for i in range(line,n+1):
            dct[i][j]=dct[i-1][d]+dct[i-1][j]
            x=len(dct[i])-2
            dct[i][x]=dct[i-1][d]+dct[i-1][j]

        j +=1
        d +=1
        x -=1
        line += 1

    for values in dct.values():
        nums = list(map(str,values))
        print(' '.join(nums))
