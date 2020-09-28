import sys
c = 0
for r in sys.stdin.read().splitlines()[1:-1]:
    if r == '문제':
        c += 1
    else:
        if c > 0:
            c -= 1
        else:
            c += 2
print("힝구" if c else "고무오리야 사랑해")
