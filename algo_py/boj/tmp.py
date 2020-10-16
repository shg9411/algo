from collections import deque
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(x, y):
    t = [(x, y)]
    tq = deque([(x, y)])
    s = m[x][y]
    v[x][y] = 1
    while tq:
        x, y = tq.popleft()
        for _x, _y in nm:
            tx = x+_x
            ty = y+_y
            if 0 <= tx < n and 0 <= ty < n and not v[tx][ty]:
                diff = abs(m[x][y]-m[tx][ty])
                if l <= diff <= r:
                    v[tx][ty] = 1
                    s += m[tx][ty]
                    tq.append((tx, ty))
                    t.append((tx, ty))
    if (size := len(t)) > 1:
        num = s//size
        for i in range(size):
            x, y = t[i]
            m[x][y] = num
            q.append((x, y))
        return 0
    else:
        return 1


def c(x, y):
    for _x, _y in nm:
        if 0 <= (tx := x-1):
            diff = abs(m[tx][y]-m[x][y])
            if l <= diff <= r:
                return 0
        if 0 <= (ty := y-1):
            diff = abs(m[x][ty]-m[x][y])
            if l <= diff <= r:
                return 0
        if (tx := x+1) < n:
            diff = abs(m[tx][y]-m[x][y])
            if l <= diff <= r:
                return 0
        if (ty := y+1) < n:
            diff = abs(m[x][ty]-m[x][y])
            if l <= diff <= r:
                return 0
    return 1


n, l, r = map(int, input().split())
m = [[] for _ in range(n)]
cnt = 0
q = deque()
for i in range(n):
    m[i] = list(map(int, input().split()))
    for j in range(n):
        q.append((i, j))
f = 0
while not f:
    v = [[0]*n for _ in range(n)]
    f = 1
    sz = len(q)
    for _ in range(sz):
        x, y = q.popleft()
        if v[x][y] or c(x, y):
            continue
        if not bfs(x, y):
            f = 0
    if not f:
        cnt += 1
print(cnt)
