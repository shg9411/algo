import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
cnt = 0
tmp = num[0]
for x in num[1:]:
    if x >= tmp:
        cnt += 1
        tmp = x
print(cnt)
