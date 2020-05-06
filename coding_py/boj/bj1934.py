t = int(input())


def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


for _ in range(t):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    print(a*b//gcd(a, b))
