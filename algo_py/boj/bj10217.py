import sys
import heapq
input = sys.stdin.readline


def solve():
    N, M, K = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        adj[u].append((v, c, d))
    dist = [[sys.maxsize for _ in range(M+1)] for _ in range(N+1)]
    q = []
    dist[1][0] = 0
    heapq.heappush(q, (0, 0, 1))
    res = -1
    while q:
        time, cost, here = heapq.heappop(q)
        if dist[here][cost] < time:
            continue
        if here == N:
            res = time
            break
        for nxt, nc, nt in adj[here]:
            nt += time
            nc += cost
            if nc > M or dist[nxt][nc] <= nt:
                continue
            for i in range(nc, M+1):
                if dist[nxt][i] > nt:
                    dist[nxt][i] = nt
                else:
                    break
            heapq.heappush(q, (nt, nc, nxt))
    print("Poor KCM" if res == -1 else res)
    return


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()
