# 30. Вычислить число pi c заданной точностью d
# 	  Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

import math
from math import pi

n = pi
print(n)

n=20000000

mypi = 4 * (sum(1/x for x in range (1, n + 1, 4)) + sum(-1/x for x in range (3, n + 1, 4)))

print(format(mypi,'.100')) 