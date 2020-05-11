import sys
input = sys.stdin.readline
m = int(input())
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


fact = [0 for _ in range(4000001)]
inverse = [0 for _ in range(4000001)]
fact[1] = 1
for i in range(2, 4000001):
    fact[i] = (fact[i-1]*i) % mod
inverse[4000000] = xy(fact[4000000], mod-2)
for i in range(3999999, -1, -1):
    inverse[i] = (inverse[i+1]*(i+1)) % mod

for _ in range(m):
    n, k = map(int, input().split())
    r = (((fact[n] * inverse[n-k]) % mod)*inverse[k]) % mod
    print(r)
