import io
import os
import sys
import heapq
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    q = []
    res = []
    for _ in range(int(input())):
        if (a := int(input())):
            heapq.heappush(q, -a)
        else:
            res.append(-heapq.heappop(q) if q else 0)
    sys.stdout.write('\n'.join(map(str, res)))


if __name__ == '__main__':
    solve()
