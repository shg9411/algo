import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    fib = [1, 1]
    for _ in range(9999):
        fib.append((fib[-2]+fib[-1]))
    res = []
    for i in range(1, int(input())+1):
        p, q = map(int, input().split())
        res.append("Case #{}: {}".format(i, fib[p-1] % q))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
