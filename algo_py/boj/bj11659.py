import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n, m = map(int, input().split())
    total = [0]
    for n in map(int, input().split()):
        total.append(total[-1] + n)
    res = []
    for _ in range(m):
        i, j = map(int, input().split())
        res.append(total[j]-total[i-1])
    sys.stdout.write('\n'.join(map(str, res)))


if __name__ == '__main__':
    solve()
