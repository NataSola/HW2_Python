
import re

file1 = '33_Polynomial.txt'
file2 = '33_Polynomial2.txt'

# Получение данных из файла
def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# Получение списка кортежей (<коэффициент>, <степень>)
def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей для суммы полиномов
# (<коэф1 + коэф2>, <степень>)
def sum_pols(pol1, pol2):    
    x = [0] * (max(len(pol1), len(pol2) + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res



# def get_new_pol(pol):

pol1 = read_pol(file1)
pol2 = read_pol(file2)
print(pol1)
print(pol2)

pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)
print(pol_1)
print(pol_2)

pol_sum = sum_pols(pol_1, pol_2)
print(sum_pols(pol_1, pol_2))