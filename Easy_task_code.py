from itertools import product
number = 0
count = 0
for x in product('ГИЛТУС', repeat=6):
    s = ''.join(x)
    number += 1
    count_g = sum([1 for i in s if i in 'ИУ'])
    count_s = sum([1 for i in s if i in 'ГЛТС'])
    if count_g == count_s and number % 7 == 0:
        count += 1
print(count)