# 17. По двум заданным числам проверить, является ли одно квадратом другого

a = int(input('Введите число: '))
b = int(input('Введите число: '))

def chek_sqr(a, b):
    return a**2 == b or b**2 == a

print (chek_sqr(a,b))