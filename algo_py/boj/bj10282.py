import sys
import heapq
MAX = 1e9
input = sys.stdin.readline


def solve():
    def dijkstra(u):
        dist = [MAX]*(n+1)
        dist[u] = 0
        q = [(0, u)]
        while q:
            t, u = heapq.heappop(q)
            if t > dist[u]:
                continue
            for v, tt in adj[u]:
                tt += t
                if tt >= dist[v]:
                    continue
                dist[v] = tt
                heapq.heappush(q, (tt, v))
        resc = rest = 0
        for time in dist:
            if time < MAX:
                resc += 1
                if rest < time:
                    rest = time
        print(resc, rest)

    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s))
    dijkstra(c)


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
