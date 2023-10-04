def code(line,k):
    letters='abcdefghijklmnopqrstuvwxyz'
    big_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    new_dct={}
    new_dct2={}

    for i,j in enumerate(letters):
        new_dct[i+1]=j
    for i,j in enumerate(big_letters):
        new_dct2[i+1]=j
    # print(new_dct)
    # print(new_dct2)

    sdvig=0

    for i in line.lower():

        for j,l in new_dct.items():

            if i not in new_dct.values():
                print(i, end='')
                break
            elif i == l:
                j = j+k

                if j>26:
                    sdvig = j-26
                    if sdvig>26:
                        ost = sdvig
                        while ost>26:
                            ost=ost-26
                        sdvig = ost

                    print(new_dct[sdvig],end='')
                else:
                    print(new_dct[j],end='')

code("To be or not to be - That is the question!",200)