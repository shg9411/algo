def solve():
    def dfs(u):
        m = 0
        for v in adj[u]:
            m = max(m, t[v] if vi[v] else dfs(v))
        vi[u] = 1
        t[u] += m
        return t[u]

    n, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    vi = [0 for _ in range(n+1)]
    t = [0]+list(map(int, input().split()))
    for _ in range(k):
        x, y = map(int, input().split())
        adj[y].append(x)
    w = int(input())
    print(dfs(w))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
