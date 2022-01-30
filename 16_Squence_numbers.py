# 16. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму 

from msilib import sequence

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))