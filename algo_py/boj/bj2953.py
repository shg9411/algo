idx = 0
val = 0
for i in range(1, 6):
    tmp = sum(map(int, input().split()))
    if val < tmp:
        val = tmp
        idx = i
print(idx, val)
