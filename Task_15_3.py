import re
def get_num(num):
    regex = r'(?:\+7\(812\)|\+7\(921\))\d{3}-\d{4}\b|(?:\+7\(812\)|\+7\(921\))\d{3}-\d{2}-\d{2}\b'
    return re.findall(regex,string)

string = ('I 8(812)789-1234 wish  +7(812)789-1234 I could +7(811)789-1234 understand +7'
          '+7(812)921-22-27 all this +7(921)789-1234 regular expression  thing [+7(921)789-12-34]!!')
print(get_num(string))