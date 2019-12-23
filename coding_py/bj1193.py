x = int(input())

if x == 1:
    print('1/1')
else:
    x -= 1
    a = 1
    while 1:
        a += 1
        x -= a
        if x <= 0:
            break
    if a % 2 == 0:
        print('%d/%d' % (a+x, -x+1))
    else:
        print('%d/%d' % (-x+1, a+x))
