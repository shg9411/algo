import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
num = list(map(int, input().split()))

val = gcd(num[0], num[1])
if n == 3:
    val = gcd(val, num[2])
res = []
for i in range(1, int(val**0.5)+1):
    if val % i == 0:
        res.append(i)
        if i**2 != val:
            res.append(val//i)

for i in sorted(res):
    print(i)
