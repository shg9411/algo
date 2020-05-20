import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
pre = []
for _ in range(n):
    m, v = map(int, input().split())
    pre.append([m, v])

for _ in range(k):
    pre.append([int(input()), 2000000])
pre.sort()
res = 0
pq = []
for x in pre:
    if x[1] != 2000000:
        heapq.heappush(pq, -x[1])
    else:
        if pq:
            res -= heapq.heappop(pq)
print(res)
