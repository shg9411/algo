import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(n)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

q = deque()
q.append((0, 0, False))
res = 1
can = False
while q:
    length = len(q)
    for _ in range(length):
        i, j, x = q.popleft()
        if i == n-1 and j == m-1:
            print(res)
            can = True
            exit()
        if i > 0:
            if miro[i-1][j] == '0':
                if not visited[x][i-1][j]:
                    visited[x][i-1][j] = True
                    q.append((i-1, j, x))
            else:
                if not x and not visited[x][i-1][j]:
                    visited[x][i-1][j] = True
                    q.append((i-1, j, True))
        if j > 0:
            if miro[i][j-1] == '0':
                if not visited[x][i][j-1]:
                    visited[x][i][j-1] = True
                    q.append((i, j-1, x))
            else:
                if not x and not visited[x][i][j-1]:
                    visited[x][i][j-1] = True
                    q.append((i, j-1, True))
        if i+1 < n:
            if miro[i+1][j] == '0':
                if not visited[x][i+1][j]:
                    visited[x][i+1][j] = True
                    q.append((i+1, j, x))
            else:
                if not x and not visited[x][i+1][j]:
                    visited[x][i+1][j] = True
                    q.append((i+1, j, True))
        if j+1 < m:
            if miro[i][j+1] == '0':
                if not visited[x][i][j+1]:
                    visited[x][i][j+1] = True
                    q.append((i, j+1, x))
            else:
                if not x and not visited[x][i][j+1]:
                    visited[x][i][j+1] = True
                    q.append((i, j+1, True))

    res += 1

if not can:
    print(-1)