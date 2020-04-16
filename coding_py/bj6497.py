import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if level[x] < level[y]:
        parent[x] = y
    elif level[x] < level[y]:
        parent[y] = x
    else:
        parent[x] = y
        level[y] += 1


def kruskal():
    cnt = res = 0
    for c, a, b in hq:
        if find(a) == find(b):
            continue
        cnt += 1
        res += c
        union(a, b)
        if cnt == m-1:
            return res


while 1:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    level = [-1 for i in range(m)]
    parent = [i for i in range(m)]
    hq = []
    tmp = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        hq.append([z, x, y])
        tmp += z
    hq.sort()
    print(tmp-kruskal())
