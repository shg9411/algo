import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = 1e9


def solve():
    def dijkstra(ro):
        dist = [INF for _ in range(N+1)]
        dist[X] = 0
        q = [(0, X)]
        while q:
            cost, pos = heappop(q)
            if dist[pos] < cost:
                continue
            for p, c in ro[pos]:
                c += cost
                if c < dist[p]:
                    dist[p] = c
                    heappush(q, (c, p))
        return dist[1:]

    N, M, X = map(int, input().split())
    road = [[] for _ in range(N+1)]
    back = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, t = map(int, input().split())
        road[u].append([v, t])
        back[v].append([u, t])
    print(max([a+b for (a, b) in zip(dijkstra(road), dijkstra(back))]))

if __name__ == '__main__':
    solve()