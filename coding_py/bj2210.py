nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]

number = [input().split() for _ in range(5)]
res = set()


def dfs(tmp, x, y):
    if len(tmp) == 6:
        res.add(''.join(tmp))
        return
    for move in nm:
        nx = x+move[0]
        ny = y+move[1]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(tmp+number[nx][ny], nx, ny)


for i in range(25):
    a = i//5
    b = i % 5
    dfs('', a, b)

print(len(res))