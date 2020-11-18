import sys
import heapq
input = sys.stdin.readline


def dijkstra(s, e, m):
    dist = [sys.maxsize]*(n+1)
    dist[s] = 0
    q = [(0, s)]
    while q:
        cost, p = heapq.heappop(q)
        if cost > dist[p]:
            continue
        for v, w in adj[p]:
            if w <= m and dist[v] > cost+w:
                dist[v] = cost+w
                heapq.heappush(q, (dist[v], v))
    return dist[e] <= c


n, m, a, b, c = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

s = 0
e = c+1
while s < e:
    m = (s+e) // 2
    if dijkstra(a, b, m):
        e = m
    else:
        s = m+1
print(s if s <= c else -1)
