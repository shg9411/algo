a = [list(map(int, input().split())) for _ in range(9)]
b, n = [0]*81, 0
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
squ = [[False]*10 for _ in range(9)]

def s(i, j):
    return i//3*3 + j//3

def solve(idx):
    if idx == n:
        for i in range(9):
            print(' '.join(map(str, a[i])))
        exit(0)
    x, y = b[idx]//9, b[idx]%9
    for i in range(1, 10):
        if not (row[x][i] or col[y][i] or squ[s(x,y)][i]):
            row[x][i] = col[y][i] = squ[s(x,y)][i] = True
            a[x][y] = i
            solve(idx+1)
            a[x][y] = 0
            row[x][i] = col[y][i] = squ[s(x,y)][i] = False

for i in range(9):
    for j in range(9):
        k = a[i][j]
        if k:
            row[i][k] = True
            col[j][k] = True
            squ[s(i,j)][k] = True
        else:
            b[n] = i*9 + j
            n += 1
solve(0)
