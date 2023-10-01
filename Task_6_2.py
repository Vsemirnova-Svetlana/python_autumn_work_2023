def have_read(line1,line2):
    str1=line1.replace(' ','')
    str2=line2.replace(' ','')

    set1=set(str1.lower().split(','))
    set2=set(str2.lower().split(','))
    both_read=set1&set2

    n = len(both_read)
    return n

print(have_read("Война и мир, Над пропастью во ржи, Мастер  и Маргарита, Идиот","Евгений Онегин, Идиот, Мастер и Маргарита, Война и мир"))