class Fibonacci:
    def __init__(self):
        self.num1 = 0
        self.num2 = 1
        self.num3 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.num3 = self.num1 + self.num2
        self.num1 = self.num2
        self.num2 = self.num3
        return self.num1

f = Fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

