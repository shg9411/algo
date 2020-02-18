n, k = map(int, input().split())

total = 0
nc = 9
numlen = 1
ten = 1
tmp = k

while tmp > nc*numlen:
    total += nc
    tmp -= nc*numlen
    nc *= 10
    numlen += 1

total += (tmp-1)//numlen+1

if total > n:
    result = -1
else:
    temp = (tmp-1) % numlen + 1
    for i in range(numlen-1):
        ten *= 10
    for i in range(temp):
        result = total // ten
        total %= ten
        ten //= 10
print(result)
