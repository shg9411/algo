import sys
input = sys.stdin.readline

n, s = map(int, input().split())

su = list(map(int, input().split()))

res = 0


def dfs(idx, sum):
    global res
    if sum+su[idx] == s:
        res += 1
    if idx == n-1:
        return
    dfs(idx+1, sum)
    dfs(idx+1, sum+su[idx])


dfs(0, 0)
print(res)