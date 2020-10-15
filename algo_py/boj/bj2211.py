import sys
import heapq
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    adj = [dict() for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a][b] = c
        adj[b][a] = c

    dist = [1e9]*(n+1)
    dist[1] = 0
    q = [(0, 1)]
    prev = [-1] * (n+1)
    while q:
        cost, post = heapq.heappop(q)
        if cost > dist[post]:
            continue
        for v, w in adj[post].items():
            w += cost
            if w < dist[v]:
                dist[v] = w
                prev[v] = post
                heapq.heappush(q, (w, v))
    print(n-1)
    for i in range(2, n+1):
        print(i, prev[i])


if __name__ == '__main__':
    solve()
