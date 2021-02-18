import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    life = N*N-M
    area = []
    virus = []
    check = [[0]*N for _ in range(N)]
    for i in range(N):
        area.append(list(map(int, input().split())))
        for j in range(N):
            if area[i][j] == 2:
                area[i][j] = 0
                virus.append([i, j])
                check[i][j] = 1
            elif area[i][j] == 1:
                life -= 1

    res = 987654321
    for comb in combinations(range(len(virus)), M):
        tmpArea = [area[i][:] for i in range(N)]
        tmpLife = life
        q = deque()
        for idx in comb:
            x, y = virus[idx]
            tmpArea[x][y] = 2
            q.append(virus[idx])
        t = tmp = 0
        while 1:
            c = 0
            for _ in range(len(q)):
                x, y = q.popleft()
                if x > 0 and not tmpArea[x-1][y]:
                    if not check[x-1][y]:
                        c = 1
                    tmpArea[x-1][y] = 2
                    tmpLife -= 1
                    q.append([x-1, y])
                if y > 0 and not tmpArea[x][y-1]:
                    if not check[x][y-1]:
                        c = 1
                    tmpArea[x][y-1] = 2
                    tmpLife -= 1
                    q.append([x, y-1])
                if x < N-1 and not tmpArea[x+1][y]:
                    if not check[x+1][y]:
                        c = 1
                    tmpArea[x+1][y] = 2
                    tmpLife -= 1
                    q.append([x+1, y])
                if y < N-1 and not tmpArea[x][y+1]:
                    if not check[x][y+1]:
                        c = 1
                    tmpArea[x][y+1] = 2
                    tmpLife -= 1
                    q.append([x, y+1])
            if not q:
                break
            tmp += 1
            if c:
                t += tmp
                tmp = 0
        if tmpLife == 0:
            res = min(res, t)
    print(res if res < 987654321 else -1)
