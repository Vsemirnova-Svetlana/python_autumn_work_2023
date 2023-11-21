def num_el(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
        if type(i) == list:
            new_lst.extend(num_el(i))
    return new_lst
l = [1,2,True,4,'g',['ghj',1,[3]],[False,11]]
print(len(num_el(l)))

