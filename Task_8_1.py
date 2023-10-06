def gen_code(string):

    new_str=''

    if string.find("ЦТ") != -1:
        new_str =new_str + "Ц" + "АГ" + "Т"
    elif string.find("ТЦ") != -1:
        new_str = new_str + "Т" + "АГ" + "Ц"

    else:
        if string.find("АГ") != -1:
            new_str = new_str + string.replace("АГ", "ГА")
        elif string.find("ГА") != -1:
            new_str = new_str + string.replace("ГА", "АГ")
        else: new_str = string

    return new_str


k = input("Введите изначальный генетический код: ")
print("Изменённый генетический код: ", gen_code(k))