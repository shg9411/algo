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
        tmpy = y
        if 0 <= tmpx < n and 0 <= tmpy < m:
            if paper[tmpx][tmpy]:
                paper[tmpx][tmpy] = 0
                q.append([tmpx, tmpy])
                cnt += 1
        tmpx = x
        tmpy = y-1
        if 0 <= tmpx < n and 0 <= tmpy < m:
            if paper[tmpx][tmpy]:
                paper[tmpx][tmpy] = 0
                q.append([tmpx, tmpy])
                cnt += 1
        tmpx = x+1
        tmpy = y
        if 0 <= tmpx < n and 0 <= tmpy < m:
            if paper[tmpx][tmpy]:
                paper[tmpx][tmpy] = 0
                q.append([tmpx, tmpy])
                cnt += 1
        tmpx = x
        tmpy = y+1
        if 0 <= tmpx < n and 0 <= tmpy < m:
            if paper[tmpx][tmpy]:
                paper[tmpx][tmpy] = 0
                q.append([tmpx, tmpy])
                cnt += 1
    return cnt


ans = 0
many = 0
for i in range(n):
    for j in range(m):
        if paper[i][j]:
            paper[i][j] = 0
            ans = max(bfs(i, j), ans)
            many += 1

print(many)
print(ans)
