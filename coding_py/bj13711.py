import sys
import bisect
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = [0 for _ in range(n+1)]

for i in range(n):
    tmp[b[i]] = i
for i in range(n):
    a[i] = tmp[a[i]]

res = [a[0]]

for val in a[1:]:
    if val > res[-1]:
        res.append(val)
    else:
        idx = bisect.bisect_left(res, val)
        res[idx] = val
print(len(res))
