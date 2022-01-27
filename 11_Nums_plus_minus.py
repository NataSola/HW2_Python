# 11. Для натурального N создать список: 1, -3, 9, -27 и т.д.

n = int(input('Введите число: '))

def get_degree(n):
    return [((-3)**i) for i in range(n)]

print (get_degree(n))