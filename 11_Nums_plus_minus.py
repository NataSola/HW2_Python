# Для натурального N создать множество: 1, -3, 9, -27 и т.д.

n = int(input('Введите число: '))

# def get_cubes(n):
#     cubes = {1}
#     for i in range(n):
#         if i%2 !=0: 
#             cubes.add(-3**i)
#         else: cubes.add(3**i)
#     return cubes

# print(get_cubes(n))

def get_degree(n):
    return [((-3)**i) for i in range(n)]

print (get_degree(n))