import sys
input = sys.stdin.readline


def f(x):
    if p[x] == x:
        return x
    p[x] = f(p[x])
    return p[x]


def u(x, y):
    p[f(y)] = f(x)


def k():
    cnt = r = 0
    for a, b, c in q:
        if f(a) == f(b):
            continue
        cnt += 1
        r += c
        u(a, b)
        if cnt == V-1:
            return r


if __name__ == '__main__':
    V, E = map(int, input().split())
    p = [i for i in range(V+1)]
    q = sorted([tuple(map(int, input().split()))
                for _ in range(E)], key=lambda x: x[2])
    print(k())
