def is_pal(line):
    if len(line) == 0 or len(line) == 1:
        return True
    else:
        if line[0] == line[-1]:
            return is_pal(line[1:-1])
        else:
            return False
string = 'efgh'
print(is_pal(string))