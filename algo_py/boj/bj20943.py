import io
import os
import math
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    inc = dict()
    n = int(input())
    for _ in range(n):
        a, b, _ = map(int, input().split())
        if b == 0:
            inc[float("inf")] = inc.get(float("inf"), 0)+1
        else:
            d = math.gcd(a, b)
            a, b = a//d, b//d
            inc[-a/b] = inc.get(-a/b, 0)+1
    ans = n*(n-1)//2
    for _, v in inc.items():
        ans -= v*(v-1)//2
    print(ans)


if __name__ == '__main__':
    solve()
