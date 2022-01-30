# 22. Найти сумму чисел списка, стоящих на нечетной позиции

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

n = 10
frst = 1
last = 10

mylist = get_list(n, frst, last)
print(mylist)
print(sum_odd_position(mylist))