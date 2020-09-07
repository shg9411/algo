import sys
input = sys.stdin.readline


def dfs(i, j, cnt):
    if check[i][j] > -1:
        return check[i][j]
    check[i][j] = cnt
    if maap[i][j] == 'L':
        check[i][j] = dfs(i, j-1, cnt)
    elif maap[i][j] == 'R':
        check[i][j] = dfs(i, j+1, cnt)
    elif maap[i][j] == 'U':
        check[i][j] = dfs(i-1, j, cnt)
    else:
        check[i][j] = dfs(i+1, j, cnt)
    return check[i][j]


N, M = map(int, input().split())
maap = [list(input().rstrip()) for _ in range(N)]
check = [[-1 for _ in range(M)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        tmp = dfs(i, j, cnt)
        if tmp == cnt:
            cnt += 1
print(cnt)