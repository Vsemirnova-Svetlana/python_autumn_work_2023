def arabic_to_rome(num):
    dct = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M',
       4:'IV', 9:'IX', 90:'XC', 40:'XL', 400:'CD', 900:'CM'}

    res=''

    lst = []
    k=1
    for i in num[::-1]:
        lst.append(int(i)*k)
        k=k*10
    print(lst)


    for i in lst[::-1]:
        for j,p in dct.items():
            if i == j:
                res = res + p

            else:
                if i>1000:
                    res = res + 'M'*(int(i)//1000)
                    break
                elif i>500 and i <900:
                    res = res + 'D'+'C'*((int(i)-500)//100)
                    break
                elif i>100 and i<400:
                    res = res + 'C'*(int(i)//100)
                    break
                elif i>50 and i <90:
                    res = res + 'L' + 'X'*((int(i)-50)//10)
                    break
                elif i>10 and i <40:
                    res = res + 'X'*(int(i)//10)
                    break
                elif i>5 and i <9:
                    res = res + 'V' + "I"*((int(i)-5))
                    break
                elif i>1 and i<4:
                    res = res + 'I'*(int(i))
                    break
    return res

g = input("Введите число: ")
print(g, '->', arabic_to_rome(g))