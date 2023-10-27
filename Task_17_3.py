class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    def print_colour(self):
        print(f'Цвет объекта: {self.colour}')
    def print_square(self):
        print(f'Площадь объекта: {self.square}')

    def make_transparent(self):
        self.colour = 'Прозрачный'

    def make_inf(self):
        self.square = 'Infinity'


Circle = Shape('Синий',350)
Triangle = Shape('Красный',130)
Rhombus = Shape('Зелёный',210)
Parallelogram = Shape('Белый',60)

Circle.print_colour()
Triangle.print_square()
print(Parallelogram.colour)
print(Rhombus.square)
Rhombus.make_transparent()
print(Rhombus.colour)
Parallelogram.make_inf()
print(Parallelogram.square)
