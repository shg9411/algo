import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for _x, _y in nm:
                tmpx = x+_x
                tmpy = y+_y
                if 0 <= tmpx < h and 0 <= tmpy < w and building[tmpx][tmpy] == '.':
                    building[tmpx][tmpy] = '*'
                    fire.append([tmpx, tmpy])
        for _ in range(len(q)):
            x, y = q.popleft()
            for _x, _y in nm:
                tmpx = x+_x
                tmpy = y+_y
                if 0 <= tmpx < h and 0 <= tmpy < w and building[tmpx][tmpy] == '.':
                    if tmpx == 0 or tmpx == h-1 or tmpy == 0 or tmpy == w-1:
                        print(cnt+1)
                        return True
                    building[tmpx][tmpy] = '@'
                    q.append([tmpx, tmpy])
    return False


for _ in range(T):
    x, y = -1, -1
    w, h = map(int, input().split())
    building = []
    fire = deque()
    for i in range(h):
        building.append(list(input().rstrip()))
        for j in range(w):
            if building[i][j] == '@':
                x, y = i, j
            elif building[i][j] == '*':
                fire.append([i, j])
    if x == 0 or x == h-1 or y == 0 or y == w-1:
        print(1)
        continue
    if not bfs(x, y):
        print("IMPOSSIBLE")
