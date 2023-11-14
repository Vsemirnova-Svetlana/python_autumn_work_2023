def sort_lst(l):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>=lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
lst = [45,1,-32,0,100,2,0.8,1000,-9]
print(sort_lst(lst))