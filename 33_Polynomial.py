# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polinom(k, rat):
    prods = ['*x'] * k  
    degrees = ['^'] * (k - 1)
    n = [n for n in range(k, 1, -1)]    # список степеней в обратном порядке от большей до 2            
    pol = list(itertools.zip_longest(map(str, rat), prods, degrees, n,  fillvalue=''))  # собираем члены многочлена в виде кортежей
    pol = [list(x) for x in pol if x[0] != '0']      
    for x in pol[0:-1]:
        if x[0] == '1': del x[0]
        if x[0] == '*x': x[0] = 'x'
        x.append(' + ')
    pol.append([' = 0'])
    pol = list(itertools.chain(*pol))  
    print(pol)
    return "".join(map(str, pol))   


ratios = get_ratios(k)
polynom1 = get_polinom(k, ratios)
print(polynom1)

with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polinom(k, ratios)
print(polynom2)

with open('33_Polynomial2.txt', 'w') as data:
    data.write(polynom2)