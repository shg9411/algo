import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve():
    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        m = 0
        for v in adj[u]:
            if dp[v] == -1:
                dp[v] = dfs(v)
            m = max(m, dp[v])
        return m+t[u]

    n, k = map(int, input().split())
    adj = [set() for _ in range(n+1)]
    dp = [-1 for _ in range(n+1)]
    t = [0]+list(map(int, input().split()))
    for _ in range(k):
        x, y = map(int, input().split())
        adj[y].add(x)
    w = int(input())
    print(dfs(w))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
