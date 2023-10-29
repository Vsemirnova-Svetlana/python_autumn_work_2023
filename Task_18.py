class Task:
    def __init__(self,task):
        self.task = task
    def make_task(self):
        print(f'Задача: {self.task}')

    def __getitem__(self,task):
        return self.task

class Student:
    def __init__(self,st_name):
        self.st_name = st_name
        self.homework = ''
    def take_t(self,task):
        self.homework = task
        print(f"Студент {self.st_name} получил домашнее задание.")

    def __getitem__(self,ready_task):
        self.ready_task = 'задача решена'
        return self.ready_task
    def take_a(self,answer):
        self.answer = answer
        if self.answer == True:
            print(f'{self.st_name}: Зачёт!')
        if self.answer == False:
            print(f'{self.st_name}: Незачёт! Переделать.')

class Teacher:
    def __init__(self,t_name):
        self.t_name = t_name
        
    def teach(self,task,*student):
        for i in student:
            i.take(task)

    def take(self,ready_task):
        self.ready_task = ready_task
        if ready_task == "Yes":
            print(f"{Mihail.t_name} получил решение от студента {self.st_name} в статусе 'задача решена' и проверяет.")
        if ready_task == 'No':
            print(f"Cтудент {self.st_name} д/з не прислал.")

    def __getitem__(self,answer):
        return self.answer



Mihail =Teacher('Михаил')

Sergey = Student('Сергей')
Dasha = Student('Даша')
Alex = Student('Алексей')

t = Task('Числа Фибоначчи')
Task.make_task(t)

Sergey.take_t('Числа Фибоначчи')
Dasha.take_t('Числа Фибоначчи')
Alex.take_t('Числа Фибоначчи')

Teacher.take(Sergey,'No')
Teacher.take(Dasha, "Yes")
Teacher.take(Alex, "Yes")
Student.take_a(Dasha,True)
Student.take_a(Alex,False)

