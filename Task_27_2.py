class Item:
    price = 500
    quantity = 7
    def __init__(self,name):
        self.name = name
    def __setattr__(self,name,value):
        self.__dict__[name] = value.capitalize()
    def __getattr__(self,total):
        total = self.price * self.quantity
        return total

product = Item('утёнок в ванную')
print(product.name)
print(product.total)