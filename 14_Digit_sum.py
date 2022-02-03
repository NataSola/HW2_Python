# 14. Подсчитать сумму цифр в вещественном числе.

from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(n)
print(sum_digit(n))