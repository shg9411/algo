import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [dict() for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u][v] = w
    tree[v][u] = w


def dfs(u, w):
    global tmpu, tmpval
    dist[u] = w

    if dist[u] > tmpval:
        tmpval, tmpu = dist[u], u

    for vertex, weight in tree[u].items():
        if 0 > dist[vertex]:
            dfs(vertex, w+weight)


dist = [-1 for _ in range(n+1)]
tmpu, tmpval = 0, 0
dfs(1, 0)
dist = [-1 for _ in range(n+1)]
dfs(tmpu, 0)
print(tmpval)
