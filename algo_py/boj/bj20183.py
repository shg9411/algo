import sys
import heapq
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

res = -1
dist = [sys.maxsize]*(n+1)
dist[a] = 0
q = [(0, 1, a)]
while q:
    r, cost, p = heapq.heappop(q)
    if p == b:
        res = r
        break
    for v, w in adj[p]:
        if cost+w-1 > c:
            continue
        nxt = (max(r, w), cost+w, v)
        if dist[v] > nxt[0]:
            dist[v] = nxt[0]
            heapq.heappush(q, nxt)
print(res)
