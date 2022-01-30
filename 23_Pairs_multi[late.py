# 23. Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
import math

def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]


def multiplate_pairs(mylist):
    mults = []
    i = 0
    j = -1
    while i < math.ceil(len(mylist) / 2):
        mults.append(mylist[i] * mylist[j])
        i += 1
        j -= 1
    return mults

n = 7
frst = 1
last = 10

mylist = get_numbers(n, frst, last)
print(mylist)
print(multiplate_pairs(mylist))


# Второй способ:

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

print(pairs_mult(mylist))