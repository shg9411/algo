import sys
input = sys.stdin.readline

nm = [(-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]

H, W = map(int, input().split())
top = []
q = []
for i in range(H):
    top.append(list(input().rstrip()))
    for j in range(W):
        if top[i][j] == '.':
            q.append([i, j])
            top[i][j] = 0
        else:
            top[i][j] = int(top[i][j])
res = 0
while q:
    res += 1
    tmp = []
    for x, y in q:
        for _x, _y in nm:
            tmpx, tmpy = x+_x, y+_y
            if not (0 <= tmpx < H and 0 <= tmpy < W):
                continue
            if top[tmpx][tmpy] <= 0:
                continue
            top[tmpx][tmpy] -= 1
            if top[tmpx][tmpy] == 0:
                tmp.append([tmpx, tmpy])
    q = tmp
print(res-1)