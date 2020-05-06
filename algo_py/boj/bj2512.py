import sys
input = sys.stdin.readline

n = int(input())
city = sorted(list(map(int, input().split())))
m = int(input())

l = 0
r = city[-1]
res = 0
while l <= r:
    mid = (l+r)//2
    tmp = 0
    for c in city:
        tmp += min(mid, c)
    if tmp <= m:
        res = mid
        l = mid+1
    else:
        r = mid-1
print(res)
