
def is_equal(a,b):
    lst = []
    if a == '' and b == '':
        return True
    if a == '' or b == '':
        return False
    if (a in b) and (len(b) - len(a)<=1):
        return True
    elif (b in a) and (len(a) - len(b)<=1):
        return True
    elif len(a) == len(b):
        for i,j in enumerate(a):
            for s,d in enumerate(b):
                if i == s and j == d: lst.append(True)
                elif i == s and j != d: lst.append(False)
                else: continue
        # print(lst)
        k=0
        for i in lst:
            if i == False: k +=1
        if k <= 1: return True
        else: return False
    else:
        return False

a = 'hck'
b = 'hhk'
print(is_equal(a,b))