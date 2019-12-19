import sys
import math

t = int(sys.stdin.readline())


while t:
    t -= 1
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif (r1+r2)**2 == (x2-x1)**2+(y2-y1)**2:
        print(1)
    elif (r1+r2)**2 < (x2-x1)**2+(y2-y1)**2:
        print(0)
    elif (r2-r1)**2 > (x2-x1)**2+(y2-y1)**2:
        print(0)
    elif x1==x2 and y1==y2 and r1 != r2:
        print(0)
    else:
        print(2)
