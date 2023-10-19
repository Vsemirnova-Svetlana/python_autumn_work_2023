def tri_2(n):
    print(n*'*')
    n -=1
    if n>0: tri_2(n)
    if n>0:
        print((n+1)*'*')
    return

print(tri_2(int(input('-->'))))
