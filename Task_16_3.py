def deco(func):
    def wrapper():
        f = func()
        res = f.lower()
        return res
    return wrapper

@ deco
def printer():
    return 'HI TheRe, NiCe TO MEET YOU!'

print(printer())