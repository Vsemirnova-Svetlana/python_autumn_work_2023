def transform(num):
    dct = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500, 'M':1000}

    res = 0

    if 'IV' in num:
        res = res + 4
        num= num.replace('IV','')
    if 'IX' in num:
        res = res + 9
        num = num.replace('IX', '')
    if 'XC' in num:
        res = res + 90
        num = num.replace('XC', '')
    if 'XL' in num:
        res = res + 40
        num = num.replace('XL', '')
    if 'CD' in num:
        res = res + 400
        num = num.replace('CD', '')
    if 'CM' in num:
        res = res + 900
        num = num.replace('CM', '')

    for i in num:
        res = dct[i]+res

    return res

examples={1:'MMXXIII', 2:'MMXXIV', 3:'MCMXVII', 4:'MCMLXI', 5:'MM',6:'MDCCCLXII'}
while True:
    x = int(input("Для перевода римского числа в десятичное, наберите его номер (ключ в словаре). Для завершения работы наберите 0: "))
    if x == 0: break
    else:
        print(examples[x], '=', transform(examples[x]))


