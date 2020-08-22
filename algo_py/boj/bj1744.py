import sys

n = int(input())
num = sorted(list(map(int, sys.stdin.read().splitlines())))
i = res = 0

while i < n:
    if num[i] <= 0:
        if i < n-1 and num[i+1] <= 0:
            res += num[i]*num[i+1]
            i += 2
        else:
            res += num[i]
            i += 1
    else:
        if num[i] == 1:
            res += num[i]
            i += 1
        elif (n-i) % 2 == 0:
            res += num[i]*num[i+1]
            i += 2
        else:
            res += num[i]
            i += 1
print(res)
