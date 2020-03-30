import sys
import heapq
input = sys.stdin.readline


def dijkstra():
    dist = [sys.maxsize for _ in range(V+1)]
    dist[k] = 0
    q = []
    heapq.heappush(q, [0, k])
    while q:
        cost, post = heapq.heappop(q)
        if cost > dist[post]:
            continue
        for p, c in adj[post]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [c, p])
    for i in range(1, V+1):
        print(dist[i] if dist[i] != sys.maxsize else "INF")


V, E = map(int, input().split())
k = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

dijkstra()
