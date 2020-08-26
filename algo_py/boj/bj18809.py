from itertools import combinations
from collections import deque


def bfs(gq, rq):
    tmpGarden = [garden[i][:] for i in range(N)]
    cnt = 0
    for i, j in gq:
        tmpGarden[i][j] = 0
    for i, j in rq:
        tmpGarden[i][j] = 0
    val = 2
    while gq and rq:
        gl = len(gq)
        for _ in range(gl):
            x, y = gq.popleft()
            if tmpGarden[x][y] < 0:
                continue
            if x > 0 and tmpGarden[x-1][y] == 1:
                tmpGarden[x-1][y] = val
                gq.append([x-1, y])
            if y > 0 and tmpGarden[x][y-1] == 1:
                tmpGarden[x][y-1] = val
                gq.append([x, y-1])
            if x < N-1 and tmpGarden[x+1][y] == 1:
                tmpGarden[x+1][y] = val
                gq.append([x+1, y])
            if y < M-1 and tmpGarden[x][y+1] == 1:
                tmpGarden[x][y+1] = val
                gq.append([x, y+1])
        rl = len(rq)
        for _ in range(rl):
            x, y = rq.popleft()
            if x > 0:
                if tmpGarden[x-1][y] == 1:
                    tmpGarden[x-1][y] = -val
                    rq.append([x-1, y])
                elif tmpGarden[x-1][y] == val:
                    tmpGarden[x-1][y] = -val
                    cnt += 1
            if y > 0:
                if tmpGarden[x][y-1] == 1:
                    tmpGarden[x][y-1] = -1
                    rq.append([x, y-1])
                elif tmpGarden[x][y-1] == val:
                    tmpGarden[x][y-1] = -val
                    cnt += 1
            if x < N-1:
                if tmpGarden[x+1][y] == 1:
                    tmpGarden[x+1][y] = -val
                    rq.append([x+1, y])
                elif tmpGarden[x+1][y] == val:
                    tmpGarden[x+1][y] = -val
                    cnt += 1
            if y < M-1:
                if tmpGarden[x][y+1] == 1:
                    tmpGarden[x][y+1] = -val
                    rq.append([x, y+1])
                elif tmpGarden[x][y+1] == val:
                    tmpGarden[x][y+1] = -val
                    cnt += 1
        val += 1
    return cnt


if __name__ == '__main__':
    N, M, G, R = map(int, input().split())
    garden = []
    spoil = []
    for i in range(N):
        garden.append(list(map(int, input().split())))
        for j in range(M):
            if garden[i][j] == 2:
                spoil.append((i, j))
                garden[i][j] = 1
    res = 0
    for comb in combinations(range(len(spoil)), G+R):
        comb = set(comb)
        for g in combinations(comb, G):
            g = set(g)
            green = deque(spoil[i] for i in g)
            red = deque(spoil[i] for i in comb-g)
            res = max(res, bfs(green, red))
    print(res)
