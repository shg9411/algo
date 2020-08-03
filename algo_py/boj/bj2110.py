import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted([int(input()) for i in range(n)])
l = 1
r = (house[-1]-house[0])//(c-1)+1
res = 0
while l <= r:
    m = (l+r)//2
    val = house[0]
    tmp = 1
    for i in range(1, n):
        if house[i] >= val + m:
            tmp += 1
            val = house[i]
    if tmp < c:
        r = m-1
    else:
        res = m
        l = m+1
print(res)
