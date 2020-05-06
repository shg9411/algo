sudoku = []
row = [[False for _ in range(9)] for _ in range(9)]
col = [[False for _ in range(9)] for _ in range(9)]
sqare = [[False for _ in range(9)] for _ in range(9)]
haveto = []

for i in range(9):
    sudoku.append(list(map(int, list(input().rstrip()))))
    for j in range(9):
        num = sudoku[i][j]-1
        if num != -1:
            row[i][num] = True
            col[j][num] = True
            sqare[i//3*3 + j//3][num] = True
        else:
            haveto.append([i, j])


def dfs(idx):
    if idx == len(haveto):
        for line in sudoku:
            print(''.join(map(str, line)))
        exit()

    x, y = haveto[idx][0], haveto[idx][1]

    for i in range(9):
        if row[x][i] or col[y][i] or sqare[x//3*3 + y//3][i]:
            continue
        row[x][i] = col[y][i] = sqare[x//3*3+y//3][i] = True
        sudoku[x][y] = i+1
        dfs(idx+1)
        row[x][i] = col[y][i] = sqare[x//3*3+y//3][i] = False


dfs(0)
