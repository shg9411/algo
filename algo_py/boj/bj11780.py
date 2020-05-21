import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[[] for _ in range(n+1)] for _ in range(n+1)]
to = [[[] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = sys.maxsize

for _ in range(m):
    x, y, cost = map(int, input().split())
    dist[x][y] = min(dist[x][y], cost)
    to[x][y] = y


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                to[i][j] = to[i][k]

for i in range(1, len(dist)):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != sys.maxsize else 0, end=' ')
    print()
for i in range(1, len(dist)):
    for j in range(1, n+1):
        if i == j or dist[i][j] == sys.maxsize:
            print(0)
            continue
        tmp = i
        path = []
        while tmp != j:
            path.append(tmp)
            tmp = to[tmp][j]
        path.append(j)
        print(len(path), *path)