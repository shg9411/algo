import sys
input = sys.stdin.readline


def gcd(a, b):
    return gcd(b, a % b) if a % b else b


n = int(input())
num = sorted([int(input()) for _ in range(n)])
get = num[1] - num[0]

for i in range(2, n):
    get = gcd(get, num[i]-num[i-1])

res = set()
for i in range(2, int(get**0.5)+1):
    if get % i == 0:
        res.add(i)
        res.add(get//i)
res.add(get)
res = sorted(list(res))
print(' '.join(map(str, res)))
