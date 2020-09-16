import sys
input = sys.stdin.readline


def solve():
    n, m, v = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    for _ in range(m):
        u, uu = map(int, input().split())
        edge[u].append(uu)
        edge[uu].append(u)

    for i in range(1, n+1):
        edge[i].sort()

    visit = [0 for _ in range(n+1)]

    def dfs(v):
        visit[v] = 1
        dfsRes.append(v)
        for e in edge[v]:
            if not visit[e]:
                visit[e] = 1
                dfs(e)

    def bfs(v):
        visit = [0 for _ in range(n+1)]
        visit[v] = 1
        bfsRes.append(v)
        q = [v]
        while q:
            tmp = q.pop(0)
            for e in edge[tmp]:
                if not visit[e]:
                    bfsRes.append(e)
                    q.append(e)
                    visit[e] = 1

    dfsRes = []
    bfsRes = []
    dfs(v)
    bfs(v)
    print(*dfsRes)
    print(*bfsRes)


if __name__ == "__main__":
    solve()
