import sys
from collections import deque
input = sys.stdin.readline

c = int(input())
t = int(input())
v = [deque([]) for _ in range(c+1)]

for _ in range(t):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

res = 0
visited = [False for _ in range(c+1)]
q = deque([1])
visited[1] = True
while q:
    tmp = q.popleft()
    res += 1
    for _ in range(len(v[tmp])):
        x = v[tmp].popleft()
        if not visited[x]:
            q.append(x)
            visited[x] = True

print(res-1)
