import math
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    res = 0
    for i in range(m):
        res += math.log10(i+1)
    print(int(res+1))
