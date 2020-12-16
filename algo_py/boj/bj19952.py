from collections import deque
nm = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve():
    H, W, O, F, sx, sy, ex, ey = map(int, input().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    m = [[0]*W for _ in range(H)]
    v = [[0]*W for _ in range(H)]
    for _ in range(O):
        x, y, l = map(int, input().split())
        m[x-1][y-1] = l
    q = deque([(sx, sy, F)])
    v[sx][sy] = 1
    while q:
        cx, cy, cf = q.popleft()
        if cx == ex and cy == ey:
            print("잘했어!!")
            return
        for _x, _y in nm:
            tx, ty = cx+_x, cy+_y
            if 0 <= tx < H and 0 <= ty < W and not v[tx][ty]:
                if m[tx][ty] - m[cx][cy] > cf:
                    continue
                tf = cf-1
                if tf < 0:
                    continue
                q.append((tx, ty, tf))
                v[tx][ty] = 1
    print("인성 문제있어??")


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()