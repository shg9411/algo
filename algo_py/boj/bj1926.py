import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))


def bfs(i, j):
    cnt = 1
    q = deque([])
    q.append([i, j])
    while q:
        x, y = q.popleft()
        tmpx = x-1
        if 0 <= tmpx:
            if paper[tmpx][y]:
                paper[tmpx][y] = 0
                q.append([tmpx, y])
                cnt += 1
        tmpy = y-1
        if 0 <= tmpy:
            if paper[x][tmpy]:
                paper[x][tmpy] = 0
                q.append([x, tmpy])
                cnt += 1
        tmpx = x+1
        if tmpx < n:
            if paper[tmpx][y]:
                paper[tmpx][y] = 0
                q.append([tmpx, y])
                cnt += 1
        tmpy = y+1
        if tmpy < m:
            if paper[x][tmpy]:
                paper[x][tmpy] = 0
                q.append([x, tmpy])
                cnt += 1
    return cnt


ans = []
many = 0
for i in range(n):
    for j in range(m):
        if paper[i][j]:
            paper[i][j] = 0
            ans.append(bfs(i, j))
            many += 1

print(many)
print(max(ans) if ans else 0)
