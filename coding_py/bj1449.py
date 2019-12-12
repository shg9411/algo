n, l = map(int, input().split())
l -= 1
hole = list(map(int, input().split()))
hole.sort()
count = 1
tape = hole[0]
for h in range(1, n):
    if hole[h] - tape <= l:
        pass
    else:
        count += 1
        tape = hole[h]

print(count)
