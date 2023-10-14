def min_max(lst):
    lst_min=[i for i,j in enumerate(lst) if j == min(lst)]
    lst_max=[i for i,j in enumerate(lst) if j == max(lst)]
    return lst_min, lst_max

spisok = [10,0,2,1,3,4,6,5,0,10,10]
print(min_max(spisok))