from collections import deque


def solve():
    global ans
    n, m = map(int, input().split())
    lab = []
    virus = []
    res = -3
    ans = 0
    for i in range(n):
        lab.append(list(map(int, input().split())))
        for j in range(m):
            if lab[i][j] == 2:
                virus.append((i, j))
            elif lab[i][j] == 0:
                res += 1

    def bfs():
        tmpV = deque(virus)
        tr = res
        while tmpV:
            i, j = tmpV.popleft()
            if i > 0 and lab[i-1][j] == 0:
                tmpV.append((i-1, j))
                lab[i-1][j] = 3
                tr -= 1
            if j > 0 and lab[i][j-1] == 0:
                tmpV.append((i, j-1))
                lab[i][j-1] = 3
                tr -= 1
            if i < n-1 and lab[i+1][j] == 0:
                tmpV.append((i+1, j))
                lab[i+1][j] = 3
                tr -= 1
            if j < m-1 and lab[i][j+1] == 0:
                tmpV.append((i, j+1))
                lab[i][j+1] = 3
                tr -= 1
        for i in range(n*m):
            x, y = i//m, i % m
            if lab[x][y] == 3:
                lab[x][y] = 0
        return tr

    def dfs(idx, cnt):
        global ans
        if cnt == 3:
            ans = max(ans, bfs())
            return
        for i in range(idx, n*m):
            x, y = i//m, i % m
            if lab[x][y] == 0:
                lab[x][y] = 1
                dfs(i+1, cnt+1)
                lab[x][y] = 0

    dfs(0, 0)
    print(ans)


if __name__ == '__main__':
    solve()
