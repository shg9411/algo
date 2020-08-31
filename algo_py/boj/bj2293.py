import sys


def solve():
    _, k = map(int, input().split())
    money = set(map(int, sys.stdin.read().split()))
    ans = [0] + [100001 for _ in range(k)]
    for m in money:
        for i in range(m, k+1):
            ans[i] = min(ans[i-m]+1, ans[i])
    print(ans[k] if ans[k] < 100001 else -1)


if __name__ == '__main__':
    solve()
