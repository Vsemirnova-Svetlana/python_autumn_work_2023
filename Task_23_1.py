string = 'abcdefedcbghicdedcxz'
pal=[]
for i in range(len(string)):
    for j in range(i,len(string)):
        sbstr = string[i:j+1]
        if sbstr == sbstr[::-1]:
            pal.append(sbstr)
# print(pal)
max_len = 0
for i in pal:
    if len(i)>max_len:
        max_len = len(i)
print(max_len)


