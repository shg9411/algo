import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve():
    n = int(input())
    adj = [list() for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    md = [0 for _ in range(n+1)]
    for _ in range(n-1):
        x, y, z = map(int, input().split())
        adj[x].append((y, z))

    def dfs(u):
        d = dd = 0
        for v, c in adj[u]:
            dfs(v)
            if d < (tc := md[v]+c):
                dd = d
                d = tc
            elif dd < tc:
                dd = tc
            dp[u] = max(dp[u], d+dd, dp[v])
            md[u] = max(md[u], d)
    dfs(1)
    print(dp[1])


if __name__ == '__main__':
    solve()
