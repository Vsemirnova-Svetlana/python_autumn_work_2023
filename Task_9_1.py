def to_rnk(dnk):
    rnk=''
    dct={'G':"C",'C':'G','T':'A','A':'T'}
    for i in dnk:
        for j,h in dct.items():
            if i == j:
                rnk = rnk + h
    return rnk

x = input("Введите ДНК: ")
print(to_rnk(x))