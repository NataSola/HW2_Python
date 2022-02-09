
import re
import itertools

pol1 = '7*x^2 + 0*x + 1 = 0'
pol2 = '2*x^5 + x^4 + 3*x^3 + 0*x = 0'


def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol


def get_pol_sum(pol1, pol2):    
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    print(x)
    for i in pol1 + pol2:
        print(f'0: {i}   {x[i[1]]}   {i[0]}    ', end='')
        x[i[1]] += i[0]
        print(f'1: {x[i[1]]},   {i}  {x}')
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    # print (res)
    res.sort(key = lambda r: r[1], reverse = True)
    return res


def get_new_pol(pol):
    var = ['*x^'] * len(pol)
    # degrees = ['^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]

    # print(coefs, degrees, var)
    # print(len(coefs), len(degrees), len(var))

    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]

    # print(new_pol)

    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0])
            x[0] = 'x^'
        if len(x) >1 and x[-1] == '1': 
            del x[-1]
            x[-1] - '*x'
        x.append(' + ')
    
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    print(new_pol)
    
    return "".join(map(str, new_pol))      

# new_pol = get_new_pol()
    

pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)
print(pol_1)
print(pol_2)

pol_sum = get_pol_sum(pol_1, pol_2)
print(pol_sum)
x = get_new_pol(pol_sum)
print(x)