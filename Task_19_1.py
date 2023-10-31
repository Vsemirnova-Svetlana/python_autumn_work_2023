import itertools
class Money:
    lst = []
    lst_j = []
    def __init__(self):
        self.m = [50, 100, 200, 500, 1000, 5000]
    def result(self):
        for j in range(1, 7):
            for x in itertools.combinations(self.m, j):
                # print(x)
                summa = 0
                for i in x:
                    summa += i
                Money.lst.append(summa)
                Money.lst_j.append(summa)
            print(f"Возможные суммы из {j} купюр:", Money.lst_j)
            Money.lst_j.clear()
        return f"Список всех возможных сумм: {Money.lst}"
summa = Money()
print(summa.result())
