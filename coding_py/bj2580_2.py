sudoku = [list(map(int, input().split()))for _ in range(9)]

notFill = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            notFill.append((i, j))


print(notFill)