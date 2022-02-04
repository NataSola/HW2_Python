# 30. Вычислить число pi c заданной точностью d
# 	  Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

import math
from math import pi

n = pi
print(n)

# Формула Бэйли — Боруэйна — Плаффа

n = 100
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

print(my_pi)

# Ряд Лейбница

# n = 20000000

# mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) +
#             sum(-1/x for x in range(3, n + 1, 4)))

# print(format(mypi, '.100'))