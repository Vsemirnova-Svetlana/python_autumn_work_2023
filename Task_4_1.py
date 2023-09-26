
while True:
    n = input("Для выхода из калькулятора наберите exit: ")
    if n == "exit": break

    else:
        lst = n.split()
        a = int(lst[0])
        b = int(lst[2])

        if lst[1] == '+':
            print(a + b)
        elif lst[1] == '-':
            print(a - b)
        elif lst[1] == '*':
            print(a*b)
        elif lst[1] == '/':
            print(a/b)














