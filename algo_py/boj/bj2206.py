import sys
from collections import deque
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]
input = sys.stdin.readline
n, m = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(n)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

q = deque([])
q.append([0, 0, False])
res = 1
can = False
while q:
    for _ in range(len(q)):
        i, j, x = q.popleft()
        if i == n-1 and j == m-1:
            print(res)
            can = True
            exit()
        for nx, ny in nm:
            tmpx = i+nx
            tmpy = j+ny
            if 0 <= tmpx < n and 0 <= tmpy < m:
                if miro[tmpx][tmpy] == '0':
                    if not visited[x][tmpx][tmpy]:
                        visited[x][tmpx][tmpy] = True
                        q.append([tmpx, tmpy, x])
                else:
                    if not x and not visited[x][tmpx][tmpy]:
                        visited[x][tmpx][tmpy] = True
                        q.append([tmpx, tmpy, True])
    res += 1

if not can:
    print(-1)
