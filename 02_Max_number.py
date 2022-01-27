# 2. Найти максимальное из пяти чисел

from random import *

n = 5
first = 1
last = 100

def get_nums(n, first, last):
    return [randint(first, last) for i in range(n)]

def get_max(list):
    return max(list)

list = get_nums(n, first, last)
print(list)
print(get_max(list))