n, m = map(int, input().split())
r, c, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
U, R, D, L = 0, 1, 2, 3
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

res = 0
while True:
    if field[r][c] == 0:
        field[r][c] = 2
        res += 1

    for _ in range(4):
        d = (d - 1) % 4
        nr, nc = r + move[d][0], c + move[d][1]
        if field[nr][nc] == 0:
            r, c = nr, nc
            break
    else:
        nr, nc = r - move[d][0], c - move[d][1]
        if field[nr][nc] == 1:
            break
        else:
            r, c = nr, nc

print(res)