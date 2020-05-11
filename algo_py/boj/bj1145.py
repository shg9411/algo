import itertools


def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


tmp = list(map(int, input().split()))
ans = 987654321

for x, y, z in itertools.combinations(tmp, 3):
    v = lcm(lcm(x, y), z)
    ans = min(v, ans)
print(ans)
