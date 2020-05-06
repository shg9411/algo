import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]

visited = set()


def bfs(idx):
    q = []
    q.append(idx)
    while q:
        tmp = q.pop(0)
        for i in edge[tmp]:
            if i not in visited:
                visited.add(i)
                q.append(i)


for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)


count = 0

for i in range(1, n+1):
    if i not in visited:
        visited.add(i)
        bfs(i)
        count += 1


print(count)
