n, k = map(int, input().split())
satisfaction = list(map(int, input().split()))
res = 0


def dfs(idx, surplus):
    global res
    if idx == n:
        res = max(res, surplus)
        return
    r = 0
    for i in range(idx, n):
        r += satisfaction[i]
        if r >= k:
            dfs(i+1, surplus+r-k)
            break
    dfs(idx+1, surplus)


dfs(0, 0)
print(res)