def tf(l):
    a = '('
    b = ')'
    if line.count(a) == line.count(b):
        c = True
    else:
        return False
    sum_a = 0
    sum_b = 0
    lst = []
    for i in line:
        if i == a:
            sum_a += 1
        else:
            sum_b += 1
        if sum_a >= sum_b:
            lst.append(True)
        else:
            lst.append(False)
    # print(lst)
    d = all(lst)
    return c and d

line = '(()())())('
print(tf(line))