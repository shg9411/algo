import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, s = map(int, input().split())
num = sorted(list(map(int, input().split())))
res = 0

valDict = dict()


def dfs(i, val):
    if i == n//2:
        try:
            valDict[val] += 1
        except:
            valDict[val] = 1
        return

    dfs(i+1, val)
    dfs(i+1, val+num[i])


def dfsAnother(i, val):
    global res
    if i == n:
        try:
            res += valDict.get(s-val)
        except:
            pass
        return
    dfsAnother(i+1, val)
    dfsAnother(i+1, val+num[i])


dfs(0, 0)
dfsAnother(n//2, 0)
print(res if s != 0 else res-1)
