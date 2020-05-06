import math
import sys
input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())
res = 0

for num in people:
    res += 1
    num -= b
    if num > 0:
        res += math.ceil(num/c)
print(res)
