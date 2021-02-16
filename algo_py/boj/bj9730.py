import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

res = []
for i in range(1, int(input())+1):
    input()
    r = p = 0
    for idx, n in enumerate(map(int, input().split())):
        if idx:
            r += max(p, n)
        p = n
    res.append("Case #{}: {}".format(i, r))
sys.stdout.write('\n'.join(res))
