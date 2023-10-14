def num_r(string):
    st=string.split(',')
    st1=[]
    res = []
    # print(st)
    for i in st:
        st1.append(i.split('-'))
    # print(st1)

    for i in st1:
        for j in range(int(i[0]),int(i[1])+1):
            res.append(j)
    return res
line = '1-2,4-4,3-6,10-11,100-109,0-0'
print(num_r(line))
