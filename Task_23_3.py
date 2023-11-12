def max_number(l):
    st_lst = list(map(str,lst))
    res = sorted(st_lst, key = lambda x: (x[0],x[-1]), reverse = True)
    print(res)
    return ''.join(res)

lst = [25,9,8,87,89,205]
print(max_number(lst))