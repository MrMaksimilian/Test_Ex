from itertools import *
slovar = []
for x in product('ПЕРМЯКИ', repeat = 7):
    s = ''.join(x)
    if s[1] != 'Я' and s[3] != 'Я' and s[5] != 'Я' and 'ЯКИ' in s:
        slovar += [s]
print(len(set(slovar)))