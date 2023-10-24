import re
def tit(l):
    s = l.group()
    if len(s)<4: s = ''
    else: return s[0].capitalize()

line = 'Научно-Исследовательский университет информационных технологий механики и оптики'
res = re.sub(r'\b\w+.\b',tit,line)

print(res)


