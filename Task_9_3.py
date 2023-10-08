line= '''«Природа Будды – это ваша собственная природа. 
Она реально существует, а не возникает как плод причинно-следственных связей. 
Учение Будды исходит из истинной природы вашего Сознания.
Поэтому говорят, что Сознание – это Нирвана». 
Бодхидхарма, "Учение прямой передачи"
'''
def frequensy(string):

    dct = {}
    for i in line.lower():
        dct[i]=dct.get(i,0) +1
    # print("исходник",dct)
    sorted_dct={}

    sorted_dct=sorted(dct.items(), key = lambda x: (-x[1],x[0]))
    # print('количеству и по алфавиту',sorted_dct)

    for i in sorted_dct[0:10]:
        print(i[0], '-' ,i[1])

frequensy(line)
