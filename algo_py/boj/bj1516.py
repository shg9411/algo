import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
res = [0 for _ in range(n+1)]
after = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))[:-1]
    time[i] = tmp[0]
    for x in tmp[1:]:
        after[x].append(i)
        num[i] += 1

q = deque()
for i in range(1, n+1):
    if num[i] == 0:
        q.append(i)
for _ in range(n):
    tmp = q.popleft()
    res[tmp] += time[tmp]
    for a in after[tmp]:
        res[a] = max(res[a], res[tmp])
        if num[a] == 1:
            q.append(a)
        num[a] -= 1
print('\n'.join(map(str, res[1:])))