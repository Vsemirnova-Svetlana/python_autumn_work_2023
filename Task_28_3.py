counter = 0
def h(a,b,c,n):
    global counter
    counter +=1
    if n == 1:
        print(a, '->', c)
        return f'Число перестановок = {counter}'
    else:
        h(a, c, b, n - 1)
        print(a, '->', c)
        h(b, a, c, n - 1)
    return f'Число перестановок = {counter}'
print(h('A', 'B', 'C', 10))


