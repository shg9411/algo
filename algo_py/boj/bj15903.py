import heapq
n, m = map(int, input().split())
num = sorted(map(int, input().split()))

for _ in range(m):
    xy = heapq.heappop(num) + heapq.heappop(num)
    heapq.heappush(num, xy)
    heapq.heappush(num, xy)

print(sum(num))