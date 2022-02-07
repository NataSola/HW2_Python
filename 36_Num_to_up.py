# 36. Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# *Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.*
# ***Порядок элементов менять нельзя***

nums = [1, 5, 2, 3, 4, 6, 1, 7]

def get_up2(nums):
    ups = [0]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    del ups[0]
    return ups

print(get_up2(nums))


# Предыдущий вариант

def get_up(nums):
    ups = []
    for i in range(len(nums) - 1):
        if nums[i] == max(nums[:i+1:]):
            ups.append(nums[i])
    return ups

print(get_up(nums))