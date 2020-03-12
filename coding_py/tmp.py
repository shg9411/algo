import sys
import heapq
input = sys.stdin.readline


n, l = map(int, input().split())
que = [10**9+1 for _ in range(l)]
num = list(map(int, input().split()))

for i in num:
    que.pop()
    heapq.heappush(que, i)
    print(que[0])
