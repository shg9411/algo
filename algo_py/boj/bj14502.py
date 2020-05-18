from collections import deque
from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, input().split())
    area = []
    wall = []
    virus = []
    safe = N*M-3
    res = 0
    for i in range(N):
        area.append(list(map(int, input().split())))
        for j in range(M):
            if area[i][j] == 0:
                wall.append([i, j])
                continue
            safe -= 1
            if area[i][j] == 2:
                virus.append([i, j])
    for comb in combinations(range(len(wall)), 3):
        life = safe
        for idx in comb:
            x, y = wall[idx]
            area[x][y] = 3
        q = deque(virus)
        while q:
            x, y = q.popleft()
            if x > 0 and area[x-1][y] == 0:
                area[x-1][y] = 3
                q.append([x-1, y])
                life -= 1
            if y > 0 and area[x][y-1] == 0:
                area[x][y-1] = 3
                q.append([x, y-1])
                life -= 1
            if x < N-1 and area[x+1][y] == 0:
                area[x+1][y] = 3
                q.append([x+1, y])
                life -= 1
            if y < M-1 and area[x][y+1] == 0:
                area[x][y+1] = 3
                q.append([x, y+1])
                life -= 1
        res = max(res, life)
        for i in range(N):
            for j in range(M):
                if area[i][j] == 3:
                    area[i][j] = 0
    print(res)
