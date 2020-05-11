n = int(input())
prime = [2, 3, 5, 7]


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+2):
        if num % i == 0:
            return False
    return True


def dfs(num, n):
    if not n:
        print(num)
    for i in [1, 3, 7, 9]:
        tmp = num*10+i
        if isPrime(tmp):
            dfs(tmp, n-1)


for num in prime:
    dfs(num, n-1)
