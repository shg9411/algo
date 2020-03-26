import sys
input = sys.stdin.readline
t = int(input())


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y
        num[y] += num[x]
        num[x] = 1
    return num[y]


for _ in range(t):
    f = int(input())
    cnt = 1
    parent = [i for i in range(f*2)]
    num = [1 for _ in range(f*2)]
    freind = dict()
    for _ in range(f):
        a, b = input().split()
        if a not in freind:
            freind[a] = cnt
            cnt += 1
        if b not in freind:
            freind[b] = cnt
            cnt += 1
        print(union(freind[a], freind[b]))
