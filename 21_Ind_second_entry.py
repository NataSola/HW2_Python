# 21. Определить позицию второго вхождения строки в списке либо сообщить, что его нет.

value1 = 'as'
value2 = 'sxascv acs asdf vsdg assd'

n = 3
def get_sec_entry(val1, val2):
    start = val2.find(val1)
    return val2.find(val1, start + 1)

print(get_sec_entry(value1, value2))