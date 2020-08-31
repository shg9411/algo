import heapq
n = int(input())
if n > 1022:
    print(-1)
else:
    q = [i for i in range(10)]
    i = -1
    while i < n:
        tmp = heapq.heappop(q)
        i += 1
        if len(q) >= n-i:
            continue
        x = tmp % 10
        nxt = tmp*10
        for xx in range(x):
            heapq.heappush(q, nxt+xx)
    print(tmp)
