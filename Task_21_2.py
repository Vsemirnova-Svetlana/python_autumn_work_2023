import numpy as np
def rout(arr):
    lst = [arr[0][0],]
    while True:
        if np.shape(arr)[0] == 1:
            for i in arr:
                for j in i[1:]:
                    lst.append(j)
            break
        if np.shape(arr)[1] == 1:
            for i in arr[1:]:
                for j in i:
                    lst.append(j)
            break
        if arr[0][1]>arr[1][0]:
            less = arr[1][0]
            lst.append(less)
            new = np.delete(arr,0,0)
            arr = new
            # print(new)
        else:
            less = arr[0][1]
            new = np.delete(arr,0,1)
            lst.append(less)
            arr = new
            # print(new)
    # print(lst)
    f=[]
    s = sum(lst)
    for i in lst:
        i = str(i)
        f.append(i)
    print( ' + '.join(f), '= ',s)

massiv = np.array([[10,20,30,40],[5,1,80,7],[90,2,70,1],[23,12,11,34]])
print(massiv)
print(rout(massiv))