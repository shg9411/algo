import sys
from collections import deque
input = sys.stdin.readline
nm = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m, k = map(int, input().split())
if n == m == 1:
    print(1)
    exit()
road = [input().rstrip() for _ in range(n)]
visited = [[k+1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0
q = deque([(0, 0, 0)])
res = 1
while q:
    l = len(q)
    for _ in range(l):
        x, y, c = q.popleft()
        for _x, _y in nm:
            tx = x+_x
            ty = y+_y
            if 0 <= tx < n and 0 <= ty < m:
                if x == n-1 and y == m-1:
                    print(res)
                    exit()
                if visited[tx][ty] > c:
                    if road[tx][ty] == '0':
                        visited[tx][ty] = c
                        q.append((tx, ty, c))
                    else:
                        if c >= k:
                            continue
                        visited[tx][ty] = c
                        q.append((tx, ty, c+1))
    res += 1
print(-1)