import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def ok(v):
    cnt = 0
    for t in time:
        cnt += v//t
    return cnt >= m


time = [int(input()) for _ in range(n)]

res = sys.maxsize
l = 0
r = sys.maxsize
while l <= r:
    mid = (l+r)//2
    if ok(mid):
        res = min(res, mid)
        r = mid-1
    else:
        l = mid+1
print(res)
