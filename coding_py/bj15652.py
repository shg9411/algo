import sys
n, m = map(int, input().split())
num = [i for i in range(1, n+1)]


def dfs(cnt, idx, res):
    if cnt == m:
        res += '\n'
        sys.stdout.write(' '.join(res))
        return
    for i in range(idx, n):
        dfs(cnt+1, i, res+str(num[i]))


dfs(0, 0, '')
