def summ(n):
    if n<10: return n
    else:
        return summ(n//10) + n%10

print(summ(int(input('-->'))))