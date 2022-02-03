# 30. Вычислить число pi c заданной точностью d
# 	  Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

from cmath import acos
from math import pi
from decimal import Decimal
from math import acos

# import sympy
print()
n = pi
# print(f'pi:      {n}')
# print(f'355/113: {355/113}')
print(format(pi,'.100'))
# print(format(Decimal.from_float(n), '.100f')) 
print()


# import math 
# def CalculatePi(roundVal):
# 		somepi = round(math.pi,roundVal);
# 		pi = str(somepi)
# 		someList = list(pi)
# 		return somepi;
# roundTo = input('Enter the number of digits you want after the decimal for Pi: ')
# try:
# 	roundint = int(roundTo);
# 	print(CalculatePi(roundint));
# except:
# 	print("You did not enter an integer");


