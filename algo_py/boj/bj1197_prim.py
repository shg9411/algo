import sys
import heapq
input = sys.stdin.readline


def prim(v):
    q = []
    visited = {v: 0}

    for info in adj[v]:
        heapq.heappush(q, info)
    while q:
        cost, vertex = heapq.heappop(q)
        if vertex in visited:
            continue
        visited[vertex] = cost
        for x in adj[vertex]:
            heapq.heappush(q, x)
        if len(visited) == V:
            return sum(visited.values())
    return 0


V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

print(prim(1))
