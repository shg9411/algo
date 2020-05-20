import heapq
n = int(input())
oil = []
for _ in range(n):
    oil.append(tuple(map(int, input().split())))
l, p = map(int, input().split())
oil.sort()
hq = []
i = 0
cnt = 0
while p < l:
    while i < n and oil[i][0] <= p:
        heapq.heappush(hq, -oil[i][1])
        i += 1
    if not hq:
        break
    p -= heapq.heappop(hq)
    cnt += 1
print(-1 if p < l else cnt)