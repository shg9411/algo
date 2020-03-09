import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())), reverse=True)
tmp = []


def dfs(i):
    total = sum(tmp)
    if len(tmp) == n:
        if total % n == 0:
            print(' '.join(map(str, tmp)))
            sys.exit()
        else:
            if total < n and num[i] == 0:
                print(-1)
                sys.exit()
            return
    for idx in range(i, 2*n-1):
        tmp.append(num[idx])
        dfs(idx+1)
        tmp.pop()


dfs(0)

print(-1)
