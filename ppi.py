
pol1 = '12*x^4 + x^2 + 5*x + 10 = 0'
pol2 = '2*x^3 + 3*x^2 + 8*x + 5 = 0'
import re

def convert_pol(pol):
    pol = pol.replace('= 0','')
    pol = re.sub("[*|^| ]"," ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)
print(pol_1)
print(pol_2)


# pol2 = pol2.replace('= 0','')
# pol2 = re.sub("[*|^| ]","", pol2).split('+')

# def summm (pol, pol2):
#     return [complex(x) + complex(y) for x, y in zip(pol, pol2)]

# print(summm (pol, pol2))

# print(pol)
# print(pol2)


