# 4. Показать первую цифру дробной части числа

from random import uniform

def get_frst_fract_digit (n):
    return int(n * 10 % 10)

n = uniform(10,1000)
print(n)
print(get_frst_fract_digit(n))