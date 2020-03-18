import sys
import bisect
input = sys.stdin.readline
t = int(input())
tmp = []
for _ in range(t):
    a, b = map(int, input().split())
    tmp.append([a, b])
tmp.sort()
lis = []

for val in tmp:
    lis.append(val[1])

res = [501]

for val in lis:
    if val > res[-1]:
        res.append(val)
    else:
        idx = bisect.bisect_left(res, val)
        res[idx] = val
print(t-len(res))
