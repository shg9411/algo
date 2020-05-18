import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
visited = [[False for _ in range(C)] for _ in range(R)]
miro = []
jh = deque()
fire = deque()
for i in range(R):
    miro.append(list(input().rstrip()))
    for j in range(C):
        if miro[i][j] == '.':
            continue
        visited[i][j] = True
        if miro[i][j] == 'J':
            jh.append([i, j])
        elif miro[i][j] == 'F':
            fire.append([i, j])
cnt = 0
while jh:
    cnt += 1
    for _ in range(len(fire)):
        i, j = fire.popleft()
        if i > 0 and not visited[i-1][j]:
            visited[i-1][j] = True
            fire.append([i-1, j])
        if i < R-1 and not visited[i+1][j]:
            visited[i+1][j] = True
            fire.append([i+1, j])
        if j > 0 and not visited[i][j-1]:
            visited[i][j-1] = True
            fire.append([i, j-1])
        if j < C-1 and not visited[i][j+1]:
            visited[i][j+1] = True
            fire.append([i, j+1])
    for _ in range(len(jh)):
        i, j = jh.popleft()
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            print(cnt)
            exit()
        if i > 0 and not visited[i-1][j]:
            visited[i-1][j] = True
            jh.append([i-1, j])
        if i < R-1 and not visited[i+1][j]:
            visited[i+1][j] = True
            jh.append([i+1, j])
        if j > 0 and not visited[i][j-1]:
            visited[i][j-1] = True
            jh.append([i, j-1])
        if j < C-1 and not visited[i][j+1]:
            visited[i][j+1] = True
            jh.append([i, j+1])
print("IMPOSSIBLE")