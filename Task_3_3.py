line = input("Введите предложение: ")
new_line = line.strip('.!?')
lst = new_line.split()

max_len = lst[0]

for i in lst:
    if len(i)>len(max_len):
        max_len = i


max_list = []
for j in lst:
    if len(max_len) == len(j):
        max_list.append(j)

print("Самые длинные слова в предложении: ",', '.join(max_list))