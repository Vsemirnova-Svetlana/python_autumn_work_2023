x = int(input("Введите x: "))
y = int(input("Введите y: "))

if y == 0:
    y = int(input("На ноль делить нельзя, введите другое число: "))

num_sum = x + y
difference = x - y
multiply = x * y
division = x/y
int_division = x//y

max_num = num_sum
if difference > max_num:
    max_num= difference

if multiply > max_num:
    max_num = multiply

if division > max_num:
    max_num = division

if int_division > max_num:
    max_num = int_division

print("Наибольшее из чисел: ",max_num)
