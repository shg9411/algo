import sys
import math
input = sys.stdin.readline

t = int(input())

while t:
    t -= 1
    x, y = map(int, input().split())
    dis = y-x
    minN = powN = maxN = warpCnt = 0
    n = 1
    while 1:
        powN = n**2
        minN = powN - n + 1
        maxN = powN + n
        if minN <= dis and dis <= maxN:
            if minN <= dis and dis <= powN:
                warpCnt = (n << 1) - 1
            else:
                warpCnt = n << 1
            break
        n += 1
    print(warpCnt)
