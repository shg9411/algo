n = int(input())
mod = 1000000007


def calc(a, b):
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= mod
    return c


if n <= 1:
    print(n)
else:
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]
    while n > 0:
        if n % 2 == 1:
            ans = calc(ans, a)
        a = calc(a, a)
        n //= 2
    print(ans[0][1])
