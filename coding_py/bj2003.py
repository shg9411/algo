import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
i = j = 0

ans = 0
tmp = 0
while 1:
    if tmp >= m:
        tmp -= num[i]
        i += 1
    elif j == n:
        break
    else:
        tmp += num[j]
        j += 1
    if tmp == m:
        ans += 1
print(ans)
