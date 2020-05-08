n, m = map(int, input().split(':'))


def gcd(a, b):
    while b:
        tmp = a
        a = b
        b = tmp % b
    return a


x = gcd(n, m)
print(n//x, m//x, sep=':')
