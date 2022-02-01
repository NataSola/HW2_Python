# 31. Составить список простых множителей натурального числа N

import math

def is_prime(n):
    primes = [2]
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
            primes.append(num)
    return primes

def get_prime_factors(n, primes):
    fact = []
    while n % 2 == 0:
        n = n / 2
        fact.append(2)
    for i in primes:
        while n % i == 0:
            n = n / i
            fact.append(i)
    return fact

n = int(input('Введите число: '))

primes = is_prime(n)
factors = get_prime_factors(n, primes)
print(factors)

def testing(n, factors):
    return math.prod(factors) == n       

print(testing(n, factors))