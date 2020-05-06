import sys
import heapq
input = sys.stdin.readline
n = int(input())
q = []
res = []
for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        try:
            res.append(heapq.heappop(q)[1])
        except:
            res.append(0)
print('\n'.join(str(i) for i in res))
