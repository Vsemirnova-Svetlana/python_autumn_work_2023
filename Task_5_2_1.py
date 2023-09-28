n = int(input("Введите n: "))
lst=[]

for i in range(1,n+1):
    if n%i == 0:
        i=str(i)
        lst.append(i)

g = ' '.join(lst)
print(g)
