import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]


def bfs(i, j):
    cnt = 1
    q = deque([])
    q.append([i, j])
    while q:
        x, y = q.popleft()
        if (tmpx:=x-1) >= 0:
            if paper[tmpx][y]:
                paper[tmpx][y] = 0
                q.append([tmpx, y])
                cnt += 1
        if 0 <= (tmpy:=y-1):
            if paper[x][tmpy]:
                paper[x][tmpy] = 0
                q.append([x, tmpy])
                cnt += 1
        if (tmpx:=x+1) < n:
            if paper[tmpx][y]:
                paper[tmpx][y] = 0
                q.append([tmpx, y])
                cnt += 1
        if (tmpy:=y+1) < m:
            if paper[x][tmpy]:
                paper[x][tmpy] = 0
                q.append([x, tmpy])
                cnt += 1
    return cnt


ans = []
for i in range(n):
    for j in range(m):
        if paper[i][j]:
            paper[i][j] = 0
            ans.append(bfs(i, j))

print(len(ans))
print(max(ans) if ans else 0)
