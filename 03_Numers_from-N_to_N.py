# 7. Показать числа от -N до N

N = int(input('Введите число: '))

def Show_numbers(N):
    for i in range(-N, N+1):
        return i
        
print(Show_numbers(N))