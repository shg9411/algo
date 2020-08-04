import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
miro = [list(map(int, list(input().rstrip()))) for _ in range(n)]
cnt = 0
miro[0][0] = 0
q = deque([[0, 0]])
while q:
    cnt += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            print(cnt)
            exit()
        if x > 0 and miro[x-1][y] == 1:
            miro[x-1][y] = 0
            q.append([x-1, y])
        if y > 0 and miro[x][y-1] == 1:
            miro[x][y-1] = 0
            q.append([x, y-1])
        if x < n-1 and miro[x+1][y] == 1:
            miro[x+1][y] = 0
            q.append([x+1, y])
        if y < m-1 and miro[x][y+1] == 1:
            miro[x][y+1] = 0
            q.append([x, y+1])
