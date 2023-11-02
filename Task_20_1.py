class DrinkMenu:
    Drink = {'эспрессо':180, 'американо':190, 'капучино':200, 'латте':210,'чай чёрный':70,'чай зелёный':75}
    def __init__(self):
        self.drink = DrinkMenu.Drink
    def __getitem__(self):
        return self.drink.items()
class FoodMenu:
    Food = {'чизкейк': 240, 'эклер': 130, 'булочка с корицей': 60}
    def __init__(self):
        self.food = FoodMenu.Food
    def __getitem__(self):
        return self.food.items()
class Client:
    order =[]
    daily_proceeds = 0
    in_cash = 0
    by_card = 0
    def __init__(self):
        self.drink = ''
        self.food = ''
        self.payment = '' #by card/in cash
        self.cost = 0
        self.by_card = 0
        self.in_cash = 0
        Client.order.append(self)
    def make_order(self):
        drink = input("Выберите напиток из предложенных в меню: ")
        self.drink = drink
        food = input("Выберите десерт: ")
        if food =='нет':
            self.food = None
        else:
            self.food = food
        payment = int(input("Для оплаты по карте введите 1, наличными: 2: "))
        if payment == 1:
            self.payment = 'оплата по карте'
            Client.by_card += 1
        if payment == 2:
            self.payment = 'оплата наличными'
            Client.in_cash += 1
        cost_d = DrinkMenu.Drink[self.drink]
        if self.food == None:
            cost_f = 0
        else:
            cost_f = FoodMenu.Food[self.food]
        self.cost = cost_d + cost_f
        Client.daily_proceeds += self.cost
    def d_proceeds(self):
        return f'Выручка за день: {Client.daily_proceeds}'
    def bill(self):
        for i in Client.order:
            print("Заказ клиента:",'\n','Напиток: ',i.drink,',', 'десерт:',i.food,',', i.payment, i.cost,'руб.')
    def pay(self):
        return f'За день оплатили по карте: {Client.by_card} человек, наличными: {Client.in_cash} человек.'


client1 = Client()
client1.make_order()
# client1.bill()
client2 = Client()
client2.make_order()
# client2.bill()
client3 = Client()
client3.make_order()
client3.bill()

print(client1.d_proceeds())
print(client1.pay())