import sys
input = sys.stdin.readline


def s():
    def d(i, j):
        return ((s[i][0]-s[j][0])**2+(s[i][1]-s[j][1])**2)**0.5

    def f(x):
        if p[x] == x:
            return x
        p[x] = f(p[x])
        return p[x]

    def u(x, y):
        p[f(y)] = f(x)

    def k(cnt):
        r = 0
        for a, b, c in q:
            if f(a) == f(b):
                continue
            u(a, b)
            r += c
            cnt += 1
            if cnt == n-1:
                break
        return r

    n, m = map(int, input().split())
    p = list(range(n+1))
    s = [0]+[tuple(map(int, input().split())) for _ in range(n)]
    for _ in range(m):
        u(*map(int, input().split()))
    q = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if f(i) != f(j):
                q.append((i, j, d(i, j)))
    q.sort(key=lambda x: x[2])
    print(format(k(m), ".2f"))


if __name__ == '__main__':
    s()
