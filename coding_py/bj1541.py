s = input()+' '
v = 0
minus = False
t = 0
for idx in range(len(s)):
    if s[idx] == '+' or s[idx] == ' ':
        if not minus:
            v += t
        else:
            v -= t
        t = 0
    elif s[idx] == '-':
        if not minus:
            v += t
        else:
            v -= t
        minus = True
        t = 0
    else:
        t = t * 10 + int(s[idx])

print(v)
