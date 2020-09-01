import sys
from collections import deque
input = sys.stdin.readline


def solve():
    def bfs(i, j):
        o, v = 0, 0
        q = deque()
        if by[i][j] == 'o':
            o += 1
        elif by[i][j] == 'v':
            v += 1
        by[i][j] = '#'
        q.append((i, j))
        while q:
            x, y = q.popleft()
            if x > 0 and by[x-1][y] != '#':
                q.append((x-1, y))
                if by[x-1][y] == 'v':
                    v += 1
                elif by[x-1][y] == 'o':
                    o += 1
                by[x-1][y] = '#'
            if y > 0 and by[x][y-1] != '#':
                q.append((x, y-1))
                if by[x][y-1] == 'v':
                    v += 1
                elif by[x][y-1] == 'o':
                    o += 1
                by[x][y-1] = '#'
            if x < r-1 and by[x+1][y] != '#':
                q.append((x+1, y))
                if by[x+1][y] == 'v':
                    v += 1
                elif by[x+1][y] == 'o':
                    o += 1
                by[x+1][y] = '#'
            if y < c-1 and by[x][y+1] != '#':
                q.append((x, y+1))
                if by[x][y+1] == 'v':
                    v += 1
                elif by[x][y+1] == 'o':
                    o += 1
                by[x][y+1] = '#'
        if v >= o:
            o = 0
        else:
            v = 0
        return (v, o)

    r, c = map(int, input().split())
    by = []
    for _ in range(r):
        by.append(list(input().rstrip()))
    resv, reso = 0, 0
    for i in range(r):
        for j in range(c):
            if by[i][j] != '#':
                tv, to = bfs(i, j)
                resv += tv
                reso += to
    print(reso, resv)


if __name__ == '__main__':
    solve()