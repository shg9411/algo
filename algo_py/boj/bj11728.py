import heapq
input()
print(*heapq.merge(map(int, input().split()), map(int, input().split())))
