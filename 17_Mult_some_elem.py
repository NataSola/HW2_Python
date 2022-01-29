# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

with open('data_task17.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('3\n')
    data.write('11\n')
    data.write('15\n')

def get_numbers(n):
    return [i for i in range(-n, n + 1)]

def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_mult(numbers, datalist):
    mult = 1
    for i in (datalist):
        mult *= numbers[i]
    return mult

path = 'data_task17.txt'
n = 10 
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print(datalist)
print(get_mult(numbers, datalist))