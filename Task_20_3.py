class Sequence:
    # letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_lst = []
    fin_lst = []
    def __init__(self,letters,limit):
        self.letters = letters
        self.limit = limit
        self.counter = 0
    def add_nums(self):
        for i, j in enumerate(self.letters):
            Sequence.num_lst.append(i + 1)
        zip_lst = list(zip(Sequence.num_lst, self.letters))
        for i in zip_lst:
            for j in i:
                Sequence.fin_lst.append(j)
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return Sequence.fin_lst
        else:
            raise StopIteration
seq = Sequence('ABCDEFGHIJKLMNOPQRSTUVWXYZ',99)
seq.add_nums()
seq = Sequence('ABCDEFGHIJKLMNOPQRSTUVWXYZ',99)
for i in seq:
    for j in i:
        print(j,end=',')
