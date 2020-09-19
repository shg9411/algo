def gcd(a, b):
    while b:
        r, a = a % b, b
        b = r
    return a


def lcm(a, b):
    d = gcd(a, b)
    return a*b//d


print(lcm(*map(int, input().split())))
