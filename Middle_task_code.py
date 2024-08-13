from itertools import product
count_antoha = 0
count_vovan = 0
for x in product('LACOSTE', repeat=5):
    s = ''.join(x)
    sogl_alf = 'LCST'
    gl_alf = 'AOE'
    for i in sogl_alf:
        s.replace(i, '#')
    for i in gl_alf:
        s.replace(i, '*')
    if '##' not in s and '**' not in s:
        count_antoha += 1
for x in product('MARIE', repeat=5):
    s = ''.join(x)
    sogl_alf = 'MR'
    gl_alf = 'AIE'
    for i in sogl_alf:
        s.replace(i, '#')
    for i in gl_alf:
        s.replace(i, '*')
    if '##' not in s and '**' not in s:
        count_vovan += 1
print(max(count_antoha, count_vovan))