import sys
input = sys.stdin.readline


def dfs(i):
    for c in adj[i]:
        if visited[c]:
            continue
        visited[c] = True
        if tm[c] == -1 or dfs(tm[c]):
            tm[c] = i
            return True
    return False


def can(i, j):
    if t[j]*0.75 >= c[i] >= t[j]*0.5 or t[j]*1.25 >= c[i] >= t[j]:
        return True
    return False


n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]
c = [int(input()) for _ in range(m)]
tm = [-1 for _ in range(n)]
adj = [[] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if can(i, j):
            adj[i].append(j)
r = 0
for i in range(m):
    visited = [False for _ in range(n)]
    if dfs(i):
        r += 1
print(r)
