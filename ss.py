from random import randint
import itertools

k = 5

ratios = [randint(0, 10) for i in range (k + 1)]
while ratios[0] == 0:
    ratios[0] = randint(1, 10) 

ratios = [1, 8, 2, 0, 5]



n = [n for n in range(k, -1, -1)] 
pol = list(zip(ratios, n))

print (n)
print(pol)

###################
# Вторая задача



