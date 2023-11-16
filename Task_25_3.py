def CamelStyle(line):
    str = line.title().replace(' ','')
    return str
string = 'caMel caSe woRD'
print(CamelStyle(string))
