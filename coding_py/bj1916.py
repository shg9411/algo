import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [sys.maxsize]*n

adj = [[] for _ in range(n)]

for _ in range(m):
    s, e, c = map(int, input().split())
    adj[s-1].append((e-1, c))


start, end = map(int, input().split())


def dijkstra():
    hq = []
    heappush(hq, (0, start-1))
    dist[start-1] = 0
    while hq:
        cost, now = heappop(hq)
        if dist[now] < cost:
            continue
        for nxt, ncost in adj[now]:
            ncost += cost
            if dist[nxt] > ncost:
                dist[nxt] = ncost
                heappush(hq, (ncost, nxt))
    print(dist[end-1])

dijkstra()