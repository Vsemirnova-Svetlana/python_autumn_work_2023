import re
class RongLengthNum(ValueError):
    pass

def num(l):
    while True:
        try:
            number = int(input("Введите число: "))
            if number>=10 and number<100 : break
            else:
                raise RongLengthNum

        except RongLengthNum as e:
            print("Надо ввести положительное двузначное число!",e)

    res = re.findall(r'\d+', l)
    for i in res:
        i=int(i)
        if int(i)<=number:
            print(i, end = ' ')

line = '1 3 b 67 45 12 :78 99 100 k 2 0 1000'
num(line)
