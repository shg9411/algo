import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]
q = deque()
box = []
for i in range(n):
    line = list(map(int, input().split()))
    box.append(line)
    for j in range(m):
        if line[j] == 1:
            q.append((i, j))

day = -1

while q:
    tmpq = deque()
    for _ in range(len(q)):
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]
        for move in nm:
            nx = x+move[0]
            ny = y+move[1]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = 1
                tmpq.append((nx, ny))
    q = tmpq
    day += 1

for line in box:
    if 0 in line:
        print(-1)
        exit()

print(day)
