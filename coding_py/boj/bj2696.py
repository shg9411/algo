import sys
import bisect
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    print((m+1)//2)
    num = []
    come = m
    while come > 0:
        num += list(map(int, input().split()))
        come -= 10
    tmp = []
    res = []
    for i in range(m):
        bisect.insort(tmp, num[i])
        if i % 2 == 0:
            res.append(tmp[i//2])
    for i in range(len(res)):
        if i % 10 == 9:
            print(res[i], end='\n')
        else:
            print(res[i], end=' ')
