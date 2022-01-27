# 17. По двум заданным числам проверить, является ли одно квадратом другого

a = int(input('Введите число: '))
b = int(input('Введите число: '))

def Check_square(a, b):
    if a**2 == b:
        return f'Число {b} является квадратом числа {a}'
    elif b**2 == a:
        return f'Число {a} является квадратом числа {b}'
    else:
        return 'Ни одного из чисел не является квадратом другого'

cheking_result = Check_square(a, b)
print(cheking_result)