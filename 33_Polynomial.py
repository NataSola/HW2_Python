# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.  2*х^2 + 5*х + 33 = 0

from random import randint, choice


n = 2 #int(input('k= '))


k_list = [randint(0, 101) for x in range(-10, 11)]
k = choice(k_list)
# pol = choice(k_list) * x ** n + choice(k_list) * x + choice(k_list)
# pol_member = (k + '* x ** ' + n) 

def get_pol(lst, n):
    pol = str()
    for i in range (n+1):
        for j in range (3):
            pol.join('jjj')
            pol.join(str(choice(lst)))
            pol.join(' *  x **')
            pol.join(str(i))
            # pol.join(' + ')
            # pol.join(choice(lst))
            # pol.join(' * x ')
            # pol.join(choice(lst))
    return pol


    # return str (map (lambda x: x ))



# print(k_list)
# print(k)
pol_member = []
pol_member.append(str(choice(k_list)))
pol_member.append('* x **')
pol_member.append(str(n))
polm_str = " ".join(pol_member)

# pol = get_pol(k_list, n)
# print(type(pol))
print(pol_member)
print(polm_str)
