import heapq
n = int(input())

tmp = [-i for i in range(2, n+1)]
heapq.heapify(tmp)
for i in range(n-1):
    print(-tmp[i],end=' ')
print(1)