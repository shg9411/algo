import sys
import heapq
input = sys.stdin.readline


def dijkstra(s, e):
    dist = [sys.maxsize for _ in range(n+1)]
    tmp = []
    dist[s] = 0
    index = [0 for _ in range(n+1)]
    q = []
    heapq.heappush(q, [0, s])
    while q:
        cost, post = heapq.heappop(q)
        if cost > dist[post]:
            continue
        for p, c in adj[post].items():
            c += cost
            if c < dist[p]:
                dist[p] = c
                index[p] = post
                heapq.heappush(q, [c, p])
    res = []
    tmp = e
    while tmp:
        res.append(tmp)
        tmp = index[tmp]
    return dist[e], res[::-1]


n = int(input())
m = int(input())
adj = [dict() for _ in range(n+1)]
for _ in range(m):
    x, y, c = map(int, input().split())
    if adj[x].get(y):
        adj[x][y] = min(c, adj[x].get(y))
    else:
        adj[x][y] = c

s, e = map(int, input().split())
money, res = dijkstra(s, e)
print(money)
print(len(res))
print(*res)
