import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

forest = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
d = ()
s = ()
w = []

for i in range(r):
    for j in range(c):
        if forest[i][j] == 'D':
            d = (i, j)
        elif forest[i][j] == 'S':
            s = (i, j)
        elif forest[i][j] == '*':
            w.append([i, j])


def solve():
    water_q = deque()
    dochi_q = deque()
    water_q.extend(w)
    dochi_q.append(s)
    count = 0
    while 1:
        #print(forest)
        if len(dochi_q) == 0:
            print("KAKTUS")
            break
        count += 1
        for _ in range(len(water_q)):
            tmp_water = water_q.popleft()
            for i in range(4):
                nx = tmp_water[0] + dx[i]
                ny = tmp_water[1] + dy[i]
                if nx >= r or ny >= c or nx < 0 or ny < 0:
                    continue
                if forest[nx][ny] == '.':
                    forest[nx][ny] = '*'
                    water_q.append([nx, ny])
        for _ in range(len(dochi_q)):
            tmp_dochi = dochi_q.popleft()
            for i in range(4):
                nx = tmp_dochi[0] + dx[i]
                ny = tmp_dochi[1] + dy[i]
                if nx >= r or ny >= c or nx < 0 or ny < 0:
                    continue
                if forest[nx][ny] == 'D':
                    print(count)
                    exit(0)
                if forest[nx][ny] == '.':
                    forest[nx][ny] = 'S'
                    dochi_q.append([nx, ny])


solve()
