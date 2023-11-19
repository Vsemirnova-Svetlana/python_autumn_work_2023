class Age:
    def __init__(self):
        self._age = None
    @property
    def person(self,persons_age):
        self._age = persons_age

    @person.setter
    def person(self,persons_age):
        if 1<=persons_age<=100:
            self._age = persons_age
        else:
            print('Некорректный ввод возраста')

    @person.getter
    def person(self):
        return self._age
    @person.deleter
    def person(self):
        print(f'возраст {self._age = } удалён')
        del self._age
        print(self.__dict__)

age = Age()
age.person = 23
print(age.person)





