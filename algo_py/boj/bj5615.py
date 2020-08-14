def miller(n, m):
    k = n-1
    while not k % 2:
        if pow(m, k, n) == n-1:
            return True
        k >>= 1
    tmp = pow(m, k, n)
    return tmp == n-1 or tmp == 1


def prime(n):
    if n <= 1:
        return False
    if n <= 1000:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    for m in (2, 7, 61):
        if not miller(n, m):
            return False
    return True


res = 0
for num in map(int, (__import__('sys').stdin.read().split()[1:])):
    if prime(num*2+1):
        res += 1
print(res)