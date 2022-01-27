# 7. Показать числа от -N до N

N = int(input('Введите число: '))

def Show_numbers(N):
    for i in range(-N, N+1):
        print(i, end=' ')

Show_numbers(N)