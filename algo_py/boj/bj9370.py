import sys
import heapq
input = sys.stdin.readline


def solve():
    def dijkstra(s):
        dist = [1e9 for _ in range(n+1)]
        dist[s] = 0
        pre = [0 for _ in range(n+1)]
        q = [(0, s)]
        while q:
            co, po = heapq.heappop(q)
            if co > dist[po]:
                continue
            for p, c in adj[po]:
                c += co
                if c < dist[p]:
                    dist[p] = c
                    pre[p] = po
                    heapq.heappush(q, (c, p))
        return dist

    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        if a == g and b == h or a == h and b == g:
            adj[a].append((b, d*2-1))
            adj[b].append((a, d*2-1))
        else:
            adj[a].append((b, d*2))
            adj[b].append((a, d*2))
    target = sorted([int(input()) for _ in range(t)])
    result = dijkstra(s)
    res = []
    for t in target:
        if result[t] % 2 == 1:
            res.append(t)
    print(*res)


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
