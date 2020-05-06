
def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


a, b = map(int, input().split())
if b > a:
    a, b = b, a

print(gcd(a, b))
print(a*b//gcd(a, b))
