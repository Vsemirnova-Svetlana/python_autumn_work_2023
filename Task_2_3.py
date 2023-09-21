import math
n = int(input("Введите число n: "))

factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
    # i +=1

print(f"{n}! = {factorial}")

# Проверка с помощью модуля math:
# new_f = math.factorial(n)
# print(new_f)