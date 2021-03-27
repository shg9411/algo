import sys
INF = sys.maxsize


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
PHI = -1
NOL = -2
x = [[False]*n for _ in range(n)]
ss = [0]*n
st = [0]*n
v = [0]*n
p = [0]*n
ls = [0]*n
lt = [0]*n
a = [0]*n
u = [0]*n
f = 0
for i in range(n):
    for j in range(n):
        f = max(f, cost[i][j])
for i in range(n):
    u[i] = f
    p[i] = INF
    lt[i] = NOL
    ls[i] = PHI
    a[i] = -1
while 1:
    f = -1
    i = 0
    while i < n and f == -1:
        if ls[i] != NOL and not ss[i]:
            f = i
        i += 1
    if f != -1:
        ss[f] = 1
        for j in range(n):
            if not x[f][j] and u[f] + v[j] - cost[f][j] < p[j]:
                lt[j] = f
                p[j] = u[f]+v[j] - cost[f][j]
    else:
        i = 0
        while i < n and f == -1:
            if lt[i] != NOL and not st[i] and p[i] == 0:
                f = i
            i += 1
        if f == -1:
            d1 = d2 = INF
            d = 0
            for i in u:
                d1 = min(d1, i)
            for i in p:
                if i > 0:
                    d2 = min(d2, i)
            d = min(d1, d2)
            for i in range(n):
                if ls[i] != NOL:
                    u[i] -= d
            for i in range(n):
                if p[i] == 0:
                    v[i] += d
                if p[i] > 0 and lt[i] != NOL:
                    p[i] -= d
            if d2 >= d1:
                break
        else:
            st[f] = 1
            s = -1
            i = 0
            while i < n and s == -1:
                if x[i][f]:
                    s = i
                i += 1
            if s == -1:
                l = r = 0
                while 1:
                    r = f
                    l = lt[r]
                    if r >= 0 and l >= 0:
                        x[l][r] = not x[l][r]
                    else:
                        break
                    r = ls[l]
                    if r >= 0 and l >= 0:
                        x[l][r] = not x[l][r]
                    else:
                        break
                    f = r
                p = [INF]*n
                lt = [NOL]*n
                ls = [NOL]*n
                ss = [0]*n
                st = [0]*n
                for i in range(n):
                    ex = 1
                    j = 0
                    while j < n and ex:
                        ex = not x[i][j]
                        j += 1
                    if ex:
                        ls[i] = PHI
            else:
                ls[s] = f

for i in range(n):
    for j in range(n):
        if x[i][j]:
            a[j] = i
res = 0
for i in range(n):
    print(i, a[i])
    res += cost[a[i]][i]
print(res)
