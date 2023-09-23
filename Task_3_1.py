lst = []
while True:
    salary = int(input('Введите зарплату, для завершения ввода нажмите 0 ("ноль"): '))
    if salary == 0: break

    else:
        lst.append(salary)

total_salary = 0
num_of_workers = 0
for j in lst:
    num_of_workers +=1
    total_salary +=j

average_sal = total_salary/num_of_workers
print("Средняя зарплата сотрудников: ", round(average_sal,1))