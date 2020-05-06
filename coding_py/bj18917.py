import sys
input = sys.stdin.readline
sumNum = 0
xorNum = 0
M = int(input())
for _ in range(M):
    x, *y = map(int, input().split())
    if x == 1:
        sumNum += y[0]
        xorNum ^= y[0]
    elif x == 2:
        sumNum -= y[0]
        xorNum ^= y[0]
    elif x == 3:
        print(sumNum)
    else:
        print(xorNum)
