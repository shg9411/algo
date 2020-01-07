t = int(input())


def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a


for _ in range(t):
    num = sorted(list(map(int, input().split()))[1:])
    res = 0
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            print(i, j)
            res += gcd(num[j], num[i])
    print(res)
