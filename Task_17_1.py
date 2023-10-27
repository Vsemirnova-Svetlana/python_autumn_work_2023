import re

text = ('Напишите программу программу, которая устраняет устраняет повторяющиеся слова слова.')

regex1 = re.findall(r'\b\w+\b|\W*', text)
# print(regex1)

st=',..-:;?!'
lst = []
fin_lst=[]
for i in regex1:
    if i == ' ': continue
    if i in st: fin_lst.append(i)
    else:
        lst.append(i)
        if len(lst)==2:
            if lst[0]!=lst[1]:
                fin_lst.append(lst[0])
                print('fin',fin_lst)
                lst.remove(lst[0])
                print('ls',lst)
            elif lst[0] == lst[1]:
                fin_lst.append(lst[0])
                print('fin',fin_lst)
                lst.clear()
            else: continue
d = ' '.join(fin_lst)
print(d)

res =re.sub(r'\s+',' ',d)
res1 =re.sub(r'\s,',',',res)
print(res1)



