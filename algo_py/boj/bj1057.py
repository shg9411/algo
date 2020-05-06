import sys

input = sys.stdin.readline

n, k, i = map(int, input().split())
count = 0

while k != i:
    k = (k+1)//2
    i = (i+1)//2
    count += 1

print(count)
