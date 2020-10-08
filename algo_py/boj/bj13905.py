import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def f(x):
    if p[x] == x:
        return x
    p[x] = f(p[x])
    return p[x]


def u(x, y):
    p[f(y)] = f(x)


def k():
    for a, b, c in q:
        if f(a) == f(b):
            continue
        u(a, b)
        if f(s) == f(e):
            print(c)
            exit()


n, m = map(int, input().split())
s, e = map(int, input().split())
p = [i for i in range(n+1)]
q = sorted([tuple(map(int, input().split()))
            for _ in range(m)], key=lambda x: x[2], reverse=True)
k()
print(0)