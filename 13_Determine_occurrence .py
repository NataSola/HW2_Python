# 13. Пользователь задаёт две строки. 
# Определить количество количество вхождений одной строки в другой.

from itertools import count

value1 = str(input('Введите данные: '))
value2 = str(input('Введите данные: '))

def determ_occur(val1, val2):
    return val2.count(val1)

print(determ_occur(value1, value2))