def odd(lst):
    for i in lst:
        if i %2 !=0:
            yield i

gf = odd([1,2,3,4,5,6,7,22,35,65,7,0,46,1])
for m in gf:
    print(m, end = ' ')