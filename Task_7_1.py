def min_krat(lst):

    new_lst2=[]
    tes=set()

    y = max(lst)

    for i in lst:
        if y%i == 0:
            new_lst2.append(i)
    # print("список делителей макс. числа",new_lst2)

    tes=set(lst)-set(new_lst2)

    tes.add(y)
    # print("множество, эл-ты которого будем перемножать",tes)

    res = 1
    for i in tes:
        res *=i

    return res

print(min_krat([2,3,10,5,8,200,13]))



