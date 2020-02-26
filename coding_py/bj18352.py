import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n, m, k, x = map(int, input().split())
edge = [dict() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    edge[a][b] = 1

dist = [INF for _ in range(n+1)]
dist[x] = 0

pq = [(0, x)]

while pq:
    d1, v1 = heapq.heappop(pq)
    for v2, d2 in edge[v1].items():
        if dist[v1]+d2 < dist[v2]:
            dist[v2] = dist[v1]+d2
            heapq.heappush(pq, (dist[v2], v2))

res = []
for i, v in enumerate(dist):
    if v == k:
        res.append(str(i))
print('\n'.join(res) if res else -1)
