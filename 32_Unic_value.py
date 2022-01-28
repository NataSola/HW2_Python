# 32. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    # list2 = []
    return set(list)
    # [i for i in range[list] if not in rage(list2)]

size = 25
m = 10
n = 100

origin = create_list(size, m, n)
print(origin)

print(get_unic_value)


