import sys
import heapq
input = sys.stdin.readline

n, l = map(int, input().split())
num = list(map(int, input().split()))
q = []
for idx, val in enumerate(num):
    heapq.heappush(q, (val, idx))
    tmpVal, tmpIdx = q[0]
    while tmpIdx <= idx-l:
        heapq.heappop(q)
        tmpIdx = q[0][1]
    tmpVal = q[0][0]
    sys.stdout.write(str(tmpVal)+' ')
