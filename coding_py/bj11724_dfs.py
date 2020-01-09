import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0


def dfs(idx):
    visited[idx] = True
    for num in edge[idx]:
        if not visited[num]:
            dfs(num)


for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
