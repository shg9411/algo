# 유클리드 호제법
def gcd(a, b):
    while b:
        r, a = a % b, b
        b = r
    return a
