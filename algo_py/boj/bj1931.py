import sys
input = sys.stdin.readline
last = 0
res = 0
for data in sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0])):
    if last <= data[0]:
        last = data[1]
        res += 1
print(res)
