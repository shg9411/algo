from collections import deque


def solve():
    r, c = map(int, input().split())
    # 입력
    bd = [[0 for _ in range(c)] for _ in range(r)]
    nm = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    for i in range(r):
        tmp = input()
        for j in range(c):
            # 각 칸마다 전처리
            bd[i][j] = 1 << (ord(tmp[j])-65)
    # 같은 알파벳 조합으로 방문했었는지 확인하기 위한 리스트
    tm = [[0 for _ in range(c)] for _ in range(r)]
    msk = bd[0][0]
    res = 1
    q = deque([(0, 0, msk, 1)])
    while q:
        x, y, m, l = q.popleft()
        if l > res:
            res = l
            if res == 26:
                print(26)
                exit()
        for _x, _y in nm:
            tx = x+_x
            ty = y+_y
            if 0 <= tx < r and 0 <= ty < c:
                # 그 칸에 이미 방문했던 알파벳이 있으면 pass
                if (tmsk := m | bd[tx][ty]) == m:
                    continue
                # 같은 알파벳 조합으로 온 적이 없으면 q에 삽입
                if tm[tx][ty] != tmsk:
                    q.append((tx, ty, tmsk, l+1))
                    tm[tx][ty] = tmsk
    print(res)


if __name__ == '__main__':
    solve()
