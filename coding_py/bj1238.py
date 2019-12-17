import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, m, x = map(int, input().split())
adj = [[] for _ in range(n)]
dist = [sys.maxsize] * n
total = [0] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a-1].append((b-1, c))


def dijkstra(f, t, a):
    hq = []
    heappush(hq, (0, f-1))
    dist[f-1] = 0
    while hq:
        cost, now = heappop(hq)
        if dist[now] < cost:
            continue
        for nxt, ncost in adj[now]:
            ncost += cost
            if dist[nxt] > ncost:
                dist[nxt] = ncost
                heappush(hq, (ncost, nxt))


for i in range(1,n+1):
    dijkstra(i,x,a)
    dijkstra(x,i,a)

print(max(total))