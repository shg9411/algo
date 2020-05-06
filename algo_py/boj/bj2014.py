import heapq

k, n = map(int, input().split())
sosu = list(map(int, input().split()))
mv = max(sosu)
hq = []
for num in sosu:
    heapq.heappush(hq, num)
n -= 1
while n:
    tmp = heapq.heappop(hq)
    for num in sosu:
        val = tmp*num
        if len(hq) >= n and val > mv:
            continue
        heapq.heappush(hq, val)
        mv = max(mv, val)
    n -= 1
print(hq[0])
