import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
ground[r][c] = 2
count = 1
while 1:
    curx = r
    cury = c
    for i in range(4):
        nx = r+dx[d]
        ny = c+dy[d]
        d = (d+3) % 4
        if ground[nx][ny] == 0:
            ground[nx][ny] = 2
            count += 1
            r = nx
            c = ny
            break
    if i == 3 and curx == r and cury == c:
        nx = r+dx[(d+3) % 4]
        ny = c+dy[(d+3) % 4]
        if ground[nx][ny] == 1:
            break
        else:
            r = nx
            c = ny

print(count)
