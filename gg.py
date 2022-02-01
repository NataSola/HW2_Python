import math
import decimal


from math import pi
from decimal import Decimal


n = pi
print(n)
print(format(n,'.100'))
print(format(Decimal.from_float(n), '.100f')) 





# d = '3' /
# dd = '.{d}f'
# print(dd)
# print ('Простой вывод пи на печать')
# print(10**(-10))

# print ("Вывод пи на печать (200 знаков) с использованием format(n,'.200')")
# print(format(pi,'.200'))
# print()

# print ('Вывод на печать (100 знаков) пи с использованием Decimal')
# print(format(Decimal.from_float(pi), '.100f')) 
# print()

# print ('Простой вывод на печать пи * 10^(-100)')
# print(n)
# print()

# print ('Вывод на печать (400 знаков): пи * 10^(-100) с использованием Decimal')
# print(format(Decimal.from_float(n), '.400f')) 
# print()


# print(round(pi, 20))
# print(format(n,'.400f'))






# def task31 (n):
#     i = 2
#     array = []
#     while n != 1: 
#         if n % i == 0:
#             array.append(i) #3
#             n = n / i
#             i = 2
#         else: 
#             i += 1
#     return (array)

# n = 549
# ff = task31 (n)
# print (ff)

# def testing(n, ff):
#     return math.prod(ff) == n       

# print(testing(n, ff))

# # n_str = str(n).replace('.','') 