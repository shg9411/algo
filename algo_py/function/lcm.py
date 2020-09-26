from gcd import *


def lcm(a, b):
    d = gcd(a, b)
    return a*b//d
