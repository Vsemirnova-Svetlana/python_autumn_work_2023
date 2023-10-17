def seq(n):

    for i in range(1, n):
        if i%2 !=0: yield i
        else: yield -i

gf = seq(31)

for k in gf:
    print(k, end=', ')
