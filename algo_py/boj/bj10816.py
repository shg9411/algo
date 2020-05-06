import sys
from collections import Counter
input = sys.stdin.readline
res = []
input()
tmp = Counter(input().split())
input()
for n in input().split():
    res.append(tmp[n])
print(' '.join(map(str, res)))
