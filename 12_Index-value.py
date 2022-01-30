# 12. Для натурального N создать словарь индекс-значение,
# состоящий из элементов последовательности 3k + 1.

from random import randint

def get_dict(n):
    return {x: 3 * x + 1 for x in range(1, n+1)}

n = randint(5, 20)

print(n)
print(get_dict(n))