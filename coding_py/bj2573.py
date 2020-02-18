import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
ice = []
iceland = [[] for _ in range(n)]
for i in range(n):
    iceland[i] = list(map(int, input().split()))
    for j in range(m):
        if iceland[i][j] > 0:
            ice.append([i, j])

res = 0
while ice:
    minus = []
    new_ice = []
    for i in range(len(ice)):
        tx = ice[i][0]
        ty = ice[i][1]
        cnt = 0
        if 0 <= tx-1 < n and iceland[tx-1][ty] == 0:
            cnt += 1
        if 0 <= tx+1 < n and iceland[tx+1][ty] == 0:
            cnt += 1
        if 0 <= ty-1 < m and iceland[tx][ty-1] == 0:
            cnt += 1
        if 0 <= ty+1 < m and iceland[tx][ty+1] == 0:
            cnt += 1
        minus.append(cnt)
    for i,[tx,ty] in enumerate(ice):
        if iceland[tx][ty]-minus[i] > 0:
            new_ice.append([tx, ty])
            iceland[tx][ty] -= minus[i]
        else:
            iceland[tx][ty] = 0
    res += 1
    if not new_ice:
        break
    ice = new_ice
    visited = [[False for _ in range(m)] for _ in range(n)]
    tmpVisit = 1
    tmpQ = deque()
    tmpQ.append(ice[0])
    visited[ice[0][0]][ice[0][1]] = True
    while tmpQ:
        tmp = tmpQ.popleft()
        tx = tmp[0]
        ty = tmp[1]
        if iceland[tx-1][ty] > 0 and not visited[tx-1][ty]:
            visited[tx-1][ty] = True
            tmpQ.append([tx-1, ty])
            tmpVisit += 1
        if iceland[tx+1][ty] > 0 and not visited[tx+1][ty]:
            visited[tx+1][ty] = True
            tmpQ.append([tx+1, ty])
            tmpVisit += 1
        if iceland[tx][ty-1] > 0 and not visited[tx][ty-1]:
            visited[tx][ty-1] = True
            tmpQ.append([tx, ty-1])
            tmpVisit += 1
        if iceland[tx][ty+1] > 0 and not visited[tx][ty+1]:
            visited[tx][ty+1] = True
            tmpQ.append([tx, ty+1])
            tmpVisit += 1
    if tmpVisit < len(ice):
        print(res)
        exit(0)
print(0)
