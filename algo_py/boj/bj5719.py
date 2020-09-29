import sys
import heapq
from collections import deque
input = sys.stdin.readline


def solve():
    def dijkstra(s, e):
        dist = [sys.maxsize for _ in range(n)]
        dist[s] = 0
        q = [(0, s)]
        while q:
            cost, des = heapq.heappop(q)
            if dist[des] != cost:
                continue
            if des == e:
                break
            for to, val in adj[des].items():
                val += cost
                if dist[to] > val:
                    dist[to] = val
                    heapq.heappush(q, (val, to))
        q = deque([e])
        while q:
            des = q.popleft()
            for i in range(n):
                if des in adj[i] and dist[i]+adj[i][des] == dist[des]:
                    adj[i].pop(des)
                    q.append(i)
        dist = [sys.maxsize for _ in range(n)]
        dist[s] = 0
        q = [(0, s)]
        while q:
            cost, des = heapq.heappop(q)
            if dist[des] != cost:
                continue
            if des == e:
                break
            for to, val in adj[des].items():
                val += cost
                if dist[to] > val:
                    dist[to] = val
                    heapq.heappush(q, (val, to))
        return dist[e]

    while 1:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        s, e = map(int, input().split())
        adj = [dict() for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            adj[u][v] = p
        val = dijkstra(s, e)
        print(val if val != sys.maxsize else -1)


if __name__ == '__main__':
    solve()
