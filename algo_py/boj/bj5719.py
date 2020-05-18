import sys
import heapq
from collections import deque
input = sys.stdin.readline


def dijkstra(s, e):
    dist = [sys.maxsize for _ in range(n)]
    dist[s] = 0
    q = [(0, s)]
    tmp = [set() for _ in range(n)]
    while q:
        cost, des = heapq.heappop(q)
        for to in adj[des]:
            val = cost+adj[des][to]
            if dist[to] < val:
                continue
            dist[to] = val
            tmp[to].add(des)
            heapq.heappush(q, (val, to))
    q = deque([e])
    while q:
        cur = q.popleft()
        for pre in tmp[cur]:
            if cur in adj[pre] and dist[cur] == adj[pre][cur] + dist[pre]:
                q.append(pre)
                adj[pre].pop(cur)
    dist = [sys.maxsize for _ in range(n)]
    dist[s] = 0
    q = [(0, s)]
    while q:
        cost, des = heapq.heappop(q)
        for to in adj[des]:
            val = cost+adj[des][to]
            if dist[to] <= val:
                continue
            dist[to] = val
            heapq.heappush(q, (val, to))
    return dist[e]


while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    s, d = map(int, input().split())
    adj = [dict() for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        adj[u][v] = p
    val = dijkstra(s, d)
    print(val if val != sys.maxsize else -1)
