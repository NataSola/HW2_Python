# 31. Составить список простых множителей натурального числа N

import math


def is_prime(n):
    primes = [2]
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
            primes.append(num)
    return primes


primes = is_prime(100)
print(primes)
