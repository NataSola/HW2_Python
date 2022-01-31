# 28. Найти корни квадратного уравнения Ax² + Bx + C = 0
#     - Математикой
#     - Используя дополнительные библиотеки

import math

a = 3
b = -2
c = 8

def find_roots(a, b, c):
    D = b ^ 2 - 4*a*c
    roots = []
    if D < 0: 
        roots.append('Нет корней')
        return roots
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    roots.append(x1)
    if D > 0: roots.append(x2)
    return roots   

print(find_roots(a, b, c))
print(type(find_roots(a, b, c)))