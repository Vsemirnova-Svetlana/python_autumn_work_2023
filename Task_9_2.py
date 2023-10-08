def similar_words(x,*args):
    vowels='ауоыиэяюёе'
    lst=[]
    lst_of_similar_words=[]

    for j,i in enumerate(x):
        if i in vowels:
            lst.append(j)
    # print(lst)

    for j in args:
        lst2 = []
        for k,m in enumerate(j):
            if m in vowels:
                lst2.append(k)
        # print(lst2)
        if lst == lst2: lst_of_similar_words.append(j)
        lst2.clear()
    # print(lst_of_similar_words)
    if len(lst_of_similar_words) == 0:
        lst_of_similar_words.append("их тут нет!")

    return ', '.join(lst_of_similar_words)


g=input("Введите первое слово: ").lower()

print(f"Слова, похожие на слово '{g}': ", similar_words(g,'титан','поросёнок','итог','лавка','погост','свобода'))