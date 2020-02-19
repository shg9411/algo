import sys
import queue
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
pq = queue.PriorityQueue(n)
for x in pre:
    if x[1] != 2000000:
        pq.put(-x[1])
    else:
        if not pq.empty():
            t = -pq.get()
            res+=t
print(res)
