import itertools


def solve():
    n, k = map(int, input().split())
    dp = {0: 0}
    for _ in range(n):
        w, v = map(int, input().split())
        t = []
    for ck, cv in dp.items():
        if ck+w <= k:
            t += (ck+w, cv+v),
    for tk, tv in t:
        if tk <= k:
            if dp.get(tk, 0) < tv:
                dp[tk] = tv
    print(max(dp.values()))


if __name__ == "__main__":
    solve()
