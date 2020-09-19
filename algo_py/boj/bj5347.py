import sys


def gcd(a, b):
    while b:
        r, a = a % b, b
        b = r
    return a


def lcm(a, b):
    d = gcd(a, b)
    return a*b//d


for _ in range(int(input())):
    print(lcm(*map(int, sys.stdin.readline().split())))
