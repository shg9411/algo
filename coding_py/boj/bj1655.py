import sys
import bisect
input = sys.stdin.readline

n = int(input())
tmp = []
for i in range(n):
    bisect.insort(tmp, int(input()))
    print(tmp[i//2])
