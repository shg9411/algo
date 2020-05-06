s = int(input())
count = 0
current = 1
while s >= current:
    if s - current >= 0:
        s -= current
        count += 1
    current += 1
print(count)
