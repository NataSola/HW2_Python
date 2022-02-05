# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

from random import randint
import itertools

k = 3

ratios = [randint(0, 10) for i in range (k + 1)]
# ratios = [5, 0, 1, 8, 0]

def get_polinom(k, rat):
    prods = ['*x'] * k  
    degrees = ['^'] * (k - 1)
    n = [n for n in range(k, 1, -1)]    # список степеней в обратном порядке от большего до 2
    additions = [' + '] * k
    rat = list(map(str, rat))       # преобразование чисел (список коэффициентов) в строковые значения
    pol = list(itertools.zip_longest(rat, prods, degrees, n, additions, fillvalue=''))  # собираем члены многочлена в виде кортежей
    pol = [x for x in pol if x[0] != '0']      # оставляем элементы (кортежи), коэффициент != 0
    pol = [list(x) for x in pol]        # преобразуем кортежи в списки  
    for x in pol[0:-1]:
        if x[0] == '1': del x[0]
        if x[0] == '*x': x[0] = 'x'
    if pol[-1][-1] == ' + ': del pol[-1][-1]
    pol.append([' = 0'])
    pol = list(itertools.chain(*pol))   # преобразование списка списков в список
    return "".join(map(str, pol))   # преобразование списка в строку


polynom = get_polinom(k,ratios)
print(polynom)

print(ratios)

with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom)