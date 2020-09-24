import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


if __name__ == '__main__':
    def dfs(u):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dfs(v)
        stack.append(u)

    def get(u, v):
        scc[v].append(u)
        for n in adj_r[u]:
            if not visited[n]:
                visited[n] = True
                get(n, v)

    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    adj_r = [[] for _ in range(V+1)]
    scc = [[] for _ in range(V+1)]
    stack = []

    res = 0
    for i in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj_r[v].append(u)
    visited = [False for _ in range(V+1)]
    for i in range(1, V+1):
        if not visited[i]:
            visited[i] = True
            dfs(i)
    visited = [False for _ in range(V+1)]

    while stack:
        tmp = stack.pop()
        if not visited[tmp]:
            visited[tmp] = True
            get(tmp, res)
            res += 1
    res = []
    for c in scc:
        if c:
            c.sort()
            res.append(c)
    res.sort()
    print(len(res))
    for c in res:
        print(' '.join(map(str, c)), end=' -1\n')