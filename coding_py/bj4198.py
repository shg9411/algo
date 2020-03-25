import sys
input = sys.stdin.readline
n = int(input())
train = [int(input()) for _ in range(n)]

_max = [0 for _ in range(n)]
_min = [0 for _ in range(n)]

for i in range(n-1, -1, -1):
    _max[i] = _min[i] = 1
    for j in range(i+1, n):
        if train[i] > train[j] and _max[j]+1 > _max[i]:
            _max[i] = _max[j]+1
        if train[i] < train[j] and _min[j]+1 > _min[i]:
            _min[i] = _min[j] + 1


res = 0

for i in range(n):
    res = max(res, _min[i]+_max[i]-1)
print(res)
