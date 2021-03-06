import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    nm = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    nmmap = [list(map(int, input().rstrip())) for _ in range(n)]
    resmap = [x[:] for x in nmmap]
    group = [[0]*m for _ in range(n)]

    def bfs(i, j, num):
        group[i][j] = num
        q = [(i, j)]
        cnt = deque([(i, j)])
        while cnt:
            x, y = cnt.popleft()
            for _x, _y in nm:
                tmpx, tmpy = x+_x, y+_y
                if 0 <= tmpx < n and 0 <= tmpy < m and nmmap[tmpx][tmpy] == 0 and group[tmpx][tmpy] == 0:
                    group[tmpx][tmpy] = num
                    cnt.append((tmpx, tmpy))
                    q.append((tmpx, tmpy))
        count = len(q)
        for x, y in q:
            nmmap[x][y] = count

    def get(x, y):
        cnt = 1
        include = set()
        for _x, _y in nm:
            tmpx, tmpy = x+_x, y+_y
            if 0 <= tmpx < n and 0 <= tmpy < m:
                if (gr := group[tmpx][tmpy]) and gr not in include:
                    cnt += nmmap[tmpx][tmpy]
                    include.add(gr)
        return cnt

    num = 2
    for i in range(n):
        for j in range(m):
            if nmmap[i][j] == 0:
                bfs(i, j, num)
                num += 1

    for i in range(n):
        for j in range(m):
            if nmmap[i][j] == 1 and not group[i][j]:
                resmap[i][j] = get(i, j) % 10

    for line in resmap:
        print(''.join(map(str, line)))


if __name__ == '__main__':
    solve()
