while 1:
    tmp = input()
    if tmp == '0':
        break
    print('yes' if tmp == tmp[::-1] else 'no')
