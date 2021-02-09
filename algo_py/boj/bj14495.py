f = {1: 1, 2: 1, 3: 1}


def solve(n):
    if n in f:
        return f[n]
    f[n] = solve(n-3)+solve(n-1)
    return f[n]


print(solve(int(input())))
