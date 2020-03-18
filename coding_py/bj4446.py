import sys

mo = 'aiyeou'
ja = 'bkxznhdcwgpvjqtsrlmf'

while 1:
    try:
        text = input().rstrip()
    except:
        exit()
    res = ''

    for x in text:
        char = x.lower()
        if char in mo:
            tmp = mo.index(char)
            tmpChar = mo[(tmp+3) % 6]
        elif char in ja:
            tmp = ja.index(char)
            tmpChar = ja[(tmp+10) % 20]
        else:
            res += x
            continue
        if x.islower():
            res += tmpChar
        else:
            res += tmpChar.upper()

    print(res)
