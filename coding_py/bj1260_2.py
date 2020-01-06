import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

edge = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

for i in range(len(edge)):
    edge[i].sort()

visit = [0] * (n+1)


def dfs(v):
    visit[v] = 1
    dfsRes.append(v)
    for e in edge[v]:
        if visit[e] == 0:
            visit[e] = 1
            dfs(e)


def bfs(v):
    visit = [0] * (n+1)
    visit[v] = 1
    bfsRes.append(v)
    q = [v]
    while q:
        tmp = q.pop(0)
        for e in edge[tmp]:
            if visit[e] == 0:
                bfsRes.append(e)
                q.append(e)
                visit[e] = 1


dfsRes = []
bfsRes = []
dfs(v)
bfs(v)
print(*dfsRes)
print(*bfsRes)
