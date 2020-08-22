import sys
input = sys.stdin.readline
h, w, m = map(int, input().split())
row = [0 for _ in range(h)]
col = [0 for _ in range(w)]
info = dict()
tmpx = 0
tmpy = 0
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x not in info:
        info[x] = set()
    info[x].add(y)
    row[x] += 1
    if row[x] > tmpx:
        tmpx = row[x]
    col[y] += 1
    if col[y] > tmpy:
        tmpy = col[y]

xset = []
yset = []
for idx, v in enumerate(row):
    if tmpx == v:
        xset.append(idx)
for idx, v in enumerate(col):
    if tmpy == v:
        yset.append(idx)
res = 0
for x in xset:
    for y in yset:
        tmp = row[x]+col[y]
        if x in info and y in info[x]:
            tmp -= 1
        res = max(res, tmp)
print(res)
