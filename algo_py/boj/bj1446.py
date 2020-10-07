import sys
input = sys.stdin.readline


def solve():
    n, d = map(int, input().split())
    adj = [dict() for _ in range(d+1)]
    for _ in range(n):
        s, e, l = map(int, input().split())
        if e > d:
            continue
        if e in adj[s]:
            adj[s][e] = min(adj[s][e], l)
        elif l < e-s:
            adj[s][e] = l
    dist = [10001]*(d+1)
    dist[d] = 0
    for u in range(d-1, -1, -1):
        dist[u] = dist[u+1]+1
        for v in adj[u]:
            dist[u] = min(dist[u], dist[v]+adj[u][v])
    print(dist[0])


if __name__ == '__main__':
    solve()