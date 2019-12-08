n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1


def dfs(current, row, foot):
    foot += [current]
    for search in range(len(row[current])):
        if row[current][search] and search not in foot:
            foot = dfs(search, row, foot)
    return foot


def bfs(start):
    queue = [start]
    foot = [start]
    while queue:
        current = queue.pop(0)
        for search in range(len(matrix[current])):
            if matrix[current][search] and search not in foot:
                foot += [search]
                queue += [search]
    return foot


print(*dfs(v, matrix, []))
print(*bfs(v))
