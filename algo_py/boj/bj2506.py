n = int(input())
res = 0
tmp = 0
for x in map(int, input().split()):
    if x == 1:
        tmp += 1
        res += tmp
    else:
        tmp = 0
print(res)
