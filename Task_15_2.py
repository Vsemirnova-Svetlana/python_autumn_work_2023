import re
def car_num(l):

    regex = r'\b[АAХXВBСCРPНHЕEМMОOТTУYКK]\d{3}[АAХXВBСCРPНHЕEМMОOТTУYКK]{2}78\b|\b[АAХXВBСCРPНHЕEМMОOТTУYКK]\d{3}[АAХXВBСCРPНHЕEМMОOТTУYКK]{2}178\b'
    return re.findall(regex,l)

line= 'Java blablabla 095 - L173YU178 56 - 67 К173KX178 L890YU77 Javascript 095 ghj A123KB78, Д123KB78   L890YU179'

print(car_num(line))

