import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,checked):
    changed = [(x,y)]
    total = people[x][y]
    q = deque()
    q.append((x,y))
    while q:
        i,j = q.popleft()
        cur = people[i][j]
        if i > 0:
            if not visited[i-1][j] and L<=abs(cur-people[i-1][j])<=R:
                visited[i-1][j] = True
                q.append((i-1,j))
                changed.append((i-1,j))
                total+=people[i-1][j]
        if j > 0:
            if not visited[i][j-1] and L<=abs(cur-people[i][j-1])<=R:
                visited[i][j-1] = True
                q.append((i,j-1))
                changed.append((i,j-1))
                total+=people[i][j-1]
        if i < N-1:
            if not visited[i+1][j] and L<=abs(cur-people[i+1][j])<=R:
                visited[i+1][j] = True
                q.append((i+1,j))
                changed.append((i+1,j))
                total+=people[i+1][j]
        if j < N-1:
            if not visited[i][j+1] and L<=abs(cur-people[i][j+1])<=R:
                visited[i][j+1] = True
                q.append((i,j+1))
                changed.append((i,j+1))
                total+=people[i][j+1]
    if len(changed)>1:
        val = total//len(changed)
        for x,y in changed:
            people[x][y] = val
        return True
    return checked

N,L,R = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while 1:
    visited = [[False for _ in range(N)] for _ in range(N)]
    checked = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                checked = bfs(i,j,checked)
    if checked:
        cnt+=1
    else:
        break
print(cnt)