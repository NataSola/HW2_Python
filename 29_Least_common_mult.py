# 29. Найти НОК двух чисел

from math import lcm

a = 6
b = 8

def get_lcm(a, b):
    return lcm(a, b)

print(get_lcm(a, b))