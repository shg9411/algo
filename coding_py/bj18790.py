import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())), reverse=True)
tmp = []
total = 0


def dfs(i):
    global total
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
        total += num[idx]
        dfs(idx+1)
        tmp.pop()
        total -= num[idx]


dfs(0)

print(-1)
