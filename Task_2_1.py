n = int(input("Введите n: "))

result = 0
for i in range(1,10):
    result = i * n
    print(f"{i} x {n} = {result}")