import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
total = [0]
for n in num:
    total.append(total[-1] + n)
for _ in range(m):
    i, j = map(int, input().split())
    print(total[j]-total[i-1])