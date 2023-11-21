import numpy as np
def darts(n):
    matrix = np.ones((n,n),dtype=int)
    if n == 1 or n == 2:
        return matrix
    if n>18:
        return 'Слишком большое число'
    if n>2:
        k = 1
        d=0
        while n - 2 > 0:
            k +=1
            d += 1
            for i in range(d,n-1):
                for j in range(d,n-1):
                    matrix[i][j] = k
            n = n-1
        return matrix
print(darts(int(input('Введите n: '))))


