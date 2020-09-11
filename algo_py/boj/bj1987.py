from collections import deque


def solve():
    r, c = map(int, input().split())
    bd = [[0 for _ in range(c)] for _ in range(r)]
    nm = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    for i in range(r):
        for j,x in enumerate(input()):
            bd[i][j] = 1 << (ord(x)-65)
    tm = [[0 for _ in range(c)] for _ in range(r)]
    res = 1
    q = deque([(0, 0, bd[0][0], 1)])
    while q:
        x, y, msk, l = q.popleft()
        if l > res:
            res = l
        for _x, _y in nm:
            tx = x+_x
            ty = y+_y
            if 0 <= tx < r and 0 <= ty < c:
                if (tmsk := msk | bd[tx][ty]) == msk:
                    continue
                if tm[tx][ty] != tmsk:
                    q.append((tx, ty, tmsk, l+1))
                    tm[tx][ty] = tmsk
    print(res)


if __name__ == '__main__':
    solve()