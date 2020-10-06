def solve(idx, cnt, diff):
    global res
    if cnt == n//2:
        res = min(res, abs(diff))
        return
    if idx == n:
        return
    solve(idx+1, cnt+1, diff-r[idx]-c[idx])
    solve(idx+1, cnt, diff)


n = int(input())
s = [[0]*n for _ in range(n)]
r = [0]*n
c = [0]*n
t = 0
for i in range(n):
    s[i] = list(map(int, input().split()))
    for j in range(n):
        t += s[i][j]
        r[i] += s[i][j]
        c[j] += s[i][j]
res = 987654321
solve(1, 1, t-r[0]-c[0])
print(res)
