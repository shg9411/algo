def solution(land):
    ll = len(land)
    dp = [[0 for _ in range(4)] for _ in range(ll)]
    dp[0] = land[0]
    for i in range(1,ll):
        for j in range(4):
            tmpMax = 0
            for tmp in range(4):
                if tmp !=j:
                    tmpMax = max(tmpMax,dp[i-1][tmp])
            dp[i][j] = tmpMax+land[i][j]
    #print(dp)
    return max(dp[ll-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))