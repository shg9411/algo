import sys
input = sys.stdin.readline

nm = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]


def bfs(x, y, square):
    q = []
    q.append([x, y])
    while q:
        tmp = q.pop(0)
        tmpX = tmp[0]
        tmpY = tmp[1]
        for move in nm:
            nx = tmpX+move[0]
            ny = tmpY+move[1]
            if 0 <= nx < len(square) and 0 <= ny < len(square[0]) and square[nx][ny] == 1:
                square[nx][ny] = 0
                q.append([nx, ny])


while 1:
    w, h = map(int, input().split())
    if w+h == 0:
        break
    square = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if square[i][j] == 1:
                square[i][j] = 0
                bfs(i, j, square)
                count += 1
    print(count)
