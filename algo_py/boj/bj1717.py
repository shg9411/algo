import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
