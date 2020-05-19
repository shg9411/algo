import sys
import math
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(cur, lv):
    visited[cur] = True
    depth[cur] = lv
    for other in adj[cur]:
        if visited[other]:
            continue
        parent[other][0] = cur
        dfs(other, lv+1)


def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x
    for i in range(maxLv, -1, -1):
        if depth[y]-depth[x] >= (1 << i):
            y = parent[y][i]
    if x == y:
        return x
    for i in range(maxLv, -1, -1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]
    return parent[x][0]


if __name__ == '__main__':
    N = int(input())
    maxLv = math.ceil(math.log2(N))
    parent = [[0 for _ in range(maxLv+1)] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    depth = [-1 for _ in range(N+1)]
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    dfs(1, 0)
    for j in range(1, maxLv+1):
        for i in range(1, N+1):
            parent[i][j] = parent[parent[i][j-1]][j-1]
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(lca(a, b))
