def deco(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        res = []
        for i in args:
            if type(i) == list:
                for j in i:
                    if type(j)==str:
                        res.append(j.upper())

            elif type(i) == str:
                res.append(i.upper())

            elif type(i) == dict:
                for k,m in i.items():
                    if type(m) == str:
                        res.append(m.upper())

            elif type(i) == tuple:
                i = list(i)
                for j in i:
                    if type(j)==str:
                        res.append(j.upper())

            elif type(i) == set:
                i = list(i)
                for j in i:
                    if type(j)==str:
                        res.append(j.upper())

        for h,l in kwargs.items():
            if type(l) == str:
                res.append(l.upper())

        return res
    return wrapper

@deco
def test(*args,**kwargs):
    return None

dct =  {1:'hi',2:222,'here':'St-Petersburg'}
lst = ['aaa',123,None,'bbb']
tup = (1,2,'HahaHa')
tes = {10,20,"enough!!!"}


print(test('eee', lst,'vfg',111, dct, tup, tes, a = 'Named_arg', b = 123, c = 'another_named_arg'))

