def sort(lst):
    new_lst=[]
    for i in lst:
        for j in i:
            new_lst.append(j)

    x_max=new_lst[0]

    for i in new_lst:
        if i>x_max:
            x_max=i
    new_lst.remove(x_max)

    x_sec_max = new_lst[0]
    for i in new_lst:
        if i>x_sec_max:
            x_sec_max=i
    new_lst.remove(x_sec_max)

    x_thd_max = new_lst[0]
    for i in new_lst:
        if i>x_thd_max:
            x_thd_max=i

    max_lst = sorted([x_max,x_sec_max,x_thd_max])

    return max_lst

print(sort([[11,6,200],[3,4,0],[10,5,45],[140,-5,4]]))






