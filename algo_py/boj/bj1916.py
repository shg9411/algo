import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def solve():
    n = int(input())
    m = int(input())

    adj = [dict() for _ in range(n+1)]

    for _ in range(m):
        s, e, c = map(int, input().split())
        if (tc:=adj[s].get(e)):
            adj[s][e]=min(tc, c)
        else:
            adj[s][e]=c

    start, end=map(int, input().split())

    def dijkstra():
        dist=[sys.maxsize for _ in range(n+1)]
        dist[start]=0
        hq=[(0, start)]
        while hq:
            cost, now=heappop(hq)
            if dist[now] < cost:
                continue
            for nxt, ncost in adj[now].items():
                ncost += cost
                if dist[nxt] > ncost:
                    dist[nxt]=ncost
                    heappush(hq, (ncost, nxt))
        print(dist[end])
    dijkstra()


if __name__ == '__main__':
    solve()