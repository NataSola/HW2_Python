# 20. Определить, присутствует ли в заданном списке строк некоторое число

from random import randint
import itertools


def get_list(raw, col, frst, last):
    return [[randint(frst, last) for j in range(col)] for i in range (raw)]

def find_number(n, mylist):
    return n in list(itertools.chain(*mylist))

raw = 3
col = 3
frst = 1
last = 100

mylist = get_list(raw, col, frst, last)

print(mylist)

n = int(input('Введите число: '))
print(find_number(n, mylist))