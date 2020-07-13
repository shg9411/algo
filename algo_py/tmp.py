def getMostVisited(n, sprints):
    tmp = [0 for _ in range(n+1)]
    ans = [0 for _ in range(n+1)]
    for i in range(len(sprints)-1):
        x, y = sprints[i], sprints[i+1]
        if x > y:
            x, y = y, x
        tmp[x] += 1
        if y < n:
            tmp[y+1] -= 1
    cur = 0
    for i in range(1, n+1):
        cur += tmp[i]
        ans[i] = cur
    return ans.index(max(ans))


print(getMostVisited(10,[2,4,1,3]))