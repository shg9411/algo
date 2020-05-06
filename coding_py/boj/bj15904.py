txt = input()
a = b = c = d = False
for i in txt:
    if i == 'U':
        a = True
    if a:
        if i == 'C':
            b = True
    if b:
        if i == 'P':
            c = True
    if c:
        if i == 'C':
            d = True

print('I love UCPC' if a == True and b == True and c ==
      True and d == True else 'I hate UCPC')
