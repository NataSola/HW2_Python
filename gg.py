import math
print (2)
for num in range(3,101,2):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       print (num)

