total_salary = 0
num_of_workers = 0

while True:
    salary = int(input('Введите зарплату, для завершения ввода нажмите 0 ("ноль"): '))
    if salary == 0: break

    else:
        total_salary = total_salary + salary
        num_of_workers +=1

average_sal = total_salary/num_of_workers
print("Средняя зарплата сотрудников: ", round(average_sal,1))
