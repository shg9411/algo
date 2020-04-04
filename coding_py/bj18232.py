import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
visited = [False for _ in range(300001)]
can = [[] for _ in range(300001)]
for _ in range(m):
    x, y = map(int, input().split())
    can[x].append(y)
    can[y].append(x)
q = deque([])
visited[s] = True
q.append([s, 0])
while q:
    a, b = q.popleft()
    if a == e:
        print(b)
        break
    for x in can[a]:
        if not visited[x]:
            q.append([x, b+1])
            visited[x] = True
    if a+1 <= n and not visited[a+1]:
        q.append([a+1, b+1])
        visited[a+1] = True
    if a-1 >= 1 and not visited[a-1]:
        q.append([a-1, b+1])
        visited[a-1] = True
