import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

total = int(input())

num = list(map(int, input().split()))

candi = deque([])
can = []
for i in num:
    if i in can:
        candi[can.index(i)][1] += 1
    elif len(candi) < n and i not in can:
        candi.append([i, 1])
        can.append(i)
    else:
        idx = can.index((min(candi, key=lambda l: l[1])[0]))
        del candi[idx]
        del can[idx]
        candi.append([i, 1])
        can.append(i)
can.sort()
print(' '.join(map(str, can)))
