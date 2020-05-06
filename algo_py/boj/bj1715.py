import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

res = 0

while len(card) > 1:
    tmp = heapq.heappop(card)+heapq.heappop(card)
    heapq.heappush(card, tmp)
    res += tmp
print(res)
