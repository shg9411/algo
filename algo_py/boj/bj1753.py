import sys
import heapq
input =sys.stdin.readline
INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

dist = [INF for _ in range(V + 1)]
dist[K] = 0
q = [(0, K)]

while q:
    c, p = heapq.heappop(q)
    if c > dist[p]:
        continue
    for v, w in adj[p]:
        if dist[v] <= c+w:
            continue
        dist[v] = c+w
        heapq.heappush(q, (c+w, v))

for r in dist[1:]:
    if r < sys.maxsize:
        print(r)
    else:
        print("INF")
