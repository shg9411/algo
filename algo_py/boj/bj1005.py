import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(10**6)


def solve():
    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        m = max([dp[v] if dp[v] != -1 else dfs(v) for v in adj[u]], default=0)
        dp[u] = m+t[u]
        return dp[u]

    n, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    dp = [-1 for _ in range(n+1)]
    t = [0]+list(map(int, input().split()))
    for _ in range(k):
        x, y = map(int, input().split())
        adj[y].append(x)
    w = int(input())
    print(dfs(w))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
