import sys
input = sys.stdin.readline
N, K = map(int, input().split())
move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
chess = [list(map(list, zip(map(int, input().split()), [[] for _ in range(N)])))
         for _ in range(N)]
where = []
for i in range(K):
    x, y, dist = map(int, input().split())
    where.append([x-1, y-1, dist])
    chess[x-1][y-1][1].append(i)
turn = 0
while turn < 1000:
    turn += 1
    for i in range(K):
        x, y, dist = where[i][0], where[i][1], where[i][2]
        tmpx = x+move[dist][0]
        tmpy = y+move[dist][1]
        if tmpx >= N or tmpx < 0 or tmpy >= N or tmpy < 0 or chess[tmpx][tmpy][0] == 2:
            if where[i][2] % 2 == 1:
                where[i][2] += 1
            else:
                where[i][2] -= 1
            tmpx = x-move[dist][0]
            tmpy = y-move[dist][1]
            if tmpx >= N or tmpx < 0 or tmpy >= N or tmpy < 0 or chess[tmpx][tmpy][0] == 2:
                continue
        idx = chess[x][y][1].index(i)
        horse = chess[x][y][1][idx:]
        for num in horse:
            where[num][0] = tmpx
            where[num][1] = tmpy
        chess[x][y][1] = chess[x][y][1][:idx]
        if chess[tmpx][tmpy][0] == 0:
            chess[tmpx][tmpy][1].extend(horse)
        else:
            chess[tmpx][tmpy][1].extend(horse[::-1])
        if len(chess[tmpx][tmpy][1]) >= 4:
            print(turn)
            exit()
print(-1)
