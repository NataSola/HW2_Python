# 14. Подсчитать сумму цифр в вещественном числе.

from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    n_str = str(n).replace('.','') 
    n_num = map(int, list(n_str))
    return sum(n_num)

print(n)
print(sum_digit(n))