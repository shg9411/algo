from heapq import heappush, heappop
import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n = int(input())
    m = int(input())

    adj = [dict() for _ in range(n+1)]

    for _ in range(m):
        s, e, c = map(int, input().split())
        if e in adj[s]:
            adj[s][e] = min(adj[s][e], c)
        else:
            adj[s][e] = c

    start, end = map(int, input().split())

    def dijkstra():
        dist = [sys.maxsize for _ in range(n+1)]
        dist[start] = 0
        hq = [(0, start)]
        while hq:
            cost, now = heappop(hq)
            if dist[now] < cost:
                continue
            if now==end:
                print(cost)
                exit()
            for nxt, ncost in adj[now].items():
                ncost += cost
                if dist[nxt] > ncost:
                    dist[nxt] = ncost
                    heappush(hq, (ncost, nxt))
    dijkstra()


if __name__ == '__main__':
    solve()