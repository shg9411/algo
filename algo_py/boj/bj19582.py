import sys
input = sys.stdin.readline
n = int(input())
total = maxim = 0
skip = 2
for _ in range(n):
    x, p = map(int, input().split())
    if total <= x:
        total += p
        if maxim < p:
            maxim = p
    elif total - maxim > x or maxim < p:
        skip -= 1
    else:
        skip -= 1
        total -= maxim-p
    if not skip:
        break
if skip:
    print("Kkeo-eok")
else:
    print("Zzz")
