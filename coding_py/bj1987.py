
def dfs(selected, v, k):
    global max_count
    for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        i = v[0] + di
        j = v[1] + dj
        if 0 <= i <= r-1 and 0 <= j <= c-1 and not(selected[ord(alpha[i][j])-65]):
            selected[ord(alpha[i][j])-65] = True
            dfs(selected, [i, j], k + 1)
            selected[ord(alpha[i][j])-65] = False
    if k > max_count:
        max_count = k


r, c = map(int, input().split())
max_count = 1
alpha = [input() for _ in range(r)]
sel = [False] * 26
sel[ord(alpha[0][0])-65] = True
dfs(sel, [0, 0], 1)
print(max_count)
