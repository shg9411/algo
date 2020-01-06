import sys
input = sys.stdin.readline
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]
r, c = map(int, input().split())
alpha = [list(input().rstrip()) for _ in range(r)]
check = set()
check.add(alpha[0][0])
res = 1


def dfs(x, y, count):
    global res
    for move in nm:
        nx = x+move[0]
        ny = y+move[1]
        if 0 <= nx < r and 0 <= ny < c and alpha[nx][ny] not in check:
            res = max(res, count+1)
            check.add(alpha[nx][ny])
            dfs(nx, ny, count+1)
            check.remove(alpha[nx][ny])


dfs(0, 0, 1)
print(res)
