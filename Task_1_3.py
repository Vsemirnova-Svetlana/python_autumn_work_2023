x = int(input("Введите x: "))
y = int(input("Введите y: "))

if y == 0:
    y = int(input("На ноль делить нельзя, введите другое число: "))

num_list = []

num_sum = x + y
num_list.append(num_sum)

difference = x - y
num_list.append(difference)

multiply = x * y
num_list.append(multiply)

division = x/y
num_list.append(division)

int_division = x//y
num_list.append(int_division)

sorted_list = sorted(num_list,reverse=True)

print("Второе по величине число: ",sorted_list[1])