import sys
import heapq
input = sys.stdin.readline


def dijkstra_pre():
    dist = [1e9 for _ in range(n+1)]
    dist[1] = 0
    q = [(0, 1)]
    while q:
        co, po = heapq.heappop(q)
        if co > dist[po]:
            continue
        for p, c in adj[po]:
            if (c := c+co) < dist[p]:
                dist[p] = c
                pre[p] = po
                heapq.heappush(q, (c, p))
    return dist[n]


def dijkstra(i, j):
    dist = [sys.maxsize for _ in range(n+1)]
    dist[1] = 0
    q = [(0, 1)]
    while q:
        co, po = heapq.heappop(q)
        if co > dist[po]:
            continue
        for p, c in adj[po]:
            if po == i and p == j or p == i and po == j:
                continue
            if (c := c+co) < dist[p]:
                dist[p] = c
                heapq.heappush(q, (c, p))
    if dist[n] < sys.maxsize:
        return dist[n]
    else:
        print(-1)
        exit()


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
pre = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))
    adj[b].append((a, t))
base = dijkstra_pre()
res = 0
rmv = n
while rmv != 1:
    res = max(dijkstra(pre[rmv], rmv)-base, res)
    rmv = pre[rmv]
print(res)
