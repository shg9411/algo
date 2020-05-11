import sys
input = sys.stdin.readline
mod = 1000000007


def xy(x, y):
    res = 1
    while y:
        if y % 2:
            res *= x
            res %= mod
        x *= x
        x %= mod
        y //= 2
    return res


n, k = map(int, input().split())
fact = [0 for _ in range(n+1)]
inverse = [0 for _ in range(n+1)]
fact[1] = 1
for i in range(2, n+1):
    fact[i] = (fact[i-1]*i) % mod
inverse[n] = xy(fact[n], mod-2)
for i in range(n-1, -1, -1):
    inverse[i] = (inverse[i+1]*(i+1)) % mod


r = (((fact[n] * inverse[n-k]) % mod)*inverse[k]) % mod
print(r)
