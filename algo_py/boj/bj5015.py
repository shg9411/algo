def regex(N, P):
    nl, pl = len(N), len(P)
    dp = [[0]*(nl+1) for _ in range(pl+1)]
    dp[0][0] = 1
    for i in range(1, pl+1):
        f = 0
        for j in range(nl+1):
            if P[i-1] == '*':
                f |= dp[i-1][j]
                dp[i][j] = f
            elif j:
                dp[i][j] = dp[i-1][j-1] * (P[i-1] == N[j-1])
    if dp[pl][nl]:
        return True
    return False


P = input()
for _ in range(int(input())):
    N = input()
    if regex(N, P):
        print(N)
