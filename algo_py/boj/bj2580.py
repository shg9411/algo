if __name__ == '__main__':
    m = [list(map(int, input().split()))for _ in range(9)]
    x = [[0]*10 for _ in range(9)]
    y = [[0]*10 for _ in range(9)]
    sq = [[0]*10 for _ in range(9)]
    get = [[i//3*3+j//3 for j in range(9)]for i in range(9)]
    todo = []
    for i in range(9):
        for j in range(9):
            if m[i][j] == 0:
                todo.append((i, j))
            else:
                x[i][m[i][j]] = 1
                y[j][m[i][j]] = 1
                sq[get[i][j]][m[i][j]] = 1

    def solve(c):
        if len(todo) == c:
            for i in range(9):
                print(*m[i])
            exit()
        i, j = todo[c]
        for can in range(1, 10):
            if x[i][can] or y[j][can] or sq[get[i][j]][can]:
                continue
            m[i][j] = can
            x[i][can] = y[j][can] = sq[get[i][j]][can] = 1
            solve(c+1)
            x[i][can] = y[j][can] = sq[get[i][j]][can] = 0

    solve(0)
