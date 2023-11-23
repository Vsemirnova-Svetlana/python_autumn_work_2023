def l_hem(a,b):
    res = sum([1 for i in range(len(a)) if a[i] != b[i]])
    return res

print(l_hem(input('Введите первую строку:'),input('Введите вторую строку')))

