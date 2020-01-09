import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

def bfs(idx):
    visited[idx] = True
    q = []
    q.append(idx)
    while q:
        tmp = q.pop(0)
        for i in edge[tmp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)


count = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1


print(count)
