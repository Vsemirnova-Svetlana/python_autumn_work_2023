import string
def separator(line):
    letters = string.ascii_letters
    letters_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    nums = string.digits
    symb = string.punctuation

    letter_s,num_s,symb_s=set(),set(),set()

    for i in line:
        if i in letters: letter_s.add(i)
        elif i in letters_rus: letter_s.add(i)
        elif i in nums: num_s.add(i)
        elif i in symb: symb_s.add(i)
    print(' '.join(letter_s))
    print(' '.join(num_s))
    print(' '.join(symb_s))
    return None

print(separator("ab18.,cab=561:xz:"))

