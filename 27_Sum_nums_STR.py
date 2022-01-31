# 27. Строка содержит набор чисел. Показать большее и меньшее число

string = '49 25 46 7 4 3 8 5'

def convert_to_int(str):
    return [int(x) for x in str.split()]

str_list = convert_to_int(string)
print(min(str_list), max(str_list))