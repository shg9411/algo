import sys
import heapq
input = sys.stdin.readline
n, e = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edge[a].append([b, c])
    edge[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(a, b):
    dist = [sys.maxsize for _ in range(n+1)]
    dist[a] = 0
    hq = [[0, a]]

    while hq:
        cost, pos = heapq.heappop(hq)
        if dist[pos] < cost:
            continue
        for p, c in edge[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(hq, [c, p])
    return dist[b]


res = min(dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n),
          dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n))
print(res if res < sys.maxsize else -1)
