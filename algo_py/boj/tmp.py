import io
import os
import sys
import heapq
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline

q = []
res = []
for _ in range(int(input())):
    if (a := int(input())):
        heapq.heappush(q, a)
    else:
        if q:
            res.append(heapq.heappop(q))
        else:
            res.append('0')


sys.stdout.write('\n'.join(map(str, res)))
