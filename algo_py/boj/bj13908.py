import math


def nCr(n, r):
    return math.factorial(n)//math.factorial(r)//math.factorial(n-r)


n, m = map(int, input().split())
input()
res = 0
for i in range(m+1):
    res += ((-1)**i) * nCr(m, i)*((10-i)**n)
print(res)
