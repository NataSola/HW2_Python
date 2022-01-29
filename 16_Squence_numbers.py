# 16. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму 

n = int(input('Введите число: ')) 

def get_squerence(n):
    return sum([(1 + 1 / x)**x for x in range (1, n + 1)])

print(get_squerence(n))