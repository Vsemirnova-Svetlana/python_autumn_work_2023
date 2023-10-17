def pal(n):

    for k in range(1,n):
        k = str(k)
        if k == k[::-1]:
            yield k

gf = pal(500)
for m in gf:
    print(m, end = " ")
