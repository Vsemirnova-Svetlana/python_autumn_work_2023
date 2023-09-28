n = int(input("Введите n: "))
lst =[]
lst2=[]

# список всех делителей, кроме 1
for i in range(2,n+1):
    if n%i == 0:
        lst.append(i)
# print(lst)

#список только простых делителей
for j in range(len(lst)):
    x = lst[j]
    for l in range(2, x):
        if x%l == 0: break
    else: lst2.append(x)
# print(lst2)

dct = {}
for j in range(len(lst)):
    x = lst[j]
    for i in range(len(lst2)+1):
        y=lst[i]
        for l in range(1,n):
            if y**l == x:
                if y in lst2:
                    dct[y]=l

# print(dct)
for i,j in dct.items():
    print(i,' - ',j)





