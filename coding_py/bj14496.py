import sys
from heapq import *
INF = sys.maxsize

a, b = map(int, input().split())
n, m = map(int, input().split())
adj = [dict() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1

dist = [INF for _ in range(n+1)]
dist[a] = 0

pq = [(0, a)]

while pq:
    d1, v1 = heappop(pq)
    for v2, d2 in adj[v1].items():
        if dist[v1]+d2 < dist[v2]:
            dist[v2] = dist[v1]+d2
            heappush(pq, (dist[v2], v2))
# print(dist)
print(dist[b] if dist[b] != INF else -1)
