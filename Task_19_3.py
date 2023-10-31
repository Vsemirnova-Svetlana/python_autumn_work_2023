class Person:
    def __init__(self,surname,name,patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        lst = [self.surname[::-1],self.name[::-1],self.patronymic[::-1]]
        return ''.join(lst[::-1])
p = Person('Иванов','Михаил','Федорович')
print(p)