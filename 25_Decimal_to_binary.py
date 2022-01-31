# 25. Написать программу преобразования десятичного числа в двоичное

n = int(input('Введите число: '))

def conv_dec_to_bin(n):
    bin_num = ''
    while n > 1:
        bin_num += str(n % 2)
        n = n // 2
    return bin_num[::-1]

print(conv_dec_to_bin(n))

# Другие решения

def convert_dec_to_bin(n):
    bin_num = []
    while n > 1:
        bin_num.insert(0, n % 2)
        n = n // 2
    return bin_num

print(convert_dec_to_bin(n))

print(bin(n).replace('0b1',''))