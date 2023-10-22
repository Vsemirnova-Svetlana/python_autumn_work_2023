def f(dct,x):
    lst = []
    for i,j in dct.items():
        if i == x:
            lst.append(j)

        if type(j) == dict:
            lst.extend(f(j,x))
    return  lst

ex = {1:1,2:2,3:{2:22,3:{1:111,2:222,3:{0:1111,1:2222,2:3333}},1:11},6:22}
print(f(ex,1))