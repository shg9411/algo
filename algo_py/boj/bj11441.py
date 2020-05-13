import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
total = [0]
for n in num:
    total.append(total[-1] + n)
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print(total[j]-total[i-1])
