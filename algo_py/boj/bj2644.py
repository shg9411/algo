import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
visited = [0 for _ in range(n+1)]
q = deque([a])
while q:
    tmp = q.popleft()
    val = visited[tmp]+1
    for rel in adj[tmp]:
        if not visited[rel]:
            if rel == b:
                print(val)
                exit()
            visited[rel] = val
            q.append(rel)
print(-1)