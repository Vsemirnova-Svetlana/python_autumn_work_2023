# Программа считает количество нулей, на которые заканчивается факториал
n = int(input("Введите число: "))

factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
    i +=1
string = list(str(factorial))
new_string = string[::-1]
count = 0

for i in new_string[:]:
    if i == "0":
        count +=1
    else:
        break


print(count)

# print(string)
# print(new_string)
