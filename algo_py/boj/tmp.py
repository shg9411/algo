import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(V)]
ward = list(map(int, input().split()))
ward[-1] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    if ward[u] or ward[v]:
        continue
    adj[u].append((v, w))
    adj[v].append((u, w))

dist = [INF for _ in range(V)]
dist[0] = 0
q = [(0, 0)]

while q:
    c, p = heapq.heappop(q)
    if c > dist[p]:
        continue
    for v, w in adj[p]:
        if dist[v] <= c+w:
            continue
        dist[v] = c+w
        heapq.heappush(q, (c+w, v))

print(dist[-1] if dist[-1] < sys.maxsize else -1)
