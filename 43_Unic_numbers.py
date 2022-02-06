# 43. Дана последовательность чисел. Получить список 
#     уникальных элементов заданной последовательности.
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [5, 3, 2, 5, 10, 15, 10, 8, 3, 8]

def get_unic(my_list):
    unic = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
            unic.append(my_list[i])
    return unic

print(get_unic(my_list))