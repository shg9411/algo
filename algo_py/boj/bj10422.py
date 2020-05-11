T = int(input())


def binomial(n, k):
    tmp = 1
    for i in range(k):
        tmp *= n-i
        tmp //= i+1
    return tmp


def catalan(num):
    tmp = binomial(2*num, num)
    return tmp//(num+1)


for _ in range(T):
    L = int(input())
    if L % 2:
        print(0)
        continue
    print(catalan(L//2) % 1000000007)
