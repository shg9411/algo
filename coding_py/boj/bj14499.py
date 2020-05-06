import sys

nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0]

n, m, x, y, k = map(int, sys.stdin.readline().split())

zido = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dice = [0]*6

command = list(map(int, sys.stdin.readline().split()))


def check(mx, my, d):
    if mx+nx[d] >= n or mx+nx[d] < 0 or my+ny[d] >= m or my+ny[d] < 0:
        return False
    return True


for c in command:
    if check(x, y, c-1):
        x += nx[c-1]
        y += ny[c-1]
        if c == 1:
            dice[3], dice[5], dice[1], dice[2] = dice[2], dice[3], dice[5], dice[1]
            if zido[x][y] == 0:
                zido[x][y] = dice[5]
            else:
                dice[5] = zido[x][y]
                zido[x][y] = 0
            print(dice[2])
        elif c == 2:
            dice[1], dice[5], dice[3], dice[2] = dice[2], dice[1], dice[5], dice[3]
            if zido[x][y] == 0:
                zido[x][y] = dice[5]
            else:
                dice[5] = zido[x][y]
                zido[x][y] = 0
            print(dice[2])
        elif c == 3:
            dice[4], dice[2], dice[0], dice[5] = dice[2], dice[0], dice[5], dice[4]
            if zido[x][y] == 0:
                zido[x][y] = dice[5]
            else:
                dice[5] = zido[x][y]
                zido[x][y] = 0
            print(dice[2])
        else:
            dice[0], dice[5], dice[4], dice[2] = dice[2], dice[0], dice[5], dice[4]
            if zido[x][y] == 0:
                zido[x][y] = dice[5]
            else:
                dice[5] = zido[x][y]
                zido[x][y] = 0
            print(dice[2])
