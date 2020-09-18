from itertools import product

for i,l in enumerate(product('([)]',repeat = 4)):
    if 59<i<64:
        print(''.join(l))

