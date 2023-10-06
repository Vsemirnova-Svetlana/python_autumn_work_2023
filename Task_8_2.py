x = [[1,222,7,5777],[4,51,3],[1,51,6,899],[1,2]]
def sort(x):
    lst=[]
    for i in x:
        y = sorted(i, reverse=True)
        lst.append(y)

    x1 = lst
    lst2 = []
    for i in x1:
        lst2.append(list(map(str, i)))

    ww=[]
    for i in lst2:
        summ = ''
        for j in i:
            summ += j
        # print(summ)
        ww.append(len(summ))
    # print(ww)

    f=list(zip(ww,lst2))
    # print(f)

    def ff(l):
        return l[0]

    j =sorted(f, key = ff)
    # print(j)

    fin_lst=[]
    for i in j:

        fin_lst.append(i[1])
    # print(fin_lst)

    result=[]
    for i in fin_lst:
        result.append(list(map(int,i)))
    # print(result)

    return result

print(sort(x))
