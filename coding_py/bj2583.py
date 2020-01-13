import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n, k = map(int, input().split())

sqare = [[False for _ in range(n)] for _ in range(m)]
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]

res = 0
area = []


def dfs(i, j):
    sqare[i][j] = True
    tmp = 1
    for mv in nm:
        nx = i+mv[0]
        ny = j+mv[1]
        if 0 <= nx < m and 0 <= ny < n and not sqare[nx][ny]:
            tmp += dfs(nx, ny)
    return tmp

def bfs(i, j):
    q = [[i, j]]
    ta = 0
    while q:
        tmp = q.pop(0)
        ta += 1
        x = tmp[0]
        y = tmp[1]
        for mv in nm:
            nx = x+mv[0]
            ny = y+mv[1]
            if 0 <= nx < m and 0 <= ny < n and not sqare[nx][ny]:
                sqare[nx][ny] = True
                q.append([nx, ny])
    area.append(ta)


for _ in range(k):
    a, b, c, d = map(int, input().split())
    for x in range(b, d):
        for y in range(a, c):
            sqare[x][y] = True


for i in range(m):
    for j in range(n):
        if not sqare[i][j]:
            #bfs
            '''
            res += 1
            sqare[i][j] = True
            bfs(i, j)
            '''
            #dfs
            res += 1
            area.append(dfs(i, j))

print(res)
print(' '.join(map(str, sorted(area))))
