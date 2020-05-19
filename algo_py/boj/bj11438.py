import sys
import math
from collections import deque
input = sys.stdin.readline


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
q = deque()
q.append(1)
depth[1] = 0
visited[1] = True
while q:
    tmp = q.popleft()
    for other in adj[tmp]:
        if visited[other]:
            continue
        q.append(other)
        visited[other] = True
        depth[other] = depth[tmp] + 1
        parent[other][0] = tmp

for j in range(1, maxLv+1):
    for i in range(1, N+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
