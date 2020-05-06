import sys
import copy
input = sys.stdin.readline

x, y = map(int, input().split())
nm = [[-1,0],[0,-1],[1,0],[0,1]]
mapmap = [list(input().rstrip()) for _ in range(x)]
ll = len(mapmap[0])
lll = len(mapmap)
ans = []


def bfs(x, y):
    global ll,lll
    sss = [[-1 for _ in range(ll)] for _ in range(lll)]
    sss[x][y] = 0
    q = [[x, y]]
    while q:
        tmp = q.pop(0)
        tmpX = tmp[0]
        tmpY = tmp[1]
        for move in nm:
            nx = move[0]+tmpX
            ny = move[1]+tmpY
            if 0<=nx<lll and 0<=ny<ll and mapmap[nx][ny] =='L' and sss[nx][ny]==-1:
                q.append([nx,ny])
                sss[nx][ny] = sss[tmpX][tmpY]+1
    ssss = 0
    for i in range(lll):
        for j in range(ll):
            ssss = max(ssss,sss[i][j])
    ans.append(ssss)

for i in range(x):
    for j in range(y):
        if mapmap[i][j] == 'L':
            bfs(i, j)

print(max(ans))