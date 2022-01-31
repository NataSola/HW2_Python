
#  Список из нечетных элементов, возведенных в квадрат

# nums = [3, 2, 7, 8, 9, 4, 1, 5]
# def get_square_odd(nums):
#     return [x**2 for x in nums if x % 2 != 0]

# print(nums)
# print(get_square_odd(nums))

a,n=[0,1],9
map(lambda i: reduce(lambda x,y: a.append(x+y),a[-2:]),range(n-2))

# def fibonacci (n):
#     # if n<= 0:
#     #     return "Incorrect Output"
#     data = [0, 1]
#     # if n > 2:
#     #     for i in range (2, n):
#     #         data.append(data[i-1] + data[i-2])
#     if n < 0:
#         for i in range(n, -1, -1):
#             data.append(data[i + 1] - data[i + 2])
#     return data

#     # Driver Program

# print(fibonacci(-10))
# ----------
# def fibo(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a + b

#     return result

# l = [100, 200]
# print(l + fib)
# --------------

def fibo(n):
    result = []
    res_neg = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    # return a, b
    for i in range(-n, n):
        res_neg.append(b)
        a, b = b, a - b
    return a, b, result, res_neg

        


fib = fibo(3)
print(fib)

