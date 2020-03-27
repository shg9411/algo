import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(map(int, input().split()))for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]

maxV = -1


def fy(x, y):
    global maxV
    tmp = paper[x][y]
    if x == 0:
        if y == 0 or y == m-1:
            return
    elif x == n-1:
        if y == 0 or y == m-1:
            return
    if x == 0:
        tmp += paper[x+1][y] + paper[x][y-1] + paper[x][y+1]
    elif x == n-1:
        tmp += paper[x-1][y] + paper[x][y-1] + paper[x][y+1]
    elif y == 0:
        tmp += paper[x][y+1] + paper[x-1][y] + paper[x+1][y]
    elif y == m-1:
        tmp += paper[x][y-1] + paper[x-1][y] + paper[x+1][y]
    else:
        tmpLine = []
        tmpLine.append(paper[x+1][y] + paper[x][y-1] + paper[x][y+1])
        tmpLine.append(paper[x-1][y] + paper[x][y-1] + paper[x][y+1])
        tmpLine.append(paper[x][y+1] + paper[x-1][y] + paper[x+1][y])
        tmpLine.append(paper[x][y-1] + paper[x-1][y] + paper[x+1][y])
        tmp += max(tmpLine)

    maxV = max(maxV, tmp)


def dfs(x, y, count, total):
    global maxV
    if count == 4:
        maxV = max(maxV, total)
        return
    for move in nm:
        nx = x+move[0]
        ny = y+move[1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if paper[nx][ny] == -1:
                continue
            visited[nx][ny] = True
            dfs(nx, ny, count+1, total+paper[nx][ny])
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        fy(i, j)
        visited[i][j] = False

print(maxV)
