import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())

arr = list(map(int, input().split()))
q = []

for i in range(n):
    heapq.heappush(q, arr[i])
    if i >= k:
        print(heapq.heappop(q), end=' ')

while q:
    print(heapq.heappop(q), end=' ')
