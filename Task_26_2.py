def dis(self):
    print(self.animal)
    print(self.name)
    print(self.age)

Pet = type('Pet',(),{'dis':dis})
pet1 = Pet()
pet2 = Pet()
pet3 = Pet()
pet1.animal = 'Кошка'
pet1.name = 'Мурка'
pet1.age = 5
pet2.animal = 'Собака'
pet2.name = 'Дружок'
pet2.age = 1
pet3.animal = 'Лошадь'
pet3.name = 'Бахрома'
pet3.age = 12
for i,j in pet1.__dict__.items():
    print(i,j)



