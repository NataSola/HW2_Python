# 26. Дано число. Составить список чисел Фибоначчи, 
# в том числе для отрицательных индексов

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_pos = []
    fibo_neg = []
    a, b = 0, 1
    for i in range(n):
        fibo_pos.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_neg.insert(0, a)
        a, b = b, a - b
    return fibo_neg + fibo_pos[1::]

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))