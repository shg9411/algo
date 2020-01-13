import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())

su = list(map(int, input().split()))

count = 0

for i in range(1, n+1):
    tmp = list(map(sum,(combinations(su, i))))
    count += tmp.count(s)


print(count)
