# 15. Написать программу получающую набор произведений чисел от 1 до N.

from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(get_prods(N))


# Предыдущий вариант решения

# def get_factorial_list(n):
#     fact = 1
#     facts = []
#     for i in range(1, n+1):
#         fact *= i
#         facts.append(fact)
#     return facts

# print(get_factorial_list(N))