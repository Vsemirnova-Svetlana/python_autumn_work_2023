import re
line = '1 3 67 45 44 12 39 78 99 100 200 2 0 1000'
x=input("Введите положительное двузначное число: ")

k = x[0]
d = x[1]

res = re.findall(rf'\b\d\b|\b[0-{int(k)-1})][0-9]\b|\b{k}[0-{d}]\b',line)
print(res)


