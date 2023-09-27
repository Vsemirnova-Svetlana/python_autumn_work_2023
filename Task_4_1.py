dct = {"+": '', "-": '', "*": '', "/": ''}
while True:
    n = input("Для выхода из калькулятора наберите exit: ")
    if n == "exit": break

    else:
        lst = n.split()
        a = int(lst[0])
        b = int(lst[2])
        c = lst[1]
        for i in dct:
            if i == c:
                if c == "+": dct[i] = a + b
                elif c == '-': dct[i] = a - b
                elif c == '*': dct[i] = a * b
                elif c == '/': dct[i] = a / b
            print(dct[i])
            break














