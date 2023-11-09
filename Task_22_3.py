import keyword
import re
kw_lst = keyword.kwlist
print(kw_lst)
def wk(x):
    s = x.group()
    if s in kw_lst:
        return '<kw>'
    else:
        return s

text = r'''True: This keyword is used to represent a boolean true. 
If a statement is true, "True" is printed.
False: This keyword is used to represent a boolean false. If a 
statement is false, "False" is printed. 
None: That's a special constant used to denote a null value or a 
void. It’s important to remember, 0, any empty container(e.g. empty list) 
does not compute to None. '''

new_text = re.sub(r'\w*',wk,text)
print(new_text)