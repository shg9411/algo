import sys
from collections import deque
input = sys.stdin.readline


def solve():
    N, M, K = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        adj[u].append((v, c, d))
    dist = [[sys.maxsize for _ in range(M+1)] for _ in range(N+1)]
    dist[1][0] = 0
    for j in range(M+1):
        for i in range(1, N+1):
            if dist[i][j] == sys.maxsize:
                continue
            time = dist[i][j]
            for nv, nc, nd in adj[i]:
                if nc+j > M:
                    continue
                if dist[nv][nc+j] > time+nd:
                    dist[nv][nc+j] = time+nd
    res = min(dist[N])
    if res == sys.maxsize:
        print("Poor KCM")
    else:
        print(res)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()
