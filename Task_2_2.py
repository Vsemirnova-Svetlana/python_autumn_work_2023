# lst = [-4,15,100,-77,2,0]
lst =[]
num = ''
while True:

    num = input("Введите элемент списка, для завершения ввода наберите exit: ")
    if num == 'exit': break
    else:
        num = int(num)  #если предполагается ввод только целых чисел, если и дробные тоже, то используем тип float
        lst.append(num)


min_num = lst[0]
for i in range(len(lst)-1):
    if i+1 > (len(lst)-1): break

    if lst[i+1] < min_num:
        min_num = lst[i+1]
print(lst)
print(min_num)

