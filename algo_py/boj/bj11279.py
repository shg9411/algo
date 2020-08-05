import sys
import heapq
q = []
res = []
for i in map(int, sys.stdin.read().splitlines()[1:]):
    if i:
        heapq.heappush(q, -i)
    else:
        res.append(-heapq.heappop(q) if q else 0)
print('\n'.join(map(str, res)))