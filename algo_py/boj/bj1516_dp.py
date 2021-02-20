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

    n = int(input())
    adj = [[] for _ in range(n+1)]
    dp = [-1]*(n+1)
    t = [0]*(n+1)
    for i in range(1, n+1):
        time, *others = map(int, input().split()[:-1])
        t[i] = time
        if not others:
            dp[i] = t[i]
        else:
            adj[i].extend(others)
    sys.stdout.write('\n'.join(map(str, [dfs(i) for i in range(1, n+1)])))


if __name__ == "__main__":
    solve()
