def is_izomorf(line1,line2):
    lst1 = []
    lst2 = []
    fin_lst1=[]
    fin_lst2=[]
    dct1 = {}
    dct2 = {}

    for i in line1:
        dct1[i] = dct1.get(i,0)+1
    let_lst1 = []
    for k in dct1:
        let_lst1.append(k)
    for i in line1:
        for k,m in enumerate(let_lst1):
            if i == m:
                lst1.append((i,k))
    # print(lst1)

    for i in line2:
        dct2[i] = dct2.get(i,0)+1
    let_lst2 = []
    for k in dct2:
        let_lst2.append(k)
    for i in line2:
        for k,m in enumerate(let_lst2):
            if i == m:
                lst2.append((i,k))
    # print(lst2)

    for i in lst1:
        fin_lst1.append(i[1])
    # print(fin_lst1)
    for j in lst2:
        fin_lst2.append(j[1])
    # print(fin_lst2)
    return fin_lst1 == fin_lst2

l1 = 'CBAABC'
l2 = 'DEFFED'
print(is_izomorf(l1,l2))