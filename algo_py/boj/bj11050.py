def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)


n, r = map(int, input().split())
print(bino_coef_factorial(n, r))
