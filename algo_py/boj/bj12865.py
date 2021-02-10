import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n, k = map(int, input().split())
    dp = {0: 0}
    for _ in range(n):
        w, v = map(int, input().split())
        t = {}
        for ck, cv in dp.items():
            if ck+w <= k and dp.get(ck+w, 0) < cv+v:
                t[ck+w] = cv+v
        dp.update(t)
    print(max(dp.values()))


if __name__ == "__main__":
    solve()
