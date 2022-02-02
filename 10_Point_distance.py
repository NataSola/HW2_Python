# 10. Найти расстояние между двумя точками пространства

from random import randint
import math

def Get_coordinates(num_plan, left, right):     # координаты точек
    return tuple([randint(left, right) for i in range(num_plan)])

def Find_dist(a, b):    # расстояние между точками
    return round(math.sqrt(sum((x - y)**2 for x, y in zip(a, b))), 3)

num_plan = 3    # количество осей координат
left = -10
right = 10

point_A = Get_coordinates(num_plan, left, right)
point_B = Get_coordinates(num_plan,left, right)

print(f'A {point_A}, B {point_B}')
print (f'Расстояние между точками: {Find_dist(point_A, point_B)}')