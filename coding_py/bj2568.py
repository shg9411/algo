import sys
import bisect
input = sys.stdin.readline

t = int(input())
tmp = []
aSet = set()
for _ in range(t):
    a, b = map(int, input().split())
    tmp.append([a, b])
    aSet.add(a)

tmp.sort(key=lambda x: x[1])
lis = []

for val in tmp:
    lis.append(val[0])

lis_arr = [lis[0]]
res = [0]

for val in lis[1:]:
    if val > lis_arr[-1]:
        lis_arr.append(val)
        res.append(len(lis_arr)-1)
    else:
        idx = bisect.bisect_left(lis_arr, val)
        lis_arr[idx] = val
        res.append(idx)
i = len(lis_arr)
print(t-i)
idx = len(res)-1
while i:
    if res[idx] == i-1:
        aSet.discard(lis[idx])
        i -= 1
    idx -= 1
print('\n'.join(map(str, aSet)))
