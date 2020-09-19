from gcd import *


def lcm(a, b):
    d = gcd(a, b)
    return d*(a//d)*(b//d)
