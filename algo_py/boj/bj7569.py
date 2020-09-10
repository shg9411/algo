import sys
from collections import deque
input = sys.stdin.readline


def solve():
    m, n, h = map(int, input().split())
    tomato = [[] for _ in range(h)]
    haveto = 0
    tmt = deque()
    for k in range(h):
        for i in range(n):
            tomato[k].append(input().split())
            for j in range(m):
                if tomato[k][i][j] == '0':
                    haveto += 1
                elif tomato[k][i][j] == '1':
                    tmt.append((k, i, j))
    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            hh, x, y = tmt.popleft()
            if x > 0 and tomato[hh][x-1][y] == '0':
                tomato[hh][x-1][y] = 1
                tmt.append((hh, x-1, y))
                haveto -= 1
            if y > 0 and tomato[hh][x][y-1] == '0':
                tomato[hh][x][y-1] = 1
                tmt.append((hh, x, y-1))
                haveto -= 1
            if x < n-1 and tomato[hh][x+1][y] == '0':
                tomato[hh][x+1][y] = 1
                tmt.append((hh, x+1, y))
                haveto -= 1
            if y < m-1 and tomato[hh][x][y+1] == '0':
                tomato[hh][x][y+1] = 1
                tmt.append((hh, x, y+1))
                haveto -= 1
            if hh > 0 and tomato[hh-1][x][y] == '0':
                tomato[hh-1][x][y] = 1
                tmt.append((hh-1, x, y))
                haveto -= 1
            if hh < h-1 and tomato[hh+1][x][y] == '0':
                tomato[hh+1][x][y] = 1
                tmt.append((hh+1, x, y))
                haveto -= 1
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    solve()
