import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(x,y):
    farm[x][y] = 2
    for move in nm:
        tmpx = x+move[0]
        tmpy = y+move[1]
        if 0<=tmpx<n and 0<=tmpy<m and farm[tmpx][tmpy]==1:
            dfs(tmpx,tmpy)

for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    count = 0

    for i in range(n):
        for j in range(m):
            if farm[i][j]==1:
                count+=1
                dfs(i,j)
    print(count)