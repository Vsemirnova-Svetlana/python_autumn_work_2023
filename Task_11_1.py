import calendar, datetime
import locale

dct={}
for i in range(1,13):
    c = calendar.monthcalendar(2023,i)
    # print(c)
    if c[0][4] == 0:
        dct[i] = c[3][3]
    else:
        dct[i] = c[2][3]
# print(dct)

print("Даты бесплатного посещения Эрмитажа в 2023 году: ")
for i,j in dct.items():

    a = datetime.date(2023, i,j)
    locale.setlocale(locale.LC_ALL,'ru')
    print(a.strftime("%B %d,(%A)"))