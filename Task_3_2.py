n = input("Введите число: ")
lst = []
for i in n:
    lst.append(i)

n0 = lst.count('0')
n1 = lst.count('1')
n2 = lst.count('2')
n3 = lst.count('3')
n4 = lst.count('4')
n5 = lst.count('5')
n6 = lst.count('6')
n7 = lst.count('7')
n8 = lst.count('8')
n9 = lst.count('9')

print(f'0 - {n0}\n1 - {n1}\n2 - {n2}\n3 - {n3}\n'
      f'4 - {n4}\n5 - {n5}\n6 - {n6}\n7 - {n7}\n'
      f'8 - {n8}\n9 - {n9}\n')


