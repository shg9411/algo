import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]
visited = set()
count = 0


def dfs(idx):
    visited.add(idx)
    for num in edge[idx]:
        if num not in visited:
            dfs(num)


for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

for i in range(1, n+1):
    if i not in visited:
        count += 1
        dfs(i)

print(count)
