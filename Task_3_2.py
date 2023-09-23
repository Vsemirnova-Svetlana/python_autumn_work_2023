n = input("Введите число: ")
n0,n1,n2,n3,n4,n5,n6,n7,n8,n9 = 0,0,0,0,0,0,0,0,0,0
for i in n:
    if i == '0': n0 +=1
    elif i == '1': n1 +=1
    elif i == '2': n2 +=1
    elif i == '3': n3 +=1
    elif i == '4': n4 +=1
    elif i == '5': n5 +=1
    elif i == '6': n6 +=1
    elif i == '7': n7 +=1
    elif i == '8': n8 +=1
    elif i == '9': n9 +=1
print(f'0 - {n0}\n1 - {n1}\n2 - {n2}\n3 - {n3}\n'
      f'4 - {n4}\n5 - {n5}\n6 - {n6}\n7 - {n7}\n'
      f'8 - {n8}\n9 - {n9}\n')


