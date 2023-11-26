def find_num(lst):
    dct = {}
    for i in lst:
        dct[i] = dct.get(i,0) + 1
    # print(dct)
    for k,m in dct.items():
        if m == 1:
            return k

l = [12,12,12,12,4,12,12,12]
print(find_num(l))