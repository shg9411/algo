import sys
INF = sys.maxsize

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
lx = [0]*n
ly = [0]*n
max_match = 0
lx = [0]*n
ly = [0]*n
xy = [-1]*n
yx = [-1]*n
s = [0]*n
t = [0]*n
slack = [0]*n
slackx = [0]*n
prev = [0]*n
res = 0


def init_labels():
    for i in range(n):
        for j in range(n):
            lx[i] = max(lx[i], cost[i][j])


def add_to_tree(x, prevx):
    global s, prev, slack, slacky, cost
    s[x] = True
    prev[x] = prevx
    for y in range(n):
        if lx[x] + ly[y] - cost[x][y] < slack[y]:
            slack[y] = lx[x] + ly[y] - cost[x][y]
            slackx[y] = x


def augment():
    global s, t
    if max_match == n:
        return
    wr = rd = root = 0
    q = [0]*n
    s = [0]*n
    t = [0]*n
    prev = [-1]*n
    for x in range(n):
        if xy[x] == -1:
            q[wr] = root = x
            prev[x] = -2
            s[x] = True
            break
    for y in range(n):
        slack[y] = lx[root] + ly[y] - cost[root][y]
        slackx[y] = root

    while 1:
        while rd < wr:
            x = q[rd]
            rd += 1
            for y in range(n):
                if cost[x][y] == lx[x] + ly[y] and not t[y]:
                    if yx[y] == -1:
                        break
                    t[y] = 1
                    q[wr] = yx[y]
                    wr += 1
                    add_to_tree(yx[x], x)
            if y < n:
                break
        if y < n:
            break
        #update_labels()
        wr = rd = 0
        for y in range(n):
            if not t[y] and slack[y] == 0:
                if yx[y] == -1:
                    x = slackx[y]
                    break
                else:
                    t[y] = 1
                    if not s[yx][y]:
                        q[wr] = yx[y]
                        wr += 1
                        add_to_tree(yx[y], slackx[y])
        if y < n:
            break
    if y < n:
        max_match += 1
        cx = x
        cy = y
        while cx != -2:
            ty = xy[cx]
            yx[cy] = cx
            xy[cx] = cy
            cx = prev[cx]
            cy = ty
        augment()


init_labels()
augment()
for x in range(n):
    res += cost[x][xy[x]]
print(res)
